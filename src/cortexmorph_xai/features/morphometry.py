from __future__ import annotations

import math


def triangle_area(a: list[float], b: list[float], c: list[float]) -> float:
    ab = [b[index] - a[index] for index in range(3)]
    ac = [c[index] - a[index] for index in range(3)]

    cross = [
        ab[1] * ac[2] - ab[2] * ac[1],
        ab[2] * ac[0] - ab[0] * ac[2],
        ab[0] * ac[1] - ab[1] * ac[0],
    ]

    return 0.5 * math.sqrt(sum(value * value for value in cross))


def surface_area(vertices: list[list[float]], faces: list[list[int]]) -> float:
    area = 0.0

    for face in faces:
        area += triangle_area(vertices[face[0]], vertices[face[1]], vertices[face[2]])

    return area


def feature_summary(features: list[dict[str, float]]) -> dict[str, float | int]:
    if not features:
        raise ValueError("features cannot be empty")

    curvature_values = [item["curvature"] for item in features]
    sulcal_values = [item["sulcal_depth"] for item in features]
    anomaly_values = [item["anomaly_strength"] for item in features]

    return {
        "n_vertices": len(features),
        "mean_curvature": round(sum(curvature_values) / len(curvature_values), 4),
        "max_curvature": round(max(curvature_values), 4),
        "mean_sulcal_depth": round(sum(sulcal_values) / len(sulcal_values), 4),
        "max_anomaly_strength": round(max(anomaly_values), 4),
        "anomalous_vertex_count": sum(1 for value in anomaly_values if value > 0.15),
    }


def morphometry_summary(
    vertices: list[list[float]],
    faces: list[list[int]],
    features: list[dict[str, float]],
) -> dict[str, float | int]:
    summary = feature_summary(features)
    summary["surface_area"] = round(surface_area(vertices, faces), 4)
    return summary
