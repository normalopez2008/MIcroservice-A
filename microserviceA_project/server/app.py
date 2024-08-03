import zmq
import requests
import os

API_KEY = 'YOUR_API_KEY_HERE'
API_URL = 'https://api.api-ninjas.com/v1/randomimage'

def generate_random_image_url(category=None, width=640, height=480):
    params = {}
    if category:
        params['category'] = category
    if width:
        params['width'] = width
    if height:
        params['height'] = height
    
    response = requests.get(API_URL, headers={'X-Api-Key': API_KEY, 'Accept': 'image/jpg'}, params=params, stream=True)
    
    if response.status_code == requests.codes.ok:
        file_name = 'random_image.jpg'
        with open(file_name, 'wb') as out_file:
            out_file.write(response.content)
        return os.path.abspath(file_name)
    else:
        return f"Error: {response.status_code}, {response.text}"

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    
    while True:
        message = socket.recv_json()
        category = message.get('category')
        width = message.get('width')
        height = message.get('height')
        image_url = generate_random_image_url(category, width, height)
        socket.send_string(image_url)

if __name__ == "__main__":
    main()
