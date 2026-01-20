"""
simplest possible starting code with one motionless boid
display a single object, inert, at (100, 100)
"""

import arcade
import math

BACKGROUND = arcade.color.ALMOND
IMAGE = "media/arrow-resized.png"

class Boid(arcade.Sprite):
    def __init__(self, position_x: float, position_y: float, angle: float, speed: float = 1.0):
        super().__init__(IMAGE)
        self.center_x = position_x
        self.center_y = position_y
        self.angle = angle
        self.speed = speed

    def move_left(self):
        self.angle -= 5
    
    def move_right(self):
        self.angle += 5
    
    def move(self):
        """
        Ceci va permettre de faire bouger mes boids
        """
        self.center_x += math.cos(self.angle_radian()) * self.speed
        self.center_y -= math.sin(self.angle_radian()) * self.speed

    def angle_radian(self):
        return self.angle / 180 * math.pi
    
    def accelerate(self):
        self.speed += 0.1

class Window(arcade.Window):

    def __init__(self):
        super().__init__(800, 800, "My first boid")
        arcade.set_background_color(BACKGROUND)
        self.set_location(800, 100)
        self.boids = [Boid(100, 600, 10), Boid(90, 500, -20, 2)]

        self.sprites = arcade.SpriteList()
        for boid in self.boids:
            self.sprites.append(boid)

    def on_draw(self):
        self.clear()

        self.sprites.draw()
    
    def on_key_press(self, symbol: int, modifiers: int) -> None:
        if symbol == arcade.key.LEFT:
            for boid in self.boids:
                boid.move_left()
        elif symbol == arcade.key.RIGHT:
            for boid in self.boids:
                boid.move_right()
        elif symbol == arcade.key.UP:
            for boid in self.boids:
                boid.accelerate()


    def on_update(self, delta_time):
        for boid in self.boids:
            boid.move()
        self.sprites.update()

window = Window()
arcade.run()
