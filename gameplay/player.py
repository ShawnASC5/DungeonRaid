from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from settings import *
import math

app = Ursina()

class Player(Entity):
    def __init__(self, **kwargs):
        self.controller = FirstPersonController(**kwargs)
        super().__init__(parent = self.controller)

class PlayerHealth(Button):   
    def __init__(self):
        pass
    
class Inventory(Entity):
    def __init__(self):
        pass