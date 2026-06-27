import unittest
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from cortexmorph_xai.graph.mesh_graph import graph_summary, mesh_edges_from_faces


class TestMeshGraph(unittest.TestCase):
    def test_edges_are_unique(self):
        edges = mesh_edges_from_faces([[0, 1, 2], [2, 1, 0]])
        self.assertEqual(len(edges), 3)

    def test_graph_summary_counts_vertices(self):
        summary = graph_summary(3, [[0, 1, 2]])
        self.assertEqual(summary["n_vertices"], 3)
        self.assertEqual(summary["n_edges"], 3)


if __name__ == "__main__":
    unittest.main()
