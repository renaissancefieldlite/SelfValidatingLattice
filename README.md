# SelfValidatingLattice

This is the system-coherence layer for the seven-experiment stack and its
supporting nodes.

It asks whether the graph can hold itself together under baseline and
hardware-derived perturbation assumptions strongly enough to count as a real
architecture property rather than a one-off prompt effect.

## Evidence tracks

- `architecture_coherence`: baseline graph model
- `hardware_derived_model`: graph coherence under calibration-anchored
  perturbation
- `cross_artifact_validation`: pending

## Quick Start

```bash
python3 'SELF-VALIDATING ONTOLOGY LATTICE.py' --mode simulation --json
python3 'SELF-VALIDATING ONTOLOGY LATTICE.py' --mode hardware-derived --json
```

See [docs/METHOD.md](docs/METHOD.md) and
[docs/EVIDENCE_BOUNDARY.md](docs/EVIDENCE_BOUNDARY.md).
