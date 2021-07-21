# NeoPixelRasberryPiPicoPython
NeoPixel Raspberry Pi Pico LED Lights Python

Welcome! If you are looking to use a Raspberry Pi Pico and connect it to an LED strip (WS2812B single addressable) you are in the right place. 

I bought a Raspberry Pi Pico and wanted to create some cool light shows on an LED strip. Since the Pico is new (as of writing) I was having trouble finding documentation and proper setup for the Raspberry Pi Pico. I figured I could document my process and help you get started without hitting the same stumbling blocks I hit. 

I am attaching my lights inside a wizard hat, so I am buying battery packs to run both my LED strip and Pico off of AA batteries. 


What you will need:
1. WS2812B single addressable LED strip - This is the one I ordered https://www.amazon.com/dp/B088FK5QBJ?ref=ppx_pop_mob_ap_share
2. Raspberry PI Pico - pre soldered (or not if you have a soldering kit) https://vilros.com/collections/raspberry-pi-pico
3. 3 AA Battery Holder With Micro USB Connector to Pico https://vilros.com/products/3-aa-battery-holder-with-micro-usb-connector-great-for-raspberry-pi-pico
4. Wires set. I bought this set  https://www.amazon.com/dp/B01EV70C78?ref=ppx_pop_mob_ap_share
5. Low Voltage Wire Connectors to easily connect LED wires to pico wires. I bought this set off amazon https://www.amazon.com/dp/B085PQG3L5?ref=ppx_pop_mob_ap_share
6. 4xAA Battery Pack Holder Case Box for LEDs https://www.amazon.com/dp/B07T65WWCR?ref=ppx_pop_mob_ap_share
7. DC Barrel Jack 10 Pairs 12V Male+Female... https://www.amazon.com/dp/B01J1WZENK?ref=ppx_pop_mob_ap_share
8. Micro USB to USB (to connect pico to labtop)


Installing Circuit Python and Neopixel onto your Raspberry PI Pico
1. Follow the instructions in this link https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython  or follow here click "Download the latest version of Circuit Python for Raspbery PI Pico from circuitpython.org". Hold down Bootsel button on Pico while plugging in your pico to your laptop via USB Micro cable, with the file explorer window that pops up, copy the downloaded UF2 file onto and put into the pico, once the file is on there you can unplug and replug in your Pico (don't hold the bootsel this time). 
2. Next you will want to open Thonny IDE (or download it if you don't have it already onto your laptop). With your Pico plugged in and Thonny open select  Run -> Select Interpreter -> and within the first dropdown choose CircuitPython (generic). And the second dropdown "Port" try and choose "Raspberry PI Pico" (I didn't see that option and just left it on "Try to detect port automatically" and it still works).
3. Next create a new script within your Raspberry Pi Pico. Copy the code from here https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/blob/main/neopixel.py and paste into the new script you created. Save your file as neopixel.py within your Raspberry Pi Pico.
4. Copy the code from my main.py file which has a bunch of light sequences. Create a new script within Thonny on your Raspberry Pi Pico, paste in the copied data,  save  your file as main.py. (by savings this file as main.py it will automatically run this file everytime you plug in your pico). 
5. Update your main.py ~around lines 29 ~ Setting your led_count to the number of LEDS on your strip, the pico GPIO Pin you are using (I am using 0), and change the brightness to values between 0.0 - 1.0.

    pico_pin = board.GP0 #set to GPIO 0
    led_count = 60
    pixels = neopixel.NeoPixel(pico_pin, led_count, brightness=1, auto_write=False)   


Setting up Raspberry Pi Pico
