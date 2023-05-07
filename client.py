import socket
import common

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


port_start = 8000
port_range = 10

# client.bind(("localhost", 8001))
# client.listen()
# client.accept()

if common.bind_port(client, "localhost", port_start, port_range) == False:
    raise Exception()

client.connect(("localhost", 8000))

message = "hey"

client.send(common.construct_message(common.MessageType.BLUE, message))

client.close()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if common.bind_port(client, "localhost", port_start, port_range) == False:
    raise Exception()

client.connect(("localhost", 8000))

client.send(common.construct_message(common.MessageType.BLUE, "asdkjaskjnd"))

client.close()
