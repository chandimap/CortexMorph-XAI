# Surface Quality Control Notes

This project now includes lightweight surface quality-control checks for synthetic cortical-surface-style meshes.

The quality-control module evaluates:

- invalid triangle faces
- duplicate faces
- unused vertices
- edge-length distribution
- geometric irregularity signals
- review flags for downstream agentic reporting

These checks are not clinical validation. They are research-oriented safeguards for testing whether later morphometry, anomaly, and longitudinal analyses are operating on structurally plausible surface data.
