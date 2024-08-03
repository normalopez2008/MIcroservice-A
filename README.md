# MIcroservice-A
Software engineering microservice for teammate

Random Image Microservice

This microservice generates random images for playlist covers using the [API Ninjas Random Image API](https://api-ninjas.com/api/randomimage) and communicates with clients via ZeroMQ.

What I Have Done

Implemented a server script that:
  - Listens for requests via ZeroMQ.
  - Fetches random images from the API Ninjas service.
  - Returns the URL of the generated image.
  
Developed a client script that:
  - Sends requests to the microservice.
  - Receives the image URL.
  
How to Use

1. Setup

Install Python Packages and dependencies:
  - Ensure you have Python installed.
  - Install required packages using `requirements.txt`

`pip install -r microservice/requirements.txt`
 

2. Configuration

Add Your API Key:
  - Open `microservice/app.py`.
  - Replace `'YOUR_API_KEY_HERE'` with your actual API key

3. Start the Microservice:
   Terminal 1:
  `python microservice/app.py`
  

4. Send a Request:
   Terminal 2:
  `python client/client.py`

