from __future__ import annotations


def mesh_edges_from_faces(faces: list[list[int]]) -> list[tuple[int, int]]:
    edges: set[tuple[int, int]] = set()

    for a, b, c in faces:
        for first, second in [(a, b), (b, c), (a, c)]:
            edge = (first, second) if first < second else (second, first)
            edges.add(edge)

    return sorted(edges)


def vertex_degrees(n_vertices: int, edges: list[tuple[int, int]]) -> list[int]:
    degrees = [0 for _ in range(n_vertices)]

    for first, second in edges:
        degrees[first] += 1
        degrees[second] += 1

    return degrees


def graph_summary(n_vertices: int, faces: list[list[int]]) -> dict[str, float | int]:
    edges = mesh_edges_from_faces(faces)
    degrees = vertex_degrees(n_vertices, edges)

    return {
        "n_vertices": n_vertices,
        "n_edges": len(edges),
        "mean_degree": round(sum(degrees) / len(degrees), 4),
        "max_degree": max(degrees),
        "min_degree": min(degrees),
    }
