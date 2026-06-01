"""Repository structure checks for VR Engineering 101."""

from __future__ import annotations

from pathlib import Path


REQUIRED_PATHS = [
    "README.md",
    "CONTRIBUTING.md",
    "PROJECTS.md",
    "LICENSE",
    "01_donanim_sensor/README.md",
    "01_donanim_sensor/labs/imu_complementary_filter.py",
    "02_edge_ai_performans/README.md",
    "02_edge_ai_performans/labs/latency_budget.py",
    "02_edge_ai_performans/labs/foveated_tile_planner.py",
    "03_yazilim_matematik_pipeline/README.md",
    "03_yazilim_matematik_pipeline/labs/quaternion_playground.py",
    "04_ag_guvenlik/README.md",
    "04_ag_guvenlik/labs/udp_snapshot_packet.py",
    "docs/glossary.md",
    "docs/quality_gates.md",
    "docs/roadmap.md",
    "docs/system_architecture.md",
    "docs/threat_model_template.md",
    ".github/workflows/validate.yml",
    "scripts/learning_path.py",
]


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    missing = [path for path in REQUIRED_PATHS if not (root / path).exists()]
    if missing:
        print("Missing required paths:")
        for path in missing:
            print(f"- {path}")
        raise SystemExit(1)
    print(f"OK: {len(REQUIRED_PATHS)} required paths found.")


if __name__ == "__main__":
    main()
