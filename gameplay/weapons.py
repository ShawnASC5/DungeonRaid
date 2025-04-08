from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from player import Player
from enemies import Enemy

app = Ursina()

class Weapon(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def weapons(self):
        self.blade = Entity(
            parent = self.controller.camera_pivot,
            scale = 0.002,
            model = 'C:/Users/justi/OneDrive/assets/knife.zip/source/energyblade_clean.blend',
            texture = 'C:/Users/justi/OneDrive/assets/knife.zip/textures',
            position = Vec3(0.7, -1, 1.5),
            rotation = Vec3(0, 170, 0),  
            visible = False)

        self.spear = Entity(
            parent = self.controller.camera_pivot,
            scale = 0.002,
            model = 'C:/Users/justi/OneDrive/assets/spear.zip/source/spear.fbx',
            texture = 'C:/Users/justi/OneDrive/assets/spear.zip/textures/St_concept_tex.png',
            position = Vec3(0.7, -1, 1.5),
            rotation = Vec3(0, 170, 0),
            visible = False
        )

        self.bow = Entity(
            parent = self.controller.camera_pivot,
            scale = 0.002,
            model = 'C:/Users/justi/AppData/Local/Temp/0de53608-794f-406c-ba93-61029a40d917_bow.zip.917/source/Glowy Magic Bow.zip/Glowy Magic Bow.bin',
            texture = 'C:/Users/justi/AppData/Local/Temp/0de53608-794f-406c-ba93-61029a40d917_bow.zip.917/textures',
            position = Vec3(0.7, -1, 1.5),
            rotation = Vec3(0, 170, 1.5),
            visible = False
        )

        self.fists = Entity(
            parent = self.controller.camera_pivot,
            scale = 0.002,
            model = 'C:/Users/justi/OneDrive/assets/fists.zip/source/Fists_Anim.fbx',
            texture = 'C:/Users/justi/OneDrive/assets/fists.zip/textures/',
            position = Vec3(0.7, -1, 1.5),
            rotation = Vec3(0, 170, 0),
            visible = False
        )

        self.weapons = [self.blade, self.spear, self.bow, self.fists]
        self.current_weapon_index = 0
        self.current_weapon = self.weapons[self.current_weapon_index]
        self.switch_weapon()

    def input(self, key):
        if key == '0':
            self.currentWeapon.visible = False
        elif key.isdigit() and 1 <= int(key) <= len(self.weapons):
            self.switch_weapon(int(key)-1)
            self.current_weapon.visible = True

    def switch_weapon(self, index):
        self.current_weapon_index = index

    def active(self):
        self.rotation = Vec3(0, 45, 5)
        self.position = Vec3(0, 0, 1)

    def passive(self):
        self.rotation = Vec3(0, 0, 5)
        self.position = Vec3(0, 0, 0)

player = Player()
weapon = Weapon()

def update():
    if held_keys['left mouse']:
        weapon.active()
    else:
        weapon.passive()

app.run()