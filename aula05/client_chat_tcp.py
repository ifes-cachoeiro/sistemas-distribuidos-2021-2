import socket
import sys
import _thread
import json

HOST = sys.argv[1]  # Endereco IP do S
PORT = 5000  # Porta que o Servidor esta
NOME_USUARIO = sys.argv[2]
FILA_MENSAGENS = []


def receber_mensagem(tcp):
    while True:
        # Receiving confirmation from the server
        data = tcp.recv(1024).decode("utf-8")
        data_converted = json.loads(data)
        usuario = data_converted['usuario']
        mensagem = data_converted['mensagem']
        print(f"<- {usuario} {mensagem}")


def enviar_mensagem(tcp):
    while True:
        if len(FILA_MENSAGENS) > 0:
            mensagem = {}
            mensagem['acao'] = 'enviarMensagem'
            mensagem['usuario'] = NOME_USUARIO
            mensagem['mensagem'] = FILA_MENSAGENS.pop(0)
            msg_json = json.dumps(mensagem)
            tcp.send(msg_json.encode('utf-8'))

def client():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)
    print("Type q to exit")
    message = None
    try:
        tcp.connect(dest)
        _thread.start_new_thread(enviar_mensagem, (tcp,))
        _thread.start_new_thread(receber_mensagem, (tcp,))
        while message != "q":
            if sys.version_info.major == 3:
                message = input("-> ")
            else:
                message = raw_input("-> ")
            FILA_MENSAGENS.append(message)
    except Exception as ex:
        print(f"Erro de conexao...{ex}")
    tcp.close()


if __name__ == "__main__":
    client()
