from __future__ import annotations


def _bounded(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, value))


def uncertainty_aware_anomaly_review(
    features: list[dict[str, float]],
    anomaly_threshold: float = 0.15,
    uncertainty_margin: float = 0.05,
    top_k: int = 5,
) -> dict[str, object]:
    """Rank vertices using anomaly evidence and threshold-neighbourhood uncertainty.

    The aim is not to produce clinical uncertainty. It provides a transparent
    research signal for deciding which synthetic vertices deserve explanation
    or manual review in the agentic workflow.
    """
    if not features:
        raise ValueError("features cannot be empty")

    if uncertainty_margin <= 0:
        raise ValueError("uncertainty_margin must be positive")

    scored_vertices: list[dict[str, float | int | bool]] = []

    for vertex_index, feature in enumerate(features):
        anomaly_strength = float(feature.get("anomaly_strength", 0.0))
        curvature = abs(float(feature.get("curvature", 0.0)))
        sulcal_depth = abs(float(feature.get("sulcal_depth", 0.0)))

        risk_score = anomaly_strength + 0.2 * curvature + 0.1 * sulcal_depth

        distance_from_threshold = abs(anomaly_strength - anomaly_threshold)
        uncertainty_score = _bounded(1.0 - distance_from_threshold / uncertainty_margin)

        needs_review = (
            anomaly_strength >= anomaly_threshold
            or uncertainty_score >= 0.5
            or risk_score >= anomaly_threshold + 0.1
        )

        scored_vertices.append(
            {
                "vertex_index": vertex_index,
                "anomaly_strength": round(anomaly_strength, 4),
                "curvature": round(curvature, 4),
                "sulcal_depth": round(sulcal_depth, 4),
                "risk_score": round(risk_score, 4),
                "uncertainty_score": round(uncertainty_score, 4),
                "needs_review": needs_review,
            }
        )

    ranked = sorted(
        scored_vertices,
        key=lambda item: (
            float(item["needs_review"]),
            float(item["risk_score"]),
            float(item["uncertainty_score"]),
        ),
        reverse=True,
    )

    review_vertices = [item for item in scored_vertices if bool(item["needs_review"])]
    uncertain_vertices = [
        item for item in scored_vertices if float(item["uncertainty_score"]) >= 0.5
    ]

    mean_risk = sum(float(item["risk_score"]) for item in scored_vertices) / len(scored_vertices)
    max_risk = max(float(item["risk_score"]) for item in scored_vertices)

    return {
        "n_vertices": len(features),
        "review_vertex_count": len(review_vertices),
        "uncertain_vertex_count": len(uncertain_vertices),
        "mean_risk_score": round(mean_risk, 4),
        "max_risk_score": round(max_risk, 4),
        "top_review_vertices": ranked[:top_k],
        "requires_review": len(review_vertices) > 0,
        "interpretation": (
            "High review counts indicate synthetic vertices where anomaly strength, "
            "curvature, sulcal depth, or threshold-neighbourhood uncertainty should be inspected."
        ),
    }
