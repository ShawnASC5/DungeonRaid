from ursina import *

class Enemy(Entity):
    def _init_(self, player, moveSpeed = 20, position = (0,0,0), **kwargs):
        super()._init_(
            model = 'Mutant.fbx',
            texture = 'white_cube',
            position = position,
            collider='box',
            color = color.white,
            **kwargs
        )

        self.player = player
        self.moveSpeed = moveSpeed
        self.hp = 3
        self.damage = 1

    
    def update(self):
        if distance(self, self.player) > 20:
            self.position += ((self.player.position + self.random) - self.position).normalized() * self.move_speed * time.dt

        self.look_at(self.player)
        self.rotation_z = 0
# def spawnEnemy(self):
#     spawnLocation = random.randint(0,100)
#     self.springEnemy = None
#     self.summerEnemy = None
#     self.autumnEnemy = None
#     self.winterEnemy = None
