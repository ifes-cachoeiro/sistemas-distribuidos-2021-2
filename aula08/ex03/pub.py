import zmq
import time
import sys

IP_ADDRESS = "127.0.0.1"
TOPIC = "NEWS"

news = [
    {"titulo": "Linux 5.16", "noticia": "Versão estável do Linux 5.16"},
    {"titulo": "Linux M1", "noticia": "Linux está 'usável como desktop' nos Macs M1"},
    {"titulo": "Google Chrome", "noticia": "Google Chrome ficará mais rápido no Windows"},
    {"titulo": "Linux Shell", "noticia": "Como criar um link simbólico para um diretório no Linux"},
]

ctx = zmq.Context()
sock = ctx.socket(zmq.PUB)
sock.connect(f"tcp://{IP_ADDRESS}:5500")

print(f"Starting publishing to the topic {TOPIC}...")

while True:
    for msg in news:
        time.sleep(5)
        sock.send_string(f"{TOPIC}", flags=zmq.SNDMORE)
        sock.send_json({"msg": msg})
        print(f"Mensagem enviada: {msg} ...")

sock.close()
ctx.term()
