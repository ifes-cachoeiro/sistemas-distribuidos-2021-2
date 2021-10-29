import socket
import _thread

HOST = ""  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta
LISTA_P = []


def receber(conn, client):
    while True:
        msg = conn.recv(1024)
        if not msg:
            break
        msg_decoded = msg.decode('utf-8')
        for p in LISTA_P:
            if p['cliente'] != client:
                p['lista_mensagens'].append(msg_decoded)

def enviar(conn, client):
    print(f"Connected by {client}")
    while True:
        # Sending confirmation to the client
        for p in LISTA_P:
            if p['cliente'] == client:
                if len(p['lista_mensagens']) > 0:
                    msg = p['lista_mensagens'].pop(0)
                    conn.send(msg.encode('utf-8'))


def server():
    print(f"Starting TCP Server on port {PORT}")
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (HOST, PORT)
    tcp.bind(orig)
    tcp.listen(1)

    while True:
        conn, client = tcp.accept()
        LISTA_P.append(
            {
                "cliente": client,
                "lista_mensagens": []
            }
        )
        _thread.start_new_thread(enviar, (conn, client))
        _thread.start_new_thread(receber, (conn, client))

if __name__ == "__main__":
    server()
