from picamera2 import Picamera2
from gpiozero import Button
from time import sleep
import openai
import json

with open('keys.json','r') as file:
    key = json.load(file)

openai.api_key = key['OpenAI_API_Key']

camera = Picamera2()
config = camera.create_still_configuration(raw={"size": camera.sensor_resolution})
camera.configure(config)

button = Button(25) # GPIO25

def take_picture():
    camera.start()
    sleep(3)

    image = camera.capture_image() # returns a PIL image
    # camera.capture_file('image.jpg') --> can open file in binary and send to OpenAI, if easier

    camera.stop() # could be camera.close(), I have no idea
    return image

# POST request
def send_picture():

    # Waiting for image upload feature
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": "Tell me a short joke"}
        ]
    )

    return completion.choices[0].message['content']

while True:
    try:
        button.wait_for_press()
        image = take_picture()
        response = send_picture(image)
        print(response)
        sleep(10) # rudimentary way to avoid multiple captures for a single press
    except KeyboardInterrupt:
        pass
    finally:
        camera.stop()
        break