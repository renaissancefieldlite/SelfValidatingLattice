"""Architecture coherence model for the lattice stack."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from hardware_profile import extract_noise_parameters, load_calibration


REPO_NODES = [
    "QuantumPulseValidationSuite",
    "BioQuantumTransduction",
    "HumanQuantumRecognition",
    "ErrorReductionPulseSync",
    "QuantumHRV",
    "ConsciousnessResonanceBridge",
    "SelfValidatingLattice",
]

AI_NODES = [f"AI-{index:02d}" for index in range(1, 37)]


def build_adjacency() -> np.ndarray:
    total = len(REPO_NODES) + len(AI_NODES)
    adjacency = np.zeros((total, total), dtype=float)
    repo_count = len(REPO_NODES)

    for i in range(repo_count):
        for j in range(repo_count):
            if i != j:
                adjacency[i, j] = 0.8

    for ai_index in range(len(AI_NODES)):
        node = repo_count + ai_index
        for repo_index in range(repo_count):
            if (repo_index + ai_index) % 3 != 0:
                adjacency[node, repo_index] = 0.6
                adjacency[repo_index, node] = 0.6
        for other in range(node + 1, total):
            if (ai_index + other) % 5 == 0:
                adjacency[node, other] = 0.45
                adjacency[other, node] = 0.45
    return adjacency


def coherence_metrics(adjacency: np.ndarray) -> dict[str, float]:
    weights = adjacency[adjacency > 0]
    mean_weight = float(np.mean(weights)) if weights.size else 0.0
    density = float(np.count_nonzero(adjacency) / max(adjacency.size - len(adjacency), 1))
    spectral_radius = float(np.max(np.abs(np.linalg.eigvals(adjacency)))) if adjacency.size else 0.0
    normalized_radius = spectral_radius / max(adjacency.shape[0], 1)
    return {
        "mean_weight": mean_weight,
        "density": density,
        "normalized_spectral_radius": normalized_radius,
        "coherence_score": float((mean_weight + density + normalized_radius) / 3.0),
    }


def run_simulation() -> dict[str, object]:
    adjacency = build_adjacency()
    return {
        "mode": "simulation",
        "evidence_status": "architecture_coherence",
        "node_count": int(adjacency.shape[0]),
        "metrics": coherence_metrics(adjacency),
    }


def run_hardware_derived(calibration_path: str | None) -> dict[str, object]:
    calibration = load_calibration(calibration_path)
    params = extract_noise_parameters(calibration)
    adjacency = build_adjacency()
    damping = min(0.35, params["mean_gate_error"] * 20.0 + params["mean_cross_talk"] * 4.0 + params["mean_readout_error"])
    damped = adjacency * (1.0 - damping)
    return {
        "mode": "hardware-derived",
        "evidence_status": "hardware_derived_model",
        "node_count": int(damped.shape[0]),
        "noise_parameters": params,
        "metrics": coherence_metrics(damped),
    }


def main() -> dict[str, object]:
    parser = argparse.ArgumentParser(description="Run bounded lattice coherence analysis.")
    parser.add_argument("--mode", choices=["simulation", "hardware-derived"], default="simulation")
    parser.add_argument("--calibration")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--output")
    args = parser.parse_args()

    result = run_simulation() if args.mode == "simulation" else run_hardware_derived(args.calibration)
    result["schema_version"] = "rfl.self_validating_lattice.v2"
    result["next_step"] = "Correlate graph-level outputs with cross-repo or cross-session artifacts before treating the score as external evidence."

    if args.output:
        output_path = Path(args.output).resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(result, indent=2), encoding="utf-8")

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"mode={result['mode']}")
        print(f"coherence_score={result['metrics']['coherence_score']:.4f}")

    return result


if __name__ == "__main__":
    main()
