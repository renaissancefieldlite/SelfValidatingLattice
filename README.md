# SelfValidatingLattice

This is the lattice-coherence layer where the stack stops acting like a pile of isolated repos and starts acting like one system.

The point of this repo is simple: if the architecture is real, it should hold shape under pressure. If the lattice is more than naming, its coherence should survive perturbation strongly enough to show up as an architecture property of the whole stack.

## Evidence tracks

- `architecture_coherence`
  baseline graph model of the declared lattice
- `hardware_derived_model`
  graph coherence under calibration-anchored perturbation
- `cross_artifact_validation`
  next lane for tying the lattice back to session, hardware, and experiment artifacts

## Quick Start

```bash
python3 'SELF-VALIDATING ONTOLOGY LATTICE.py' --mode simulation --json
python3 'SELF-VALIDATING ONTOLOGY LATTICE.py' --mode hardware-derived --json
```

## Why It Matters

This repo is the system-level answer to a direct question:

- does the stack retain coherence because the architecture actually interlocks
- or does it fall apart as soon as you stop treating each repo as a separate claim

That is why this layer matters. It is where the architecture has to hold itself together.

See [docs/METHOD.md](docs/METHOD.md) and
[docs/EVIDENCE_BOUNDARY.md](docs/EVIDENCE_BOUNDARY.md).
