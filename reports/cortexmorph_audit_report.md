# CortexMorph-XAI Agentic Cortical Surface Audit Report

Created: 2026-06-27T18:48:43.160793+00:00

## Surface data audit

- **agent**: SurfaceDataAgent
- **n_vertices**: 144
- **n_faces**: 242
- **valid_faces**: True
- **feature_complete**: True
- **requires_review**: False

## Morphometry summary

- **n_vertices**: 144
- **mean_curvature**: 0.3144
- **max_curvature**: 1.3407
- **mean_sulcal_depth**: 0.0699
- **max_anomaly_strength**: 0.7221
- **anomalous_vertex_count**: 9
- **surface_area**: 4.3218
- **agent**: MorphometryAgent
- **requires_review**: True

## Longitudinal change

- **feature_name**: curvature
- **mean_absolute_change**: 0.0112
- **max_absolute_change**: 0.18
- **high_change_vertices**: 9
- **n_vertices**: 144
- **requires_review**: True
- **agent**: LongitudinalChangeAgent

## Safety note

Synthetic surface data only. This is a research prototype, not a clinical tool.
