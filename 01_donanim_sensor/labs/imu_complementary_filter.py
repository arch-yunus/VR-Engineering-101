"""Tiny complementary-filter demo for synthetic VR headset roll data."""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class ImuSample:
    dt: float
    gyro_roll_rate_dps: float
    accel_y: float
    accel_z: float


def accel_roll_degrees(accel_y: float, accel_z: float) -> float:
    return math.degrees(math.atan2(accel_y, accel_z))


def estimate_roll(samples: list[ImuSample], alpha: float = 0.96) -> list[float]:
    roll = 0.0
    estimates: list[float] = []
    for sample in samples:
        gyro_roll = roll + sample.gyro_roll_rate_dps * sample.dt
        accel_roll = accel_roll_degrees(sample.accel_y, sample.accel_z)
        roll = alpha * gyro_roll + (1.0 - alpha) * accel_roll
        estimates.append(roll)
    return estimates


def synthetic_samples() -> list[ImuSample]:
    samples: list[ImuSample] = []
    dt = 0.01
    bias_dps = 0.8
    last_angle = 0.0
    for i in range(240):
        t = i * dt
        true_angle = 18.0 * math.sin(2.0 * math.pi * 0.45 * t)
        rate = (true_angle - last_angle) / dt
        last_angle = true_angle

        radians = math.radians(true_angle)
        accel_y = math.sin(radians)
        accel_z = math.cos(radians)
        samples.append(ImuSample(dt, rate + bias_dps, accel_y, accel_z))
    return samples


def main() -> None:
    samples = synthetic_samples()
    estimates = estimate_roll(samples)
    print("Complementary filter demo")
    print(f"samples={len(samples)} final_roll_deg={estimates[-1]:.2f}")
    print("first_5_estimates=", ", ".join(f"{value:.2f}" for value in estimates[:5]))


if __name__ == "__main__":
    main()
