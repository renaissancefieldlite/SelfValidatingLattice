# SelfValidatingLattice

Architecture-level coherence model for the seven-experiment stack and its
supporting nodes.

This repo is not a direct hardware experiment. It is the system-coherence layer
that asks whether the graph remains internally stable under baseline and
hardware-derived perturbation assumptions.

That places it mainly in the architecture layer of the stack. It can be linked
to the transition-cadence program, but it should not be mistaken for a direct
measurement repo.

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
