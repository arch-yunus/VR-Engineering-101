"""Quaternion playground for basic VR orientation math."""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Quaternion:
    w: float
    x: float
    y: float
    z: float

    def normalized(self) -> "Quaternion":
        length = math.sqrt(self.w**2 + self.x**2 + self.y**2 + self.z**2)
        return Quaternion(self.w / length, self.x / length, self.y / length, self.z / length)

    def __mul__(self, other: "Quaternion") -> "Quaternion":
        return Quaternion(
            self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z,
            self.w * other.x + self.x * other.w + self.y * other.z - self.z * other.y,
            self.w * other.y - self.x * other.z + self.y * other.w + self.z * other.x,
            self.w * other.z + self.x * other.y - self.y * other.x + self.z * other.w,
        )


def from_axis_angle(axis: tuple[float, float, float], degrees: float) -> Quaternion:
    radians = math.radians(degrees)
    half = radians / 2.0
    scale = math.sin(half)
    x, y, z = axis
    return Quaternion(math.cos(half), x * scale, y * scale, z * scale).normalized()


def main() -> None:
    yaw = from_axis_angle((0.0, 1.0, 0.0), 30.0)
    pitch = from_axis_angle((1.0, 0.0, 0.0), 12.0)
    orientation = (yaw * pitch).normalized()
    print("Quaternion orientation after yaw then pitch")
    print(f"w={orientation.w:.4f} x={orientation.x:.4f} y={orientation.y:.4f} z={orientation.z:.4f}")


if __name__ == "__main__":
    main()
