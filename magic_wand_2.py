'''
---------------------------------------------
Title: magic_wand.py
Description: This is for a magic LED wand good for short LED strips with ~8-16 LEDs  
List:
    1) SOLID COLORS
    2) RAINBOW
    3) COLOR CHASE
    4) RAINBOW CHASE
    5) FLASHING BRIGHTS
    6) COLOR CHASE LIST
    7) COLOR CHASE STICK
    8) MULTIPLE SEND
    9) RAINBOW COMET
    10) CUSTOM COLOR CHASE
    11) RAINBOW ANIMATIONS
    12) MAGIC WAND
Gentsch, 7/11/2021, Created File
---------------------------------------------
'''
#################
#-- Data code --#
#################
import board
import neopixel
import time
#from _pixelbuf import colorwheel
import random
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.helper import PixelMap
from adafruit_led_animation.group import AnimationGroup
from adafruit_led_animation.animation.customcolorchase import CustomColorChase
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.color import colorwheel
from adafruit_led_animation.color import PINK, GREEN, RED, BLUE

pico_pin = board.GP0 #set to GPIO 0
led_count = 30   ##### MAKE SURE TO PICK EVEN NUMBER
num_strands = 1
pixels = neopixel.NeoPixel(pico_pin, led_count, brightness=1, auto_write=False)  

rainbow_range =[0.00 ,  0.01,  0.02,  0.03,  0.04]
color_chase_range = [0.00 ,  0.01,  0.02,  0.03,  0.04]  #a range between 0 and .05 is good

#for rainbow comet
strips = [PixelMap(pixels, range(i*led_count, (i+1)*led_count), individual_pixels=True)
    for i in range(num_strands)]


#for Flashing Brights
max_len=9
min_len = 2
num_flashes = 20

#colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
no_color = (0,0,0)
cyan = (0, 255, 255)
purple = (180, 0, 255)
yellow = (255, 150, 0)

# bright colors https://coolors.co/ff0000-ff8700-ffd300-deff0a-a1ff0a-0aff99-0aefff-147df5-580aff-be0aff
bright_list = [
[255, 0, 0] ,  # Red
[255, 135, 0] ,  # Dark Orange
[255, 211, 0] ,  # Cyber Yellow
[222, 255, 10] ,  # Chartreuse Traditional
[161, 255, 10] ,  # Spring Bud
[10, 255, 153] ,  # Medium Spring Green
[10, 239, 255] ,  # Electric Blue
[20, 125, 245] ,  # Azure
[88, 10, 255] ,  # Han Purple
[190, 10, 255]  # Electric Purple
]

#https://coolors.co/9ba9ff-a5adff-afb1ff-b9b5ff-c4baff-cebeff-d8c2ff-e2c6ff-eccaff
#https://coolors.co/dec9e9-dac3e8-d2b7e5-c19ee0-b185db-a06cd5-9163cb-815ac0-7251b5-6247aa
#https://coolors.co/7400b8-6930c3-5e60ce-5390d9-4ea8de-48bfe3-56cfe1-64dfdf-72efdd-80ffdb
#https://coolors.co/03045e-023e8a-0077b6-0096c7-00b4d8-48cae4-90e0ef-ade8f4-caf0f8
purple_blue_list = [
[155, 169, 255] ,  # Maximum Blue Purple
[165, 173, 255] ,  # Maximum Blue Purple
[175, 177, 255] ,  # Maximum Blue Purple
[185, 181, 255] ,  # Maximum Blue Purple
[196, 186, 255] ,  # Lavender Blue
[206, 190, 255] ,  # Lavender Blue
[216, 194, 255] ,  # Lavender Blue
[226, 198, 255] ,  # Mauve
[236, 202, 255] ,  # Mauve
[222, 201, 233] ,  #* Thistle
[218, 195, 232] ,  # Thistle
[210, 183, 229] ,  # Pink Lavender
[193, 158, 224] ,  # Wisteria
[177, 133, 219] ,  # Lavender Floral
[160, 108, 213] ,  # Amethyst
[145, 99, 203] ,  # Amethyst
[129, 90, 192] ,  # Blue Violet Crayola
[114, 81, 181] ,  # Royal Purple
[98, 71, 170] ,  # Plump Purple
[116, 0, 184] ,  #* Purple
[105, 48, 195] ,  # French Violet
[94, 96, 206] ,  # Slate Blue
[83, 144, 217] ,  # Tufts Blue
[78, 168, 222] ,  # Blue Jeans
[72, 191, 227] ,  # Vivid Sky Blue
[86, 207, 225] ,  # Sky Blue Crayola
[100, 223, 223] ,  # Medium Turquoise
[114, 239, 221] ,  # Turquoise
[128, 255, 219] ,  # Aquamarine
[202, 240, 248] ,   # Powder Blue
[173, 232, 244] ,  # Blizzard Blue
[144, 224, 239] ,  # Sky Blue Crayola
[72, 202, 228] ,  # Sky Blue Crayola
[0, 180, 216] ,  # Cerulean Crayola
[0, 150, 199] ,  # Blue Green
[0, 119, 182] ,  # Star Command Blue
[2, 62, 138] ,  # Dark Cornflower Blue
[3, 4, 94]      # Navy Blue
]


# green yellow https://coolors.co/007f5f-2b9348-55a630-80b918-aacc00-bfd200-d4d700-dddf00-eeef20-ffff3f
# yellow https://coolors.co/ff7b00-ff8800-ff9500-ffa200-ffaa00-ffb700-ffc300-ffd000-ffdd00-ffea00
# yellow to red https://coolors.co/ff4800-ff5400-ff6000-ff6d00-ff7900-ff8500-ff9100-ff9e00-ffaa00-ffb600
greenyellow_list = [
[0, 127, 95] ,  # Spanish Viridian
[43, 147, 72] ,  # Spanish Green
[85, 166, 48] ,  # Green RYB
[128, 185, 24] ,  # Apple Green
[170, 204, 0] ,  # Android Green
[191, 210, 0] ,  # Bitter Lemon
[212, 215, 0] ,  # Pear
[221, 223, 0] ,  # Titanium Yellow
[238, 239, 32] ,  # Xanthic
[255, 255, 63],   # Maximum Yellow
[255, 234, 0] ,  #* Middle Yellow
[255, 221, 0] ,  # Sizzling Sunrise
[255, 208, 0] ,  # Cyber Yellow
[255, 195, 0] ,  # Mikado Yellow
[255, 183, 0] ,  # Selective Yellow
[255, 170, 0] ,  # Chrome Yellow
[255, 162, 0] ,  # Orange Web
[255, 149, 0] ,  # Yellow Orange Color Wheel
[255, 136, 0] ,  # Dark Orange
[255, 123, 0] ,  # Heat Wave
[255, 182, 0] ,  #* Selective Yellow
[255, 170, 0] ,  # Chrome Yellow
[255, 158, 0] ,  # Orange Peel
[255, 145, 0] ,  # Yellow Orange Color Wheel
[255, 133, 0] ,  # Dark Orange
[255, 121, 0] ,  # Heat Wave
[255, 109, 0] ,  # Pumpkin
[255, 96, 0] ,  # Safety Orange Blaze Orange
[255, 84, 0] ,  # Orange Pantone
[255, 72, 0]   # Red Orange Color Wheel
]


######################
#-- Processing code--#
######################
def clear_strip_color():
    pixels.fill(no_color)   #when autowrite=False this won't work!
    pixels.show()
    time.sleep(.2)

def rainbow(speed): #this one is really cool on a loop with speed of 0
    for j in range(255):
        for i in range(led_count):
            pixel_index = (i * 256 // led_count) + j
            pixels[-i] = colorwheel(pixel_index & 255)
        pixels.show()
        time.sleep(speed)
        
def color_chase(color, wait):
    for i in range(led_count):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.2)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def rainbow_cycle_chase(cycle): #flutter the lights on and off
    for j in range(cycle): # j is one execution of the led strip
        for i in range(led_count):
            rc_index = (i * 256 // led_count) + j
            for k in range(led_count):
                pixels[i] = wheel(rc_index & 255)  #this makes sure its 255 and under
                pixels.show()
        #pixels.show()
        #time.sleep(wait)
        pixels.fill((0,0,0))
        pixels.show()
    for i in range(led_count):
        rc_index = (i * 256 // led_count) + j
        for k in range(led_count):
            pixels[-i] = wheel(rc_index & 255) #this sends is backwards
            pixels.show()
            
            
def rainbow_skip(speed): 
    for i in range(0, led_count, 2): #this will add a rainbow color on every even (0,2)
        rc_index = (i * 256 // led_count) + 0
        pixels[i] = wheel(rc_index & 255)
        pixels.show()
        time.sleep(speed)
    for i in range(0, led_count, 2): #this will add a rainbow color on every odd (1,3)
        rc_index = (i * 256 // led_count) + 0
        pixels[i+1] = wheel(rc_index & 255)
        pixels.show()
        time.sleep(speed)
#     for i in range(0, led_count, 2): #this will remove color on every even (0,2)
#         rc_index = (i * 256 // led_count) + 0
#         pixels[-i] = (no_color)
#         pixels.show()
#         time.sleep(speed)
#     for i in range(0, led_count, 2):  #this will remove color on every odd (1,3)
#         rc_index = (i * 256 // led_count) + 0
#         pixels[1-i] = (no_color)
#         pixels.show()
#         time.sleep(speed)

def flashing_brights(color_list):
    flashing = []
    for i in range(num_flashes):
        pix = random.randint(0, led_count - 1)
        col = random.randint(1, len(color_list) - 1)
        flash_len = random.randint(min_len, max_len)
        flashing.append([pix, color_list[col], flash_len, 0, 1])
        
    pixels.fill((0,0,0))
    pixels.show()

    for x in range(100):
        pixels.show()
        for i in range(num_flashes):
            pix = flashing[i][0]
            brightness = (flashing[i][3]/flashing[i][2])
            colr = (int(flashing[i][1][0]*brightness), 
                    int(flashing[i][1][1]*brightness), 
                    int(flashing[i][1][2]*brightness))
            pixels[pix] = (colr[0], colr[1], colr[2])

            if flashing[i][2] == flashing[i][3]:
                flashing[i][4] = -1
            if flashing[i][3] == 0 and flashing[i][4] == -1:
                pix = random.randint(0, led_count - 1)
                col = random.randint(0, len(color_list) - 1)
                flash_len = random.randint(min_len, max_len)
                flashing[i] = [pix, color_list[col], flash_len, 0, 1]
            flashing[i][3] = flashing[i][3] + flashing[i][4]
            time.sleep(0.005)

def color_chase_list(wait, color_list):
    j = 0
    for i in range(led_count):
        pixels[i] = color_list[j]
        time.sleep(wait)
        pixels.show()
        j = j + 1
        if j == len(color_list):
            j = 0
    time.sleep(0.1)
    
    j = 0
    for i in range(led_count):
        pixels[-i] = [0,0,0]
        time.sleep(wait)
        pixels.show()
        j = j + 1
        if j == len(color_list):
            j = 0
    time.sleep(0.1)
    
    j = 0
    for i in range(led_count):
        pixels[-i] = color_list[j]
        time.sleep(wait)
        pixels.show()
        j = j + 1
        if j == len(color_list):
            j = 0
    time.sleep(0.1)
    
    j=0
    for i in range(led_count):
        pixels[-i] = [0,0,0]
        time.sleep(wait)
        pixels.show()
    j = j + 1
    if j == len(color_list):
        j = 0
    time.sleep(0.1)


def chase_color_stick(color_list):
    for j in range(led_count): #loop through all led positions. Each J is one iteration of the LED strip
        color_choice = random.choice(color_list) #assign a color per strip loop
        for x in range(led_count): #this loops gives the appearence of jumping down the strip positions
            if x + j < (led_count): #turn on, turn off, wait, and next position ....iterate. Stopping at the last position reached
                pixels[x] = color_choice
                pixels.show()
                time.sleep(x*1.0012 - x)
                pixels[x] = no_color
                #print('j =', j , ' x = ', x, ' x+j=', x+j) #uncomment to troubleshoot
                
            elif x + j == led_count: #if you reached the stopping point of postion x, fill that cell and turn all prior cells the new landed color
                pixels[x] = color_choice
                pixels.show()
                if j > x: #for  x loop values 31-60. When you filled back end half of strip, and need to fill front half of strip. Change increment to j strip loop counter
                    pixels[x:] = [color_choice] * (j)
                    pixels.show()
                elif led_count % x == 0:   #when you reach x = 30  (if you have 60 leds)
                    pixels[x:] = [color_choice] * (x)
                    pixels.show()
                else: #this is for x loops 0-29. When you are filling up the back end of the strip
                    pixels[x:] = [color_choice] * (led_count % x)
                    pixels.show()
                #print(f'LED stopping point reached with {led_count} leds j =', j , '  position x =', x) #uncomment to troubleshoot

def multiple_send(wait, color_list, line_length):
    j = 0
    for i in range(led_count):
        try:
            #print('position:', i, "color:", color_list[j])
            pixels[i:i+line_length] = color_list[j] * line_length
            pixels.show()
            time.sleep(wait)
            pixels[i:i+line_length] = no_color * line_length
            j = j + 1
            if j == len(color_list):
                j = 0
        except:
            #print(line_length, i, j)
            pass
    time.sleep(0.1)
#     #send backwards
#     j = 0
#     for i in range(led_count):
#         #print('position i:', i, "color:", color_list[j])
#         try:
#             #print((-i), -i -line_length)
#             pixels[-i:-i-line_length:-1] = color_list[j] * line_length
#             pixels.show()
#             time.sleep(wait)
#             pixels[-i:-i-line_length:-1] = no_color * line_length
#             pixels.show()
#             j = j + 1
#             if j == len(color_list):
#                 j = 0
#         except:
#             pass
#     time.sleep(0.1)

def make_animation(strip):
    speed = (1+random.random()) * 0.02
    length = random.randrange(4, 7)
    bounce = random.random() > .5
    offset = random.randint(0, 255)
    return RainbowComet(strip, speed=speed, tail_length=length, bounce=bounce,
        colorwheel_offset=offset)


pixels.fill(no_color)   #when autowrite=False this won't work!
pixels.show()
time.sleep(.25)
##############################
#-- Presentation (I/0) code--#
##############################
        
for x in range(3):    
    ####SOLID COLORS####
    #print('no color')
    clear_strip_color()
    
    #print('red')
    pixels.fill(red)
    pixels.show()
    time.sleep(1)
    clear_strip_color()
    
    #print('green')
    pixels.fill(green)
    pixels.show()
    time.sleep(1)
    clear_strip_color()
    
    #print('blue')
    pixels.fill(blue) 
    pixels.show()
    time.sleep(1)
    clear_strip_color()
    
    ####RAINBOW####
    for x in range(5): #this is my favorite! Rainbow(0)
        rainbow(0)
    for x in rainbow_range:
        rainbow(x * .1)
    clear_strip_color()

    #####COLOR CHASE####
    color_chase(red, random.choice(color_chase_range))  # Increase the number to slow down the color chase
    color_chase(yellow, random.choice(color_chase_range)) 
    color_chase(green, random.choice(color_chase_range))
    for x in range(5): #this is my favorite! Rainbow(0)
        rainbow(0)
    color_chase(cyan, random.choice(color_chase_range)) 
    color_chase(blue, random.choice(color_chase_range)) 
    color_chase(purple, random.choice(color_chase_range)) 
    
    #####RAINBOW CHASE####
    rainbow_cycle_chase(1) # number of cycles
    clear_strip_color()

    ####RAINBOW SKIP####
    rainbow_skip(.02) #speed
    color_chase(cyan, .02)
    clear_strip_color()
    color_chase(blue, .02)
    clear_strip_color()
    color_chase(purple, .02)
    clear_strip_color()
    
    ####FLASHING BRIGHTS####
    flashing_brights(purple_blue_list)
    flashing_brights(greenyellow_list)
    clear_strip_color()

    ####COLOR CHASE LIST####
    color_chase_list(.04, purple_blue_list)
    color_chase_list(.04, greenyellow_list)
    color_chase_list(.04, bright_list)
    clear_strip_color()

    ####CHASE COLOR STICK####
    chase_color_stick(bright_list)
    
    #RAINBOW COMET
    animations = [make_animation(strip) for strip in strips]
    group = AnimationGroup(*animations, )
    t_end = time.time() + 30 * 1  #run while loop for 60 seconds * x
    while time.time() < t_end:
        group.animate()
    chase_color_stick(purple_blue_list)
    chase_color_stick(greenyellow_list)
    clear_strip_color()
    
    ####MULTIPLE SEND####
    for y in range(10):
        multiple_send(random.choice(color_chase_range), greenyellow_list, random.randint(1,5))# wait, color list, how many leds to send
        clear_strip_color()

    #RAINBOW COMET
    #animations = [make_animation(strip) for strip in strips]
    #group = AnimationGroup(*animations, )
    t_end = time.time() + 30 * 1  #run while loop for 60 seconds * x
    while time.time() < t_end:
        group.animate()
    
    #CUSTOM COLOR CHASE
    custom_color_chase_rainbow = CustomColorChase(pixels, speed=0.1, size=2, spacing=3)
    #custom_color_chase_rainbow_r = CustomColorChase(pixels, speed=0.1, size=3, spacing=3, reverse=True)
    steps = 30
    rainbow_colors = [colorwheel(n % 256) for n in range(0, 512, steps)]
    custom_color_chase_rainbowchase = CustomColorChase(pixels, speed=0.1, colors=rainbow_colors, size=2, spacing=3) # Now use rainbow_colors with CustomColorChase
    custom_color_chase_bgp = CustomColorChase(pixels, speed=0.1, colors=[BLUE, GREEN, PINK], size=3, spacing=2)

    animations = AnimationSequence(
        custom_color_chase_rainbow,
        #custom_color_chase_rainbow_r,
        custom_color_chase_rainbowchase,
        custom_color_chase_bgp,
        advance_interval=6,
        auto_clear=True,
    )
    t_end = time.time() + 30 * 1  #run while loop for 60 seconds * x
    while time.time() < t_end:
        animations.animate()
    
    #magic wand flickering
    for loop in range(3):
        color_choice = random.choice(bright_list)
        for x in range(led_count):
            pixels[x] = color_choice
            pixels.show()
            time.sleep(.3-(x*.01))   ## .01 works for ~30 leds .025 for ~10 leds
            pixels[x] = no_color
            pixels.show()
            #print(x)
            if x == led_count -4:
                for i in range(40):
                    pixels[x] = color_choice
                    pixels[x+1] = no_color
                    pixels[x+2] = color_choice
                    pixels.show()
                    time.sleep(.05)
                    #inverse
                    pixels[x] = no_color
                    pixels[x+1] = color_choice
                    pixels[x+2] = no_color
                    pixels.show()
                    time.sleep(.05)
                    if i % 10 == 0:
                        pixels.fill(color_choice)
                        pixels.show()
                        time.sleep(.03)
                        pixels.fill(no_color)
                        pixels.show()
                    if i % 20 == 0:
                        pixels.fill(no_color)
                        color_chase(color_choice,.018)
                        pixels.fill(no_color)
        
    
    
    
#finish the loops
pixels.fill(no_color)
pixels.show()
print('\n Finished')
