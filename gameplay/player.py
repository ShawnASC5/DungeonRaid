from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from settings import *
import math

app = Ursina()

class Player(Entity):
    def __init__(self, **kwargs):
        # Player placeholder
        super().__init__(model='cube', color=color.white, scale_y=2, collider='box', **kwargs)
        self.hp = 100 
        self.speed = 5
        # input weapons later
        self.weapons = []
        self.current_weapon = 0

    def update(self):
        self.move()
        self.switch_weapon()

    def move(self):
        if held_keys['w']:
            self.position += self.forward * time.dt * self.speed
        if held_keys['s']:
            self.position -= self.forward * time.dt * self.speed
        if held_keys['a']:
            self.position -= self.right * time.dt * self.speed
        if held_keys['d']:
            self.position += self.right * time.dt * self.speed
    
    def switch_weapon(self):
        # key clicked to switch weapon
        if held_keys['tab']:
            self.current_weapon = (self.current_weapon + 1) % len(self.weapons)
            print(f"Switched to weapon {self.current_weapon}")

    def health_damage(self,amount):
        self.hp -= amount
        print(f"Player took {amount} damage. HP: {self.hp}")
        if self.hp <= 0:
            print("Player is dead")
            self.disable()
            
            
