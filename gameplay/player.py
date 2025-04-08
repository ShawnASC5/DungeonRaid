from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from settings import *
import math

app = Ursina()

class Player(Entity):
    def __init__(self, **kwargs):
        self.controller = FirstPersonController(**kwargs)
        super().__init__(parent = self.controller)

    def health_damage(self):
        self.healthBar = Button(bar_color=color.lime.tint(-.25), roundness=.5, max_value=100, value=50, scale=(.5,.1))