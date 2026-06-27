from pathlib import Path
import json
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from cortexmorph_xai.agents.longitudinal_change_agent import LongitudinalChangeAgent
from cortexmorph_xai.agents.morphometry_agent import MorphometryAgent
from cortexmorph_xai.agents.surface_data_agent import SurfaceDataAgent
from cortexmorph_xai.reports.markdown import write_markdown_report
from cortexmorph_xai.synthetic.surface_mesh import generate_surface_case, save_case


def make_followup_case():
    case = generate_surface_case(case_id="CMX-SYN-001-FOLLOWUP", grid_size=12)

    for index in case.anomaly_vertex_indices:
        case.features[index]["curvature"] = round(case.features[index]["curvature"] + 0.18, 4)
        case.features[index]["sulcal_depth"] = round(case.features[index]["sulcal_depth"] + 0.08, 4)

    return case


if __name__ == "__main__":
    baseline = generate_surface_case(case_id="CMX-SYN-001-BASELINE", grid_size=12)
    followup = make_followup_case()

    save_case(baseline, PROJECT_ROOT / "data" / "baseline_surface_case.json")
    save_case(followup, PROJECT_ROOT / "data" / "followup_surface_case.json")

    data_audit = SurfaceDataAgent().run(baseline)
    morphometry = MorphometryAgent().run(baseline)
    longitudinal = LongitudinalChangeAgent().run(baseline, followup)

    audit = {
        "baseline_case_id": baseline.case_id,
        "followup_case_id": followup.case_id,
        "data_audit": data_audit,
        "morphometry": morphometry,
        "longitudinal_change": longitudinal,
        "limitations": "Synthetic surface data only; not clinical neuroimaging output.",
    }

    json_path = PROJECT_ROOT / "reports" / "cortexmorph_audit.json"
    json_path.write_text(json.dumps(audit, indent=2), encoding="utf-8")

    write_markdown_report(
        PROJECT_ROOT / "reports" / "cortexmorph_audit_report.md",
        "CortexMorph-XAI Agentic Cortical Surface Audit Report",
        {
            "Surface data audit": data_audit,
            "Morphometry summary": morphometry,
            "Longitudinal change": longitudinal,
            "Safety note": "Synthetic surface data only. This is a research prototype, not a clinical tool.",
        },
    )

    print("Wrote reports/cortexmorph_audit.json")
    print("Wrote reports/cortexmorph_audit_report.md")
