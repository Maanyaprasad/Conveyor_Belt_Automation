from ursina import *
from ursina.prefabs.slider import Slider
from ursina.prefabs.button import Button

app = Ursina()

is_running = False
conveyor_speed = 0

# --------------------------------------------------
# Conveyor Frame
# --------------------------------------------------

frame = Entity(
    model='models/Conveyor_frame.glb',
    texture='models/Texture_blend_color_pallette.png',
    scale=0.03,
    position=(0, 0.3, 0),
    rotation=(0, 90, 0)
)

# --------------------------------------------------
# Conveyor Belt
# --------------------------------------------------

belt = Entity(
    model='models/Conveyor_moving_Belt.glb',
    texture='models/Texture_blend_color_pallette.png',
    scale=0.03,
    position=(0, 0.370, 0),
    rotation=(0, 90, 0)
)

# --------------------------------------------------
# Box on Conveyor
# --------------------------------------------------

box = Entity(
    model='models/Box_model.glb',
    texture='models/Texture_blend_color_pallette.png',
    scale=0.08,
    position=(-0.75, 0.28, 0),
    rotation=(0, 90, 0)
)

def start_conveyor():
    global is_running
    is_running = True

def stop_conveyor():
    global is_running
    is_running = False

def update():
    global conveyor_speed

    conveyor_speed = speed_slider.value

    if is_running:
        # Belt circular motion - rotates to show surface movement
        belt.rotation_x += conveyor_speed * 0.1
        
        # Box travels along the conveyor
        box.x += conveyor_speed * time.dt * 0.35
        if box.x > 0.75:
            box.x = -0.75

camera.position = (1.5, 0.3, 0)
camera.rotation_y = -90

DirectionalLight()
AmbientLight(color=color.rgba(170, 170, 170, 0.5))

start_button = Button(
    text='Start',
    color=color.green,
    scale=0.15,
    position=(-0.25, -0.35)
)
start_button.on_click = lambda: start_conveyor()

stop_button = Button(
    text='Stop',
    color=color.red,
    scale=0.15,
    position=(0.25, -0.35)
)
stop_button.on_click = lambda: stop_conveyor()

speed_slider = Slider(
    min=0,
    max=10,
    default=2,
    step=0.1,
    scale=0.5,
    position=(0, -0.2)
)

Sky()
app.run()