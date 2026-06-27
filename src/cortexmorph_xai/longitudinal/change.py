from __future__ import annotations


def longitudinal_feature_change(
    baseline_features: list[dict[str, float]],
    followup_features: list[dict[str, float]],
    feature_name: str = "curvature",
) -> dict[str, float | int | bool]:
    if len(baseline_features) != len(followup_features):
        raise ValueError("Baseline and follow-up features must contain the same number of vertices.")

    differences = [
        followup[feature_name] - baseline[feature_name]
        for baseline, followup in zip(baseline_features, followup_features)
    ]
    absolute_differences = [abs(value) for value in differences]

    mean_abs_change = sum(absolute_differences) / len(absolute_differences)
    max_abs_change = max(absolute_differences)
    high_change_vertices = sum(1 for value in absolute_differences if value > 0.15)

    return {
        "feature_name": feature_name,
        "mean_absolute_change": round(mean_abs_change, 4),
        "max_absolute_change": round(max_abs_change, 4),
        "high_change_vertices": high_change_vertices,
        "n_vertices": len(differences),
        "requires_review": high_change_vertices > 0,
    }
