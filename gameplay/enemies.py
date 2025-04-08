from ursina import *
import random

class Enemy(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        currentEnemy = None

    def spawnEnemy(self):
        spawnLocation = random.randint(0,100)
        self.springEnemy = None
        self.summerEnemy = None
        self.autumnEnemy = None
        self.winterEnemy = None
