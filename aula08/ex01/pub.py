import zmq
import time
import sys

TOPIC = None

if len(sys.argv) == 2:
    TOPIC = sys.argv[1]
else:
    print("Usage: python3 pub.py <TOPIC>")
    sys.exit(0)

ctx = zmq.Context()
sock = ctx.socket(zmq.PUB)
sock.bind("tcp://*:5500")

print(f"Starting publshing to the topic {TOPIC}...")
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
