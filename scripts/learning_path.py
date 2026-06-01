"""Print the recommended VR Engineering 101 learning path."""

from __future__ import annotations


STEPS = [
    ("01", "Donanim ve Sensor", "IMU filtre lab'ini calistir, drift notu yaz."),
    ("02", "Edge-AI ve Performans", "Latency butcesini degistir, 20 ms altini hedefle."),
    ("03", "Matematik ve Pipeline", "Quaternion carpim siralarini karsilastir."),
    ("04", "Ag ve Guvenlik", "Snapshot paketini bozup imza kontrolunu test et."),
]


def main() -> None:
    print("VR Engineering 101 learning path")
    for code, title, task in STEPS:
        print(f"{code}. {title}: {task}")


if __name__ == "__main__":
    main()
