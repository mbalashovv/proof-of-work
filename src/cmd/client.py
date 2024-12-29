import socket
import os
import time
import signal

from src.internal.hashing import solve_challenge
from src.config import Config
from src.logger import get_logger


logger = get_logger(__name__)

# Variables for metrics
total_requests_sent = 0
total_response_time = 0
error_count = 0


def send_request():
    """Connects to server, receives a challenge, solves it and then checks the result."""

    start_time = time.monotonic()

    # Connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((Config.SERVER_HOST, Config.SERVER_PORT))
    logger.info("Connected to server at %s:%s", Config.SERVER_HOST, Config.SERVER_PORT)

    increment_request_count()

    # Receive a challenge from the server
    challenge = client_socket.recv(1024)
    logger.info("Challenge was received: %s", challenge.decode("utf-8"))

    # Solve the challenge
    nonce = solve_challenge(challenge.decode("utf-8"))

    # Send the result of the challenge back to the server
    client_socket.sendall(str(nonce).encode("utf-8"))

    # Receive 1 or 0 whether the result was successful or not
    result = bool(client_socket.recv(1024).decode("utf-8"))
    logger.info("The result was %s", result)

    if not result:
        increment_errors_count()

    logger.info(Config.DELIMITER)

    collect_response_time_metric(time.monotonic() - start_time)

    client_socket.close()


def collect_response_time_metric(time_: float) -> None:
    global total_response_time
    total_response_time += time_


def increment_request_count() -> None:
    global total_requests_sent
    total_requests_sent += 1


def increment_errors_count() -> None:
    global error_count
    error_count += 1


def show_metrics() -> None:
    average_response_time = 0

    if total_requests_sent > 0:
        average_response_time = total_response_time / total_requests_sent

    logger.info("%s", Config.DELIMITER)
    logger.info("Total requests sent: %s", total_requests_sent)
    logger.info("Average response time: %s", average_response_time)
    logger.info("Error count: %s", error_count)
    logger.info("%s", Config.DELIMITER)

    os._exit(0)  # Exits silently without raising SystemExit error like sys.exit()


def signal_handler(signal_received, *_) -> None:
    logger.debug("Signal received: %s", signal_received)
    show_metrics()


# Handle SIGINT and SIGTERM gracefully
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)


def main():
    logger.info(Config.DELIMITER)
    try:
        while True:
            send_request()
    except BaseException as e:
        logger.exception("An exception occurred: %s", e)
    finally:
        show_metrics()


if __name__ == "__main__":
    main()
