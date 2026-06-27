import unittest
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from cortexmorph_xai.features.morphometry import morphometry_summary, surface_area
from cortexmorph_xai.synthetic.surface_mesh import generate_surface_case


class TestMorphometry(unittest.TestCase):
    def test_surface_area_is_positive(self):
        case = generate_surface_case(grid_size=6)
        self.assertGreater(surface_area(case.vertices, case.faces), 0)

    def test_summary_contains_anomaly_count(self):
        case = generate_surface_case(grid_size=6)
        summary = morphometry_summary(case.vertices, case.faces, case.features)
        self.assertIn("anomalous_vertex_count", summary)
        self.assertGreater(summary["n_vertices"], 0)


if __name__ == "__main__":
    unittest.main()
