from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from cortexmorph_xai.qc.surface_quality import surface_quality_summary
from cortexmorph_xai.synthetic.surface_mesh import generate_surface_case


class TestSurfaceQuality(unittest.TestCase):
    def test_generated_surface_has_quality_summary(self):
        case = generate_surface_case(grid_size=8)
        summary = surface_quality_summary(case.vertices, case.faces)

        self.assertEqual(summary["n_vertices"], len(case.vertices))
        self.assertEqual(summary["n_faces"], len(case.faces))
        self.assertGreater(summary["mean_edge_length"], 0)
        self.assertIn(summary["quality_label"], {"acceptable", "monitor", "requires_review"})

    def test_invalid_face_is_detected(self):
        case = generate_surface_case(grid_size=6)
        broken_faces = case.faces + [[0, 1, len(case.vertices) + 10]]
        summary = surface_quality_summary(case.vertices, broken_faces)

        self.assertEqual(summary["invalid_face_count"], 1)
        self.assertTrue(summary["requires_review"])


if __name__ == "__main__":
    unittest.main()
