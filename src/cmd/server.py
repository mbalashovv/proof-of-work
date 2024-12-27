import socket

from src.config import Config
from src.internal.server import handle_connection


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind(("0.0.0.0", Config.SERVER_PORT))
    tcp_socket.listen(1)

    try:
        while True:
            conn, addr = tcp_socket.accept()
            handle_connection(conn, addr)
    finally:
        tcp_socket.close()


if __name__ == "__main__":
    main()
