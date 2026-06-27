# CortexMorph-XAI

CortexMorph-XAI is a research prototype for agentic, explainable cortical-surface morphometry. It explores synthetic cortical-surface meshes, anomaly simulation, longitudinal change scoring, mesh graph features, prototype explanations, and auditable reports.

This repository is an independent research prototype. It is not a clinical neuroimaging tool and must not be used for diagnosis or treatment decisions.

## Research aim

The project investigates how agentic AI can structure cortical-surface analysis by separating surface validation, morphometry calculation, anomaly detection, longitudinal change analysis, explanation, and reporting.

## Current components

- Synthetic cortical-surface-style mesh generator
- Morphometry-style feature calculation
- Surface area calculation
- Reproducible scripts
- Unit tests
- Documentation for cortical-surface terminology

## Run

```bash
python scripts/generate_surface_case.py
python -m unittest discover tests
```
