from picamera2 import Picamera2
from gpiozero import Button
from time import sleep
from bardapi import Bard
from gtts import gTTS
import json
import os
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

    # OpenAI API Request (text only)

    '''
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": "Who are you?"}
        ]
    )

    return completion.choices[0].message['content']
    '''

    # Unofficial Google Bard API Request (image capability)

    default_prompt = 'For any image you receive, including this one, you must concisely describe the contents of the image. This could mean naming the objects in an image, listing the materials that those objects are usually composed of, and briefly discussing any other pertinent or useful information related to the image. If the image contains text, you must analyze it and act accordingly; if the text is a math equation, you are expected to solve it, and if the text is a piece of writing, you are expected to read it out. Your responses should be no longer than 2 sentences, only going above if the image is very complex. Again, your job is to concisely describe images and their contents ONLY.'

    bard_answer = bard.ask_about_image(default_prompt, image)
    return bard_answer['content']

while True:
    try:
        button.wait_for_press()
        take_picture()
        sleep(1)
        image = open('image.jpg', 'rb').read()
        response = send_picture(image)
        tts = gTTS(text=response, lang='en', slow=False)
        tts.save("response.mp3")
        os.system("mpg123 response.mp3")
    except:
        camera.stop()
        break