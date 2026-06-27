# CortexMorph-XAI Technical Report

## Research question

How can an agentic cortical-surface AI workflow support auditable morphometry, anomaly explanation, longitudinal change analysis, and graph-based reasoning over surface meshes?

## Current prototype

The repository implements a synthetic cortical-surface mesh generator, morphometry summaries, anomaly patch simulation, longitudinal feature-change scoring, mesh-to-graph summaries, prototype explanations, and report generation.

## Agentic design

The project separates the workflow into specialised components:

- surface validation before analysis;
- morphometry calculation before explanation;
- longitudinal change review as a separate evidence source;
- prototype-based explanation of anomalous vertices;
- structured reporting with limitations.

## Current limitation

This version uses synthetic cortical-surface-style data only. It does not yet process FreeSurfer, FastSurfer, or real MRI outputs. The next stage is to add real neuroimaging file interfaces, graph neural baselines, and richer surface visualisation.
