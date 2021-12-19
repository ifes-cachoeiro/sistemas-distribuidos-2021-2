import zmq


def main():

    try:
        ctx = zmq.Context(1)
        # Socket facing clients
        frontend = ctx.socket(zmq.SUB)
        frontend.bind("tcp://*:5500")
        frontend.subscribe("")

        # Socket facing services
        backend = ctx.socket(zmq.PUB)
        backend.bind("tcp://*:5501")

        zmq.device(zmq.FORWARDER, frontend, backend)
    except Exception as e:
        print(f"bringing down zmq device: error -> {e}")
    finally:
        frontend.close()
        backend.close()
        ctx.term()


if __name__ == "__main__":
    main()
