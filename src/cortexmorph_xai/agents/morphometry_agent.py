from __future__ import annotations

from cortexmorph_xai.features.morphometry import morphometry_summary


class MorphometryAgent:
    """Calculate interpretable surface morphometry descriptors."""

    def run(self, case: object) -> dict[str, object]:
        summary = morphometry_summary(case.vertices, case.faces, case.features)
        summary["agent"] = "MorphometryAgent"
        summary["requires_review"] = summary["anomalous_vertex_count"] > 0
        return summary
