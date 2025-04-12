from ursina import *
from ursina.mesh_importer import load_model
import os

app = Ursina()

# Make sure we're working from the script directory
os.chdir(os.path.dirname(__file__))

model_path = 'Mutant.fbx'

print("Working directory:", os.getcwd())
print("Mutant.fbx found:", os.path.exists(model_path))

# Load the model using Panda3D's loader
mutant_model = load_model(model_path)

# Create the entity
mutant = Entity(
    model='Mutant.fbx',
    texture='white_cube',  # or use any image in your project
    position=(0, 0, 0),
    scale=1.5,
    color=color.white,
    collider='box'
)

# Setup camera to view it
camera.position = (0, 10, -40)   # Move camera back and up
camera.look_at(mutant)
EditorCamera()
# Lighting and environment
DirectionalLight(y=3, z=2, shadows=True)
Sky()

app.run()
