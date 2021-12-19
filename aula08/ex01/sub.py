import zmq
import sys

IP_ADDRESS = None
TOPIC = None

if len(sys.argv) == 3:
    IP_ADDRESS = sys.argv[1]
    TOPIC = sys.argv[2]
else:
    print("Usage: python3 sub.py <IP_ADDRESS> <TOPIC>")
    sys.exit(0)

ctx = zmq.Context()
sock = ctx.socket(zmq.SUB)
sock.connect(f"tcp://{IP_ADDRESS}:5500")
# Subscribe to the topic
sock.subscribe(f"{TOPIC}")

print(f"Starting receiver from topic(s) {TOPIC}...")
while True:
    msg_string = sock.recv_string()
    msg_json = sock.recv_json()
    print(f"Received json message {msg_json} from topic {msg_string}.")

sock.close()
ctx.term()
