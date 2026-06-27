from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from cortexmorph_xai.graph.mesh_graph import graph_summary
from cortexmorph_xai.reports.markdown import write_markdown_report
from cortexmorph_xai.synthetic.surface_mesh import generate_surface_case
from cortexmorph_xai.xai.prototype_explainer import top_anomaly_prototypes


if __name__ == "__main__":
    case = generate_surface_case(grid_size=12)
    graph = graph_summary(len(case.vertices), case.faces)
    prototypes = top_anomaly_prototypes(case.features, top_k=5)

    prototype_section = {
        f"prototype_{index + 1}": prototype
        for index, prototype in enumerate(prototypes)
    }

    write_markdown_report(
        PROJECT_ROOT / "reports" / "graph_explanation_report.md",
        "CortexMorph-XAI Mesh Graph and Prototype Explanation Report",
        {
            "Graph summary": graph,
            "Prototype vertices": prototype_section,
            "Interpretation": "Prototype vertices identify the strongest synthetic anomaly and curvature evidence.",
        },
    )

    print("Wrote reports/graph_explanation_report.md")
