"""Pack and unpack a tiny VR avatar snapshot packet."""

from __future__ import annotations

import hmac
import struct
from hashlib import sha256


PACKET = struct.Struct("!Iffff")
SECRET = b"dev-secret-change-me"


def encode(sequence: int, x: float, y: float, z: float, yaw: float) -> bytes:
    body = PACKET.pack(sequence, x, y, z, yaw)
    signature = hmac.new(SECRET, body, sha256).digest()[:8]
    return body + signature


def decode(packet: bytes) -> tuple[int, float, float, float, float]:
    body, signature = packet[:-8], packet[-8:]
    expected = hmac.new(SECRET, body, sha256).digest()[:8]
    if not hmac.compare_digest(signature, expected):
        raise ValueError("packet signature mismatch")
    return PACKET.unpack(body)


def main() -> None:
    packet = encode(sequence=42, x=1.0, y=1.7, z=-0.2, yaw=85.0)
    sequence, x, y, z, yaw = decode(packet)
    print("UDP snapshot packet")
    print(f"bytes={len(packet)} sequence={sequence} pos=({x:.1f},{y:.1f},{z:.1f}) yaw={yaw:.1f}")


if __name__ == "__main__":
    main()
