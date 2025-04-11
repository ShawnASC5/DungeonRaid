from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from player import Player

app = Ursina()

class Weapon(Entity):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.setupWeapons()

    def setupWeapons(self):
        self.knife = Entity(
            parent = self.controller.camera_pivot,
            scale = 0.002,
            model = 'assets/knife.zip/source/knife.fbx',
            texture = 'assets/knife.zip/textures/gltf_embedded_0@channels=G.jpeg',
            position = Vec3(0.7, -1, 1.5),
            rotation = Vec3(0, 170, 0),  
            visible = False)

        self.spear = Entity(
            parent = self.controller.camera_pivot,
            scale = 0.002,
            model = 'assets/spear.zip/source/spear.fbx',
            texture = 'assets/spear.zip/textures/St_concept_tex.png',
            position = Vec3(0.7, -1, 1.5),
            rotation = Vec3(0, 170, 0),
            visible = False
        )

        self.bow = Entity(
            parent = self.controller.camera_pivot,
            scale = 0.002,
            model = 'assets/bow.zip/source/lightning-bow-low-poly.fbx',
            texture = 'assets/bow.zip/textures/bow_diff.png',
            position = Vec3(0.7, -1, 1.5),
            rotation = Vec3(0, 170, 1.5),
            visible = False
        )

        self.weapons = [self.knife, self.spear, self.bow]
        self.currentWeaponIndex = 0
        self.currentWeapon = self.weapons[self.currentWeaponIndex]
        self.currentWeapon.visible = True
        self.switchWeapon()

    def input(self, key):
        if key == '0':
            self.currentWeapon.visible = False
        elif key.isdigit() and 1 <= int(key) <= len(self.weapons):
            self.switchWeapon(int(key)-1)
            self.currentWeapon.visible = True

    def switchWeapon(self, index):
        self.currentWeaponIndex = index

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