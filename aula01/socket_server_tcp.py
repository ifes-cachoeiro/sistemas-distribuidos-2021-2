import socket

HOST = ""  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta


def server():
    print(f"Starting TCP Server on port {PORT}")
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (HOST, PORT)
    tcp.bind(orig)
    tcp.listen(1)

    while True:
        conn, client = tcp.accept()
        print(f"Connected by {client}")
        while True:
            msg = conn.recv(1024)
            if not msg:
                break
            msg_decoded = msg.decode('utf-8')
            print(f"{client} {msg_decoded}")
            # Sending confirmation to the client
            conn.send("ok".encode('utf-8'))

        print(f"Connection ended by {client}")
        conn.close()


if __name__ == "__main__":
    server()
