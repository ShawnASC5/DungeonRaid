from ursina import *

health_bar = Entity(parent=camera.ui, model='quad', color=color.red, scale=(0.5, .05), position=(-.3, .45))
def updatePlayerHealth(player):
    healthBar = max(0, player.hp / player.max_hp) * 0.5

