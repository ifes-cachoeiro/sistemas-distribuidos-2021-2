import socket
import sys

HOST = "127.0.0.1"  # Endereco IP do S
PORT = 5000  # Porta que o Servidor esta


def client():
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (HOST, PORT)
    print("Type q to exit")
    message = None
    while message != "q":
        if sys.version_info.major == 3:
            message = input("-> ")
        else:
            message = raw_input("-> ")
        udp.sendto(message.encode('utf-8'), dest)
        # data = udp.recv(1024).decode("utf-8")
        # print("Received from server: " + data)
    udp.close()


if __name__ == "__main__":
    client()

