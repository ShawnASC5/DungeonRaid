from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from settings import *

class Game(Entity):
    def __init__(self):
        super().__init__()
    
    def newGame(self):
        pass

    def draw(self):
        self.screen.fill(color = color.black)
