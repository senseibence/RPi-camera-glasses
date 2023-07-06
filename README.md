# RPi-camera-glasses
This project was prompted by GPT-4's visual input feature, which allows image upload and analysis: https://openai.com/product/gpt-4. I will be attaching a Raspberry Pi camera module onto my glasses, capturing images with a button wired to the Pi, and sending those images via an API request to the GPT-4 model (once that feature is available).

# Materials
* Raspberry Pi 4 Model B
* Raspberry Pi Camera Module V3
* [Miuzei case](https://www.amazon.com/gp/product/B07VX2WDHM/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
* [Momentary push button](https://www.amazon.com/gp/product/B07WF76VHT/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&th=1) (I recommend getting a bigger one than this)
* [Arducam camera module extension cable](https://www.amazon.com/gp/product/B07SM6JTTM/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
* [Arducam camera extension cable](https://www.arducam.com/product/200mm-sensor-extension-cable-for-raspberry-pi-v2-v3-support-working-on-raspberry-pi-and-jetson-nano/)
* [Dupont wires](https://www.amazon.com/gp/product/B01EV70C78/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&th=1)
* Soldering iron (depending on push button)
* Glasses 

# Installation
1. Assemble the hardware. The camera extension cable should be wired to the camera module, the camera module should be attached to the Pi's CSI port, and the push button should be wired to any GPIO pin and ground.
2. Install the recommended Raspberry Pi OS on a microSD card: https://www.raspberrypi.com/software/
3. Boot up Raspberry Pi and open a CLI
4. Clone repository: ```git clone https://github.com/senseibence/RPi-camera-glasses.git```
5. Change directory: ```cd RPi-camera-glasses```
6. Install packages: all packages used except for 1 (openai) are included in the recommended Raspberry Pi OS (Bullseye). If you still wish to install them manually, run ```pip install -r requirements.txt```. Otherwise, run ```pip install openai``` to install the OpenAI API package. Using a virtual environment is recommended.
7. Set the value of ```OpenAI_API_Key``` in ```keys.json``` with your own API key. You can create one here: https://platform.openai.com/account/api-keys
8. Run ```python main.py``` to start the program

# Images
![image](https://cdn.discordapp.com/attachments/953870034227302470/1110371329825321102/IMG_1627.jpg)
Rough diagram of the project

![image](https://cdn.discordapp.com/attachments/953870034227302470/1110371318123208866/IMG_1615.jpg)
Raspberry Pi 4 Model B before hardware installations

![image](https://cdn.discordapp.com/attachments/953870034227302470/1110371329187774556/IMG_1625.jpg)
Raspberry Pi 4 Model B after hardware installations

![image](https://cdn.discordapp.com/attachments/953870034227302470/1110371333746995292/IMG_1626.jpg)
Glasses with camera and module
