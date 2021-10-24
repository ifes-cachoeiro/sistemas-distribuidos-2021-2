import socket

PORT = 5000  # Porta que o Servidor esta


def server(udp):
    listaUsuarios = []
    print(f"Starting UDP Server on port {PORT}")
    while True:
        msg, cliente = udp.recvfrom(1024)
        msg_decoded = msg.decode("utf-8")
        if msg_decoded.split(",")[0] == "conectar":
            novo_usuario = {
                "nome": msg_decoded.split(",")[1],
                "cliente": cliente,
            }
            listaUsuarios.append(novo_usuario)
        elif msg_decoded.split(",")[0] == "enviarMensagem":
            usuario = msg_decoded.split(",")[1]
            mensagem = msg_decoded.split(",")[2]
            msg_to_send = f"{usuario},{mensagem}"
            for u in listaUsuarios:
                udp.sendto(msg_to_send.encode("utf-8"), u["cliente"])


def main():
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    orig = ("", PORT)
    udp.bind(orig)
    server(udp)


if __name__ == "__main__":
    main()
