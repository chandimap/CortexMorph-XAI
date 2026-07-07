from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from cortexmorph_xai.synthetic.surface_mesh import generate_surface_case
from cortexmorph_xai.xai.uncertainty import uncertainty_aware_anomaly_review


class TestUncertaintyAwareAnomalyReview(unittest.TestCase):
    def test_uncertainty_review_returns_ranked_vertices(self):
        case = generate_surface_case(grid_size=8)
        review = uncertainty_aware_anomaly_review(case.features, top_k=3)

        self.assertEqual(review["n_vertices"], len(case.features))
        self.assertEqual(len(review["top_review_vertices"]), 3)
        self.assertIn("mean_risk_score", review)
        self.assertIn("requires_review", review)

    def test_empty_features_are_rejected(self):
        with self.assertRaises(ValueError):
            uncertainty_aware_anomaly_review([])


if __name__ == "__main__":
    unittest.main()
