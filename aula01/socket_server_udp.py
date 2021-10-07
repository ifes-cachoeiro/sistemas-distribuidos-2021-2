import socket

HOST = ""  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta


def server():
    print(f"Starting UDP Server on port {PORT}")
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    orig = (HOST, PORT)
    udp.bind(orig)
    while True:
        msg, cliente = udp.recvfrom(1024)
        msg_decoded = msg.decode('utf-8')
        print(f"{cliente} {msg_decoded}")
    udp.close()


if __name__ == "__main__":
    server()
