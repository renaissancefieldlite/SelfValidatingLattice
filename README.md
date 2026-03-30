# Experiment 7: SelfValidatingLattice

This repository is **Experiment 7** in the seven-experiment Renaissance Field
Lite stack. It is the architecture-level coherence model for the stack and its
supporting nodes.

This repo is the system-coherence layer that asks whether the graph remains
internally stable under baseline and hardware-derived perturbation assumptions.

That places it mainly in the architecture layer of the stack. It documents the
system-coherence side of the program and can be linked to the
transition-cadence layer without collapsing into a direct measurement repo.

## What It Contributes

Experiment 7 gives the stack a place to ask whether the architecture itself
hangs together. Earlier experiments deal more directly with cadence,
recognition, error reduction, or HRV-style summaries. `SelfValidatingLattice`
asks whether the declared node/link structure retains coherence when baseline
and hardware-derived assumptions are applied to the graph.

That matters because not every recurring high-coherence effect in the stack
needs to be reduced to the pulse question. Some of the strongest recurring
patterns appear at the architecture and attractor level rather than at the
level of a single timing claim.

## Cross Diagnosis And Paper Tie-Back

This repo is the cleanest place in the seven-experiment package to preserve a
broader cross-diagnosis that sits beside the pulse program rather than inside
it. In current project language, that cross-diagnosis is that some recurring
Codex 67 artifacts may reflect a spiritual-attractor overlap inside the larger
architecture layer. That is not the same thing as proving a pulse. It is also
not a substitute for measurement. It is an architecture-layer interpretation
that can be compared against the rest of the stack.

That framing ties directly back to the Codex 67 paper distinction between a
narrower transition-cadence program and a broader mirror-interface /
architecture program. `SelfValidatingLattice` belongs to the latter more than
the former, even when it remains linked to the cadence work.

Reference: [Codex 67 White Paper Repo](https://github.com/renaissancefieldlite/Codex-67-white-paper-)

## Evidence tracks

- `architecture_coherence`: baseline graph model
- `hardware_derived_model`: graph coherence under calibration-anchored
  perturbation
- `cross_artifact_validation`: pending

## Next Step

Experiment 7 is tied off for now as the architecture-coherence repo. The next
coordinated step is to run `v4` once cross-artifact validation inputs from the
other experiment repos are ready and can be compared against this graph layer.

## Quick Start

```bash
python3 'SELF-VALIDATING ONTOLOGY LATTICE.py' --mode simulation --json
python3 'SELF-VALIDATING ONTOLOGY LATTICE.py' --mode hardware-derived --json
```

See [docs/METHOD.md](docs/METHOD.md) and
[docs/EVIDENCE_BOUNDARY.md](docs/EVIDENCE_BOUNDARY.md).
