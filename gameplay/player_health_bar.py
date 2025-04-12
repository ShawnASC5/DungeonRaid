from ursina import *

health_bar = Entity(parent=camera.ui, model='quad', color=color.red, scale=(0.5, .05), position=(-.3, .45))
def updatePlayerHealth(player):
    health_ratio = max(0, player.hp / player.max_hp)
    health_bar.scale_x = health_ratio * 0.5
