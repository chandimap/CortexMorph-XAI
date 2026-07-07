from __future__ import annotations

import math


def _euclidean_distance(first: list[float], second: list[float]) -> float:
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(first, second)))


def _valid_triangle_face(face: list[int], n_vertices: int) -> bool:
    return (
        len(face) == 3
        and len(set(face)) == 3
        and all(isinstance(index, int) for index in face)
        and all(0 <= index < n_vertices for index in face)
    )


def edge_lengths(vertices: list[list[float]], faces: list[list[int]]) -> list[float]:
    """Return all triangle edge lengths from a surface mesh."""
    lengths: list[float] = []
    n_vertices = len(vertices)

    for face in faces:
        if not _valid_triangle_face(face, n_vertices):
            continue

        a, b, c = face
        lengths.append(_euclidean_distance(vertices[a], vertices[b]))
        lengths.append(_euclidean_distance(vertices[b], vertices[c]))
        lengths.append(_euclidean_distance(vertices[a], vertices[c]))

    return lengths


def surface_quality_summary(
    vertices: list[list[float]],
    faces: list[list[int]],
) -> dict[str, object]:
    """Summarise basic geometric quality-control signals for a surface mesh."""
    if not vertices:
        raise ValueError("vertices cannot be empty")

    if not faces:
        raise ValueError("faces cannot be empty")

    n_vertices = len(vertices)
    invalid_face_count = sum(
        1 for face in faces if not _valid_triangle_face(face, n_vertices)
    )

    canonical_faces = [
        tuple(sorted(face))
        for face in faces
        if _valid_triangle_face(face, n_vertices)
    ]
    duplicate_face_count = len(canonical_faces) - len(set(canonical_faces))

    used_vertices = {
        index
        for face in faces
        if _valid_triangle_face(face, n_vertices)
        for index in face
    }
    unused_vertex_count = n_vertices - len(used_vertices)

    lengths = edge_lengths(vertices, faces)
    if not lengths:
        raise ValueError("no valid mesh edges could be calculated")

    mean_length = sum(lengths) / len(lengths)
    min_length = min(lengths)
    max_length = max(lengths)
    length_variance = sum((value - mean_length) ** 2 for value in lengths) / len(lengths)
    length_std = math.sqrt(length_variance)
    edge_length_cv = length_std / mean_length if mean_length else 0.0
    edge_length_ratio = max_length / min_length if min_length else float("inf")

    risk_flags: list[str] = []
    if invalid_face_count:
        risk_flags.append("invalid_triangle_faces")
    if duplicate_face_count:
        risk_flags.append("duplicate_faces")
    if unused_vertex_count:
        risk_flags.append("unused_vertices")
    if edge_length_ratio > 4.0:
        risk_flags.append("large_edge_length_ratio")
    if edge_length_cv > 0.45:
        risk_flags.append("irregular_edge_length_distribution")

    if invalid_face_count or duplicate_face_count or unused_vertex_count:
        quality_label = "requires_review"
    elif risk_flags:
        quality_label = "monitor"
    else:
        quality_label = "acceptable"

    return {
        "n_vertices": n_vertices,
        "n_faces": len(faces),
        "valid_face_count": len(faces) - invalid_face_count,
        "invalid_face_count": invalid_face_count,
        "duplicate_face_count": duplicate_face_count,
        "unused_vertex_count": unused_vertex_count,
        "mean_edge_length": round(mean_length, 4),
        "min_edge_length": round(min_length, 4),
        "max_edge_length": round(max_length, 4),
        "edge_length_cv": round(edge_length_cv, 4),
        "edge_length_ratio": round(edge_length_ratio, 4),
        "quality_label": quality_label,
        "risk_flags": risk_flags,
        "requires_review": quality_label == "requires_review",
    }
