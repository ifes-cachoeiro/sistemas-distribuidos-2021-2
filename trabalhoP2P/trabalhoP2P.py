import random
import socket
import sys
import _thread

PORT = 12345

node = {
    "id": None,
    "ip": sys.argv[1],
    "id_antecessor": None,
    "ip_antecessor": None,
    "id_sucessor": None,
    "ip_sucessor": None
}

def cliente(udp):
    pass

def servidor(udp):
    pass

def main():
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind(("", PORT))
    opc = None
    while opc != "6":
        informacoes_do_no = f"""
                       ID: {node['id']}
            ID_ANTECESSOR: {node['id_antecessor']}
            IP_ANTECESSOR: {node['ip_antecessor']}
              ID_SUCESSOR: {node['id_sucessor']}
              IP_SUCESSOR: {node['ip_sucessor']}
        """
        print(informacoes_do_no)
        print("######################################")
        print("# 1 - Gerar nodeID ")
        print("# 2 - Iniciar rede P2P (no inicial)")
        print("# 3 - Entrar em uma rede P2P ")
        print("# 4 - Sair da rede P2P")
        print("# 5 - Mostrar informacoes do No")
        print("# 6 - Sair da aplicacao")
        print("#####################################")
        opc = input("Informe uma opcao: ")
        if opc == "1":
            node['id'] = random.randrange(1, 1000)
        elif opc == "2":
            node['id_antecessor'] = node['id']
            node['id_sucessor'] = node['id']
            node['ip_antecessor'] = node['ip']
            node['ip_sucessor'] = node['ip']
        elif opc == "3":
            endereco_lookup = input("informe o endereco IP")
            print(endereco_lookup)
        elif opc == "5":
            continue

if __name__ == "__main__":
    main()