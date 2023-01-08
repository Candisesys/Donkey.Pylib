from pyray import *
import random
class Car:
    def __init__(self, pos_vec : Vector2):
        self.pos_vec = pos_vec
        self.sprite = load_texture("data/gfx/car.png")
        self.posIndex = 0
        self.collrec = Rectangle(self.pos_vec.x, self.pos_vec.y, self.sprite.width, self.sprite.height)
    def update(self):
        positions = [
            Vector2(170,  230),
            Vector2(260,  230)
        ]
        if (is_key_pressed(32)):
            self.posIndex = self.posIndex + 1
            print(positions[self.posIndex%2].x, " ", positions[self.posIndex%2].y)
        self.pos_vec = positions[self.posIndex%2]
        self.collrec = Rectangle(self.pos_vec.x, self.pos_vec.y, self.sprite.width, self.sprite.height)
    def draw(self):
        draw_texture_v(self.sprite, self.pos_vec, WHITE)

class Donkey:
    def __init__(self, pos_vec: Vector2, speed: float):
        self.pos_vec = pos_vec
        self.texture = load_texture("data/gfx/donkey.png")
        self.speed = speed
        self.collrec = Rectangle(self.pos_vec.x, self.pos_vec.y, self.texture.width, self.texture.height)
    def update(self):
        self.pos_vec.y += self.speed
        self.collrec = Rectangle(self.pos_vec.x, self.pos_vec.y, self.texture.width, self.texture.height)
    def draw(self):
        draw_texture_v(self.texture, self.pos_vec, WHITE)