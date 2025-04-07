from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

rooms = []


# This is the straight corridor and all of it's components, this will be used after the player has left a Main Dungeon Room
straightCorridorGround = Entity(model='plane',
                    texture='textureStone.png', 
                    collider='box', 
                    scale=(25,1,5), 
                    position=(0,0,0))

straightCorridorRoof = Entity(model='plane',
                    texture='corridorWall.png', 
                    collider='box', 
                    scale=(25,1,5), 
                    position=(0,5,0),
                    rotation_x=180)

straightCorridorLeftWall = Entity(model='cube',
                      texture='corridorWall.png',
                      collider='box',
                      scale=(1,10,1),
                      position=(0,0,1),
                      rotation_y=90,
                      parent=straightCorridorGround)

straightCorridorRightWall = Entity(model='cube',
                      texture='corridorWall.png',
                      collider='box',
                      scale=(1,10,1),
                      position=(0,0,-1),
                      rotation_y=90,
                      parent=straightCorridorGround)

straightCorridorGround.texture_scale = (10,10)

# This is the main Dungeon Zone room and all of it's components

dungeonGround = Entity(model='plane',
                    texture='textureStone.png', 
                    collider='box', 
                    scale=(25,1,25), 
                    position=(25,0,0))


player = FirstPersonController()
player.position = (0,0,0)

app.run()

