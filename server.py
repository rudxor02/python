import socket
import common

with socket.create_server(("localhost", 8000)) as server:
    while True:
        conn, addr = server.accept()
        print(addr)
        type, body = common.decode_data(conn)
        print(type)
        print(body)
        for i in range(1000000000):
            pass
