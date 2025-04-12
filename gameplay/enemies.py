from ursina import *
# from particles import Particles
# from guns import Bullet
import random
app = Ursina()
 
#import random position when we know dimensions of the dungeon
class Enemy(Entity):
    def __init__(self, player, move_speed, position = (0,0,0), damage = 10, **kwargs):
        super().__init__(
            model = 'quad',
            texture = "zombieFemaleA.png",
            position = position,
            scale = (2,2),
            **kwargs
        )        

player = Entity(model='cube', color=color.orange, position=(0,0,0))
orc = Enemy(player=player, move_speed=1, position=(3,0,0))

camera.z = -10
app.run()

# def spawnEnemy(self):
#     spawnLocation = random.randint(0,100)
#     self.springEnemy = None
#     self.summerEnemy = None
#     self.autumnEnemy = None
#     self.winterEnemy = None
