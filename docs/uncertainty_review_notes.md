# Uncertainty-Aware Anomaly Review

This module adds a simple uncertainty-aware review signal for synthetic cortical-surface experiments.

The score combines:

- synthetic anomaly strength
- curvature evidence
- sulcal-depth evidence
- distance from the anomaly-review threshold

The purpose is to support transparent research triage: vertices near a decision boundary or with strong anomaly evidence are surfaced for explanation and review.
