# Proof of Work TCP Server & Client

To run the server, use command:
```shell
make server_up
```

To run client:
```shell
make client_up
```

To watch logs in both services:
```shell
make logs
```

To run tests:
```shell
make tests
```

Find more commands in Makefile.

---

In attached mode signals might not be handled, that's why you'd better use detached mode and use docker logs.