from __future__ import annotations


def top_anomaly_prototypes(
    features: list[dict[str, float]],
    top_k: int = 5,
) -> list[dict[str, float | int]]:
    """Return vertices that best explain the synthetic anomaly signal."""
    ranked = sorted(
        enumerate(features),
        key=lambda item: (
            item[1].get("anomaly_strength", 0.0),
            item[1].get("curvature", 0.0),
        ),
        reverse=True,
    )

    prototypes: list[dict[str, float | int]] = []

    for vertex_index, feature in ranked[:top_k]:
        prototypes.append(
            {
                "vertex_index": vertex_index,
                "anomaly_strength": feature.get("anomaly_strength", 0.0),
                "curvature": feature.get("curvature", 0.0),
                "sulcal_depth": feature.get("sulcal_depth", 0.0),
            }
        )

    return prototypes
