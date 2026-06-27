import unittest
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from cortexmorph_xai.longitudinal.change import longitudinal_feature_change


class TestLongitudinalChange(unittest.TestCase):
    def test_change_detects_difference(self):
        baseline = [{"curvature": 0.1}, {"curvature": 0.2}]
        followup = [{"curvature": 0.1}, {"curvature": 0.5}]
        summary = longitudinal_feature_change(baseline, followup)
        self.assertTrue(summary["requires_review"])
        self.assertEqual(summary["high_change_vertices"], 1)


if __name__ == "__main__":
    unittest.main()
