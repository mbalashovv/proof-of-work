import unittest
import hashlib
from src.internal.hashing import generate_challenge, solve_challenge, check_challenge


class TestHashingFunctions(unittest.TestCase):
    def test_generate_challenge(self):
        challenge = generate_challenge(4)
        self.assertIsInstance(challenge, str, "Challenge should be a string")
        self.assertIn(":", challenge, "Challenge format should be 'seed:difficulty'")
        seed, difficulty = challenge.split(":")
        self.assertTrue(seed.isalpha(), "Seed should only contain letters")
        self.assertTrue(difficulty.isdigit(), "Difficulty should be a number")
        self.assertEqual(int(difficulty), 4, "Generated difficulty should match input")

    def test_solve_challenge(self):
        raw_challenge = "abcdef:3"
        nonce = solve_challenge(raw_challenge)
        self.assertIsInstance(nonce, int, "Nonce should be an integer")
        self.assertTrue(
            hashlib.sha256(f"abcdef{nonce}".encode()).hexdigest().startswith("000"),
            "Solved nonce should produce a hash with the correct difficulty"
        )

    def test_check_challenge_valid_nonce(self):
        raw_challenge = "abcdef:3"
        valid_nonce = solve_challenge(raw_challenge)
        is_valid = check_challenge(raw_challenge, valid_nonce)
        self.assertTrue(is_valid, "check_challenge should return True for a valid nonce")

    def test_check_challenge_invalid_nonce(self):
        raw_challenge = "abcdef:3"
        invalid_nonce = 123456  # Arbitrary invalid nonce
        is_valid = check_challenge(raw_challenge, invalid_nonce)
        self.assertFalse(is_valid, "check_challenge should return False for an invalid nonce")

    def test_integration_generate_solve_check(self):
        difficulty = 2
        challenge = generate_challenge(difficulty)
        nonce = solve_challenge(challenge)
        is_valid = check_challenge(challenge, nonce)
        self.assertTrue(
            is_valid,
            "Integration test should pass for a generated challenge and its solved nonce"
        )


if __name__ == "__main__":
    unittest.main()
