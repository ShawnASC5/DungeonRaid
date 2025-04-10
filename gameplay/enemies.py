from ursina import *
import random
from player import Player

class Enemy(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.currentEnemy = None

    def spawnEnemy(self):
        spawnLocation = random.randint(0,100)
        self.springEnemy = None
        self.summerEnemy = None
        self.autumnEnemy = None
        self.winterEnemy = None

player = Player()

app.run()