from ursina import *
from ursina import collider
from ursina import texture
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
ground = Entity(model = 'plane',texture = 'grass',collider = 'mesh',scale = (100,1,100))
Sky()
player = FirstPersonController()


blocks = []
direnctions = []
from random import uniform

for i in range(8):
    r = uniform(-2,2)
    block = Entity(
        model = 'cube',
        color=color.azure,
        texture='white_cube',
        position=(r,1+i,3+i*5),
        scale=(3,0.5,3),
        collider = 'box'
    )
    if r < 0:
        direnctions.append(1)
    else:
        direnctions.append(-1)
    blocks.append(block)

def update():
    i=0
    global direction
    for block in blocks:
        block.x -= direnctions[i]*time.dt
        if abs(block.x) > 5:
            direnctions[i] *= -1
        i=i+1
app.run()