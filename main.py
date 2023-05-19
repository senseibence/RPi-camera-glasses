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
    image = camera.capture_image()
    camera.stop() # unsure if this is correct syntax, need to check
    return image

# POST request
def send_picture():
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": "Tell me a short joke"}
        ]
    )

    return completion.choices[0].message['content']

# Main loop, try/except needed to avoid errors
while True:
    if button.is_pressed:
        image = take_picture()
        response = send_picture(image)
        sleep(10)  # avoid multiple captures for a single press