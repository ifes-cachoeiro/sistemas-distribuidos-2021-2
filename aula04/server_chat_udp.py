import socket
import sys
import _thread

HOST = sys.argv[1]  # Endereco IP do S
PORT = 5000  # Porta que o Servidor esta
NOME_USUARIO = sys.argv[2]


def server(udp):
    print(f"Starting UDP Server on port {PORT}")
    while True:
        msg, cliente = udp.recvfrom(1024)
        msg_decoded = msg.decode('utf-8')
        print(f"{cliente} {msg_decoded}")


def client():
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    orig = ("", PORT)
    dest = (HOST, PORT)
    udp.bind(orig)
    _thread.start_new_thread(server, (udp,))
    print("Type q to exit")
    message = None
    while message != "q":
        if sys.version_info.major == 3:
            message = input("-> ")
        else:
            message = raw_input("-> ")
        udp.sendto(message.encode("utf-8"), dest)
        # data = udp.recv(1024).decode("utf-8")
        # print("Received from server: " + data)
    udp.close()


if __name__ == "__main__":
    client()
