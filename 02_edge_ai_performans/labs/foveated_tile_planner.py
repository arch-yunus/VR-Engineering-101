"""Simple foveated-rendering tile quality planner."""

from __future__ import annotations

import math


def quality_for_tile(x: int, y: int, gaze_x: float, gaze_y: float) -> str:
    distance = math.dist((x, y), (gaze_x, gaze_y))
    if distance <= 1.2:
        return "H"
    if distance <= 2.4:
        return "M"
    return "L"


def plan(width: int = 9, height: int = 5, gaze_x: float = 4.0, gaze_y: float = 2.0) -> list[str]:
    rows: list[str] = []
    for y in range(height):
        row = " ".join(quality_for_tile(x, y, gaze_x, gaze_y) for x in range(width))
        rows.append(row)
    return rows


def main() -> None:
    print("Foveated tile plan: H=high, M=medium, L=low")
    for row in plan():
        print(row)


if __name__ == "__main__":
    main()
