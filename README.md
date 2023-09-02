# RPi-camera-glasses 
This project was prompted by GPT-4's visual input feature, which allows image upload and analysis: https://openai.com/product/gpt-4. Since that feature has not been released as of 7/18/2023, I will be using a custom Google Bard API by Daniel Park: https://github.com/dsdanielpark/Bard-API. I will be attaching a Raspberry Pi camera module onto my glasses, capturing images upon pressing a button wired to the Pi, and sending those images to https://bard.google.com/.

Be mindful that Google may rate limit you if you make excessive requests to the website. 

# Results
![image](https://cdn.discordapp.com/attachments/953870034227302470/1147374000545210448/bottle.jpg)
![image](https://cdn.discordapp.com/attachments/953870034227302470/1147372255194652692/bardgen3.png)
## Bard's description is mostly correct, including correctly identifying the majority of the text present. Color assessment is innacurate

![image](https://cdn.discordapp.com/attachments/953870034227302470/1147374020279406592/wheelbarrow.jpg)
![image](https://cdn.discordapp.com/attachments/953870034227302470/1147372294117793906/bardgen4.png)
## Bard's description is almost perfect, with the only error being the "T" misidentified as "Y"```

# Future Changes
* Implement a USB microphone to create custom prompts for each image (input and output audio together is not simple with Raspberry Pi)
* Implement a more stable API (this will require Google or OpenAI to add image analysis with LLMs to their APIs)
* Make camera glasses more compact and useable in real-world scenarios

# Materials
* Raspberry Pi 4 Model B
* Raspberry Pi Camera Module V3
* [Miuzei case](https://www.amazon.com/gp/product/B07VX2WDHM/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
* [Momentary push button](https://www.amazon.com/gp/product/B07WF76VHT/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&th=1) (I recommend getting a bigger one than this)
* [Arducam camera module extension cable](https://www.amazon.com/gp/product/B07SM6JTTM/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
* [Arducam camera extension cable](https://www.arducam.com/product/200mm-sensor-extension-cable-for-raspberry-pi-v2-v3-support-working-on-raspberry-pi-and-jetson-nano/)
* [Dupont wires](https://www.amazon.com/gp/product/B01EV70C78/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&th=1)
* [Jonkuu Power Bank](https://www.amazon.com/Portable-10000mAh-External-Powerpack-Compatible/dp/B07VGHLRTQ/ref=sr_1_3?hvadid=282500818530&hvdev=c&hvlocphy=9002180&hvnetw=g&hvqmt=e&hvrand=9102774611039822606&hvtargid=kwd-454222816497&hydadcr=19972_9442985&keywords=jonkuu+power+bank&qid=1688676898&sr=8-3)
* Soldering iron (depending on type of push button)

# Installation
1. Assemble the hardware. The camera extension cable should be wired from camera to camera module, the camera module should be attached to the Pi's CSI port, and the push button should be wired to any GPIO pin and ground.
2. Install the recommended Raspberry Pi OS on a microSD card: https://www.raspberrypi.com/software/
3. Boot up Raspberry Pi and open a CLI
4. Clone repository: ```git clone https://github.com/senseibence/RPi-camera-glasses.git```
5. Change directory: ```cd RPi-camera-glasses```
6. Install packages: 
* All packages except for 3 (openai (unused), bardapi, and gTTS) are included in the recommended Raspberry Pi OS (Bullseye). If you still wish to install them manually, run ```pip install -r requirements.txt```. Otherwise, install just the 2 used packages (bardapi and gTTS). Using a virtual environment is recommended; however, I encountered issues with installing ```picamera2``` because of ```PyQt5```
* Run ```sudo apt install mpg123``` to install an MP3 player onto your system
7. Set the value of ```Bard_Cookie_Value``` in ```keys.json```: 
* Go to https://bard.google.com/ 
* F12 for developer console 
* Application → Cookies → Copy the value of ```__Secure-1PSID``` cookie.
8. Run ```python main.py``` to start the program

# Hardware Images
![image](https://cdn.discordapp.com/attachments/953870034227302470/1110371329825321102/IMG_1627.jpg)
Rough diagram of the project

![image](https://cdn.discordapp.com/attachments/953870034227302470/1110371318123208866/IMG_1615.jpg)
Raspberry Pi 4 Model B before hardware installations

![image](https://cdn.discordapp.com/attachments/953870034227302470/1110371329187774556/IMG_1625.jpg)
Raspberry Pi 4 Model B after hardware installations

![image](https://cdn.discordapp.com/attachments/991028278473134191/1126618381156626432/IMG-1741.jpg)
Glasses with camera and module