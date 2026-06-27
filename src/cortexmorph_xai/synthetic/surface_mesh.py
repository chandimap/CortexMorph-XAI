from __future__ import annotations

import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class SurfaceMeshCase:
    case_id: str
    vertices: list[list[float]]
    faces: list[list[int]]
    features: list[dict[str, float]]
    anomaly_vertex_indices: list[int]
    note: str


def generate_surface_case(case_id: str = "CMX-SYN-001", grid_size: int = 12) -> SurfaceMeshCase:
    """Create a synthetic cortical-surface-style mesh for research workflow testing."""
    vertices: list[list[float]] = []
    features: list[dict[str, float]] = []
    anomaly_indices: list[int] = []

    centre = (grid_size - 1) / 2

    for y in range(grid_size):
        for x in range(grid_size):
            nx = (x - centre) / centre
            ny = (y - centre) / centre
            z = 0.15 * math.sin(math.pi * nx) * math.cos(math.pi * ny)

            distance = math.sqrt((nx - 0.35) ** 2 + (ny + 0.15) ** 2)
            anomaly_strength = max(0.0, 1.0 - distance / 0.35)

            if anomaly_strength > 0.15:
                z += 0.25 * anomaly_strength
                anomaly_indices.append(len(vertices))

            curvature = abs(0.4 * math.sin(math.pi * nx) + 0.3 * math.cos(math.pi * ny)) + anomaly_strength
            sulcal_depth = abs(z) + 0.2 * anomaly_strength

            vertices.append([round(nx, 4), round(ny, 4), round(z, 4)])
            features.append(
                {
                    "curvature": round(curvature, 4),
                    "sulcal_depth": round(sulcal_depth, 4),
                    "anomaly_strength": round(anomaly_strength, 4),
                }
            )

    faces: list[list[int]] = []
    for y in range(grid_size - 1):
        for x in range(grid_size - 1):
            top_left = y * grid_size + x
            top_right = top_left + 1
            bottom_left = top_left + grid_size
            bottom_right = bottom_left + 1
            faces.append([top_left, bottom_left, top_right])
            faces.append([top_right, bottom_left, bottom_right])

    return SurfaceMeshCase(
        case_id=case_id,
        vertices=vertices,
        faces=faces,
        features=features,
        anomaly_vertex_indices=anomaly_indices,
        note="Synthetic cortical-surface-style case; not patient data.",
    )


def save_case(case: SurfaceMeshCase, output_path: str | Path) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(asdict(case), indent=2), encoding="utf-8")


def load_case(input_path: str | Path) -> SurfaceMeshCase:
    data = json.loads(Path(input_path).read_text(encoding="utf-8"))
    return SurfaceMeshCase(**data)
