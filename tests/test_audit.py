import datetime as dt
import sys
import unittest

sys.path.insert(0, "scripts")
import audit

NOW = dt.datetime(2026, 10, 5, tzinfo=dt.timezone.utc)


def meta(**kw):
    base = {"full_name": "o/r", "archived": False, "disabled": False, "license": {"spdx_id": "MIT"}}
    base.update(kw)
    return base


class Parse(unittest.TestCase):
    def test_entries(self):
        text = "- [A](https://github.com/o/a) - x.\n- [B](https://jetty.io) - y.\nprose [C](https://github.com/o/c)\n"
        self.assertEqual(
            audit.parse(text),
            [("A", "https://github.com/o/a", ("o", "a")), ("B", "https://jetty.io", None)],
        )

    def test_toc_anchors_are_not_entries(self):
        self.assertEqual(audit.parse("- [Section](#section)\n"), [])

    def test_subpath_url(self):
        (e,) = audit.parse("- [S](https://github.com/o/community/blob/main/p.md) - z.\n")
        self.assertEqual(e[2], ("o", "community"))


class Judge(unittest.TestCase):
    def j(self, m, age=10):
        return audit.judge("n", "o", "r", m, NOW - dt.timedelta(days=age), NOW)

    def test_clean(self):
        self.assertEqual(self.j(meta()), [])

    def test_archived(self):
        self.assertIn("remove", [s for s, _ in self.j(meta(archived=True))])

    def test_renamed(self):
        self.assertEqual(self.j(meta(full_name="new/r"))[0][0], "fix")

    def test_stale_and_watch(self):
        self.assertEqual(self.j(meta(), age=400)[0][0], "remove")
        self.assertEqual(self.j(meta(), age=300)[0][0], "watch")
        self.assertEqual(self.j(meta(), age=365), [("watch", "last commit 365 days ago; goes stale in 0 days")])

    def test_no_license(self):
        self.assertEqual(self.j(meta(license=None))[0][0], "check")


if __name__ == "__main__":
    unittest.main()
