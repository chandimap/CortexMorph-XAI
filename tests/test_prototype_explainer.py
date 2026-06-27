import unittest
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from cortexmorph_xai.xai.prototype_explainer import top_anomaly_prototypes


class TestPrototypeExplainer(unittest.TestCase):
    def test_top_prototype_has_highest_anomaly(self):
        features = [
            {"anomaly_strength": 0.1, "curvature": 0.2, "sulcal_depth": 0.1},
            {"anomaly_strength": 0.9, "curvature": 0.5, "sulcal_depth": 0.4},
        ]
        prototypes = top_anomaly_prototypes(features, top_k=1)
        self.assertEqual(prototypes[0]["vertex_index"], 1)


if __name__ == "__main__":
    unittest.main()
