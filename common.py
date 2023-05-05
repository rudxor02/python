import socket
import struct
from typing import Tuple
from enum import Enum

class MessageType(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


LENGTH_BYTES = 8
MESSAGE_TYPE_BYTES = 4

def bind_port(client: socket.socket, host: str, port_start: int, port_range: int) -> bool:
    for port in range(port_start, port_start + port_range):
        try:
            client.bind((host, port))
            return True
        except socket.error:
            pass
    return False

def get_message_length(conn: socket.socket) -> int:
    length_data = conn.recv(LENGTH_BYTES)
    return struct.unpack('>Q', length_data)[0]
    
def get_message_type(conn:socket.socket) -> MessageType:
    message_type_data = conn.recv(MESSAGE_TYPE_BYTES)
    return MessageType((struct.unpack('>I', message_type_data))[0])

def get_message_body(conn:socket.socket, message_length: int) -> str:
    message_body_data = conn.recv(message_length)
    return message_body_data.decode()

def decode_data(conn: socket.socket) -> Tuple[MessageType, str]:
    message_length = get_message_length(conn)
    message_type = get_message_type(conn)
    message_body = get_message_body(conn, message_length)
    return (message_type, message_body)

def construct_message(message_type: MessageType, message_body: str) -> bytes:
    message_type_data = struct.pack('>I', message_type.value)
    message_body_data = message_body.encode()
    message_length_data = struct.pack('>Q', len(message_body_data))
    return message_length_data + message_type_data + message_body_data