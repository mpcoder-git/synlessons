from map import Map
import time
import os
import json
from helicopter import Helicopter as Helico
from pynput import keyboard
from clouds import Clouds

TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 100
CLOUDS_UPDATE = 100
MAP_W, MAP_H = 10, 10

tick = 1
field = Map(MAP_W,MAP_W)
clouds = Clouds(MAP_W, MAP_H)
helico = Helico(MAP_W, MAP_H)

MOVES = {'w':(-1,0), 'd':(0,1), 's':(1,0), 'a':(0,-1)}
# f - save, g - load

def process_key(key):
    global helico, tick, clouds, field    
    c = key.char.lower()
    # move helicopter
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx,dy)
    # save game
    elif c == 'f':
        data = {"helicopter": helico.export_data(), 
                "clouds": clouds.export_data(), 
                "field":field.export_data(),
                "tick": tick}
        with open("level.json","w") as lvl:
            json.dump(data, lvl)
    # load game
    elif c == 'g':
        with open("level.json","r") as lvl:
            data = json.load(lvl)
            helico.import_data(data["helicopter"])
            tick = data["tick"] or 1
            field.import_data(data["field"])
            clouds.import_data(data["clouds"])
    
    if (key.char == 'a' or key.char == 'A'):
        print('cool')
    # print('{0} released'.format(
    #     key))
    # if key == keyboard.Key.esc:
    #     # Stop listener
    #     return False

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()









while True:
    os.system('cls')
    print('tick', tick)
    field.process_helicopter(helico, clouds)
    helico.print_stats()
    field.print_map(helico, clouds)
    
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        field.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        field.update_fires()
    if (tick % CLOUDS_UPDATE == 0):
        clouds.update_clouds()