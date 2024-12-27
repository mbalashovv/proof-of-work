import hashlib
import string
import random

from typing import TypeVar


__all__ = (
    "generate_challenge",
    "solve_challenge",
    "check_challenge",
)


Challenge = TypeVar("Challenge", bound=str)
Nonce = TypeVar("Nonce", str, int)


def solve_challenge(raw_challenge: Challenge) -> Nonce:
    challenge, difficulty = raw_challenge.split(":")
    nonce = 0
    while not hashlib.sha256(f"{challenge}{nonce}".encode()).hexdigest().startswith("0" * int(difficulty)):
        nonce += 1
    return nonce


def generate_challenge(difficulty: int) -> Challenge:
    seed = "".join(random.sample(string.ascii_letters, 40))
    return f"{seed}:{difficulty}"


def check_challenge(raw_challenge: Challenge, nonce: Nonce) -> bool:
    challenge, difficulty = raw_challenge.split(":")
    return hashlib.sha256(f"{challenge}{nonce}".encode()).hexdigest().startswith("0" * int(difficulty))
