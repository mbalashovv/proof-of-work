import socket

from src.internal.server import handle_connection
from src.config import Config
from src.logger import get_logger


logger = get_logger(__name__)


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind(("0.0.0.0", Config.SERVER_PORT))
    tcp_socket.listen(1)

    logger.info("Server was successfully started | POW difficulty: %s", Config.POW_DIFFICULTY)

    try:
        while True:
            conn, addr = tcp_socket.accept()
            handle_connection(conn, addr)
    except KeyboardInterrupt:
        pass
    finally:
        logger.info("Closing socket...")
        tcp_socket.close()


if __name__ == "__main__":
    main()
