from ursina import *
from ursina.mesh_importer import load_model
import os

app = Ursina()

os.chdir(os.path.dirname(__file__))

model_path = 'character.fbx'  # ✅ Make sure this is the Blender-exported FBX 7.4 version

print("Working directory:", os.getcwd())
print("character_2013.fbx found:", os.path.exists(model_path))

character_model = load_model(model_path)

character = Entity(
    model=character_model,
    position=(0, 0, 0),
    scale=2,
    collider='box',
    color=color.white
)

camera.position = (0, 5, -20)
camera.look_at(character)

DirectionalLight(y=3, z=2, shadows=True)
Sky()

app.run()

# def spawnEnemy(self):
#     spawnLocation = random.randint(0,100)
#     self.springEnemy = None
#     self.summerEnemy = None
#     self.autumnEnemy = None
#     self.winterEnemy = None
