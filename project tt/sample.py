import random
import string
from PIL import Image
from claptcha import Claptcha

def randomString():
    rndLetters = (random.choice(string.ascii_uppercase) for _ in range(6))
    return "".join(rndLetters)
for i in range(2):
    c = Claptcha(randomString, "FreeMono.ttf",noise = 0.3)
    text, _ = c.write('t' + str(i) + '.png')
