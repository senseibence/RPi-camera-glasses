from picamera2 import Picamera2
from gpiozero import Button
from time import sleep
import openai

camera = Picamera2()

config = camera.create_still_configuration(raw={"size": camera.sensor_resolution})
camera.configure(config)

camera.start()
sleep(5)

# image = camera.capture_image() // for API
camera.capture_file("/home/bence/image.png")

camera.close()