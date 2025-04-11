from ursina import *
from gameplay.weapons import Weapon
from gameplay.player import Player
import random

class LootBox(Entity):
    def __init__(self, lootTable = [], position = Vec3(0, 0, 0)):
        super().__init__(
            model = 'cube',
            color = color.green,
            texture = None,
            collider = 'box',
            position = position,
            scale = Vec3(1, 1, 1))
        self.lootTable = lootTable
        self.isOpen = False

    #if held_keys('E'), then openBox()

    def openBox(self):
        #first check if inventory is full and don't open box if it is
        if not self.isOpen:
            self.isOpen = True
            self.color = color.gray
            self.extractLoot(player)

    def extractLoot(self, player):
        lootGained = random.choice(self.lootTable)
        weapon.weapons.append(lootGained)
        #need to add the weapon to the player's inventory
        for spawnLocation in range(5):
            position = Vec3(random.randint(-10, 10), 0, random.randint(-10, 10))
            box = LootBox(position=position)
            #add to inventory; will write this once inventory is created/weapons are finished
            #check if inventory is full first

player = Player()
weapon = Weapon()

app.run()