from __future__ import annotations

from cortexmorph_xai.longitudinal.change import longitudinal_feature_change


class LongitudinalChangeAgent:
    """Compare baseline and follow-up surface feature evidence."""

    def run(self, baseline_case: object, followup_case: object) -> dict[str, object]:
        change = longitudinal_feature_change(
            baseline_case.features,
            followup_case.features,
            feature_name="curvature",
        )
        change["agent"] = "LongitudinalChangeAgent"
        return change
