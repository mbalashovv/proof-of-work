import hashlib
import string
import random


__all__ = (
    "generate_challenge",
    "solve_challenge",
    "check_challenge",
)


def solve_challenge(raw_challenge: str) -> int:
    challenge, difficulty = raw_challenge.split(":")
    nonce = 0
    while not hashlib.sha256(f"{challenge}{nonce}".encode("utf-8")).hexdigest().startswith("0" * int(difficulty)):
        nonce += 1
    return nonce


def generate_challenge(difficulty: int) -> str:
    seed = "".join(random.sample(string.ascii_letters, 40))
    return f"{seed}:{difficulty}"


def check_challenge(raw_challenge: str, nonce: int) -> bool:
    challenge, difficulty = raw_challenge.split(":")
    return hashlib.sha256(f"{challenge}{nonce}".encode("utf-8")).hexdigest().startswith("0" * int(difficulty))
