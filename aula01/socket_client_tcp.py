import socket
import sys

HOST = "127.0.0.1"  # Endereco IP do S
PORT = 5000  # Porta que o Servidor esta


def client():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)
    print("Type q to exit")
    message = None
    tcp.connect(dest)
    while message != "q":
        if sys.version_info.major == 3:
            message = input("-> ")
        else:
            message = raw_input("-> ")
        tcp.send(message.encode('utf-8'))
        # Receiving confirmation from the server
        data = tcp.recv(1024).decode("utf-8")
        print("Received from server: " + data)
    tcp.close()


if __name__ == "__main__":
    client()
