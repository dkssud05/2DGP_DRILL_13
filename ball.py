from pico2d import *
import random

class Ball:
    def __init__(self):
        self.x = random.randint(21, 1821)
        self.y = random.randint(21, 1000)
        self.image = load_image('ball21x21.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)