from __future__ import annotations


class SurfaceDataAgent:
    """Check structural validity of a cortical-surface research case."""

    def run(self, case: object) -> dict[str, object]:
        vertices = getattr(case, "vertices")
        faces = getattr(case, "faces")
        features = getattr(case, "features")

        n_vertices = len(vertices)
        valid_faces = all(
            len(face) == 3 and all(0 <= index < n_vertices for index in face)
            for face in faces
        )
        feature_complete = len(features) == n_vertices

        return {
            "agent": "SurfaceDataAgent",
            "n_vertices": n_vertices,
            "n_faces": len(faces),
            "valid_faces": valid_faces,
            "feature_complete": feature_complete,
            "requires_review": not valid_faces or not feature_complete,
        }
