import zmq
import sys

IP_ADDRESS = "127.0.0.1"
TOPIC = "NEWS"

ctx = zmq.Context()
sock = ctx.socket(zmq.SUB)
sock.connect(f"tcp://{IP_ADDRESS}:5501")
sock.subscribe(f"{TOPIC}")

print(f"Starting receiver from topic(s) {TOPIC}...")
while True:
    msg_string = sock.recv_string()
    msg_json = sock.recv_json()
    print(f"Received json message {msg_json} from topic {msg_string}.")

sock.close()
ctx.term()
