import zmq

def request_random_image(category=None, width=640, height=480):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    request_data = {
        'category': category,
        'width': width,
        'height': height
    }
    socket.send_json(request_data)

    image_url = socket.recv_string()
    return image_url


if __name__ == "__main__":
    print(request_random_image('nature', 800, 600))
