"""Motion-to-photon latency budget calculator."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Stage:
    name: str
    milliseconds: float


DEFAULT_PIPELINE = [
    Stage("sensor_read", 1.2),
    Stage("pose_prediction", 0.8),
    Stage("simulation", 2.0),
    Stage("render", 6.4),
    Stage("compositor", 1.6),
    Stage("display_scanout", 4.2),
]


def total_latency(stages: list[Stage]) -> float:
    return sum(stage.milliseconds for stage in stages)


def frame_budget(refresh_hz: float) -> float:
    return 1000.0 / refresh_hz


def main() -> None:
    refresh_hz = 90.0
    budget = frame_budget(refresh_hz)
    total = total_latency(DEFAULT_PIPELINE)
    print("Motion-to-photon budget")
    for stage in DEFAULT_PIPELINE:
        print(f"{stage.name:>16}: {stage.milliseconds:4.1f} ms")
    print(f"{'total':>16}: {total:4.1f} ms")
    print(f"{'90hz_frame':>16}: {budget:4.1f} ms")
    print("status:", "ok_under_20ms" if total < 20.0 else "too_slow")


if __name__ == "__main__":
    main()
