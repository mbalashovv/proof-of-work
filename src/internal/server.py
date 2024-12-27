from src.internal.hashing import generate_challenge, check_challenge
from src.config import Config
from src.logger import get_logger

__all__ = (
    "handle_connection",
)

logger = get_logger(__name__)


def handle_connection(client_socket, client_address):
    logger.info("New connection from %s", client_address)

    # Generating a challenge
    challenge = generate_challenge(Config.POW_DIFFICULTY)

    logger.info("Generated a challenge: %s", challenge)
    client_socket.sendall(challenge.encode("utf-8"))

    with client_socket:
        while True:
            result = client_socket.recv(1024)
            if not result:
                break  # Exit if no data
            logger.info("Received a result from %s: %s", client_address, result.decode())

            # Checking the result
            is_passed = check_challenge(challenge, result.decode())
            logger.info("Is the challenge passed: %s", is_passed)

            # Sending back to the client whether the answer was correct
            client_socket.sendall(str(int(is_passed)).encode("utf-8"))