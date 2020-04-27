'''Based on the Pong game app, but now remove the paddles, and
only has a ball bouncing around. 

Wherever the user touches the screen, the ball restarts from there.
'''
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from random import randrange


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)
    i = 0

    def serve_ball(self):
        
        self.ball.center = self.center
        self.ball.velocity = self.gen_random_velocity()

    def gen_random_velocity(self):
        return  (randrange(0,10,2), randrange(0,10,2))
    
    def update(self, dt):
        self.ball.move()

        # bounce ball off bottom or top
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1
        # bounce ball off left and right
        if (self.ball.x < 0) or (self.ball.x>self.width):
            self.ball.velocity_x *= -1

    def on_touch_up(self, touch):
        self.i += 1 
        SoundLoader.load('base_tone.wav').play()
        print('I=',self.i)
        self.ball.center = touch.pos
        self.ball.velocity = self.gen_random_velocity()
    

class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 /100.0)
        return game


if __name__ == '__main__':
    PongApp().run()