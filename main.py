from picamera2 import Picamera2
from gpiozero import Button
from time import sleep
import json
from bardapi import Bard
# import openai

with open('keys.json','r') as file:
    key = json.load(file)

# openai_key = key['OpenAI_API_Key']
bard_key = key['Bard_Cookie_Value']

# openai.api_key = openai_key
bard = Bard(token=bard_key)

camera = Picamera2()
config = camera.create_still_configuration(raw={"size": camera.sensor_resolution})
camera.configure(config)

button = Button(25)

def take_picture():
    camera.start()
    sleep(3)
    camera.capture_file('image.jpg')
    camera.stop()

def send_picture(image):
    
    # OpenAI API Request
    
    '''
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": "Who are you?"}
        ]
    )

    return completion.choices[0].message['content']
    '''
    
    # Unofficial Google Bard API Request
    
    bard_answer = bard.ask_about_image('Describe the contents of this image', image)
    return bard_answer['content']

while True:
    try:
        button.wait_for_press()
        take_picture()
        sleep(1)
        image = open('image.jpg', 'rb').read()
        response = send_picture(image)
        print(response)
    except:
        camera.stop()
        break
