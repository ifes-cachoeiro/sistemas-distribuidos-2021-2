import zmq
import time
import sys

IP_ADDRESS = None
TOPIC = None

if len(sys.argv) == 3:
    IP_ADDRESS = sys.argv[1]
    TOPIC = sys.argv[2]
else:
    print("Usage: python3 pub.py <IP_ADDRESS> <TOPIC>")
    sys.exit(0)

ctx = zmq.Context()
sock = ctx.socket(zmq.PUB)
sock.connect(f"tcp://{IP_ADDRESS}:5500")

print(f"Starting publishing to the topic {TOPIC}...")
i = 1
while True:
    msg = f"Hi for the {i}:th time..."
    sock.send_string(f"{TOPIC}", flags=zmq.SNDMORE)
    sock.send_json({"msg": msg})
    print(f"Sent json: {msg} ...")
    i += 1
    time.sleep(1)

sock.close()
ctx.term()
