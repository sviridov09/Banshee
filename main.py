from map import Map
import time
import os
from helicopter import Helicopter as helic
from pynput import keyboard
from clouds import Clouds

TICK_SLEEP = 0.1
# TICK_SLEEP = 1 / 59
THREES_UPDATE = 50
FIRE_UPDATE = 5
MAP_W, MAP_H = 40, 10
CLOUDS_UPDATE = 30

field = Map(MAP_W,MAP_H)
field.generate_forest(5, 10)
field.generate_river(10)
field.generate_river(30)
field.generate_river(40)
field.generate_river(25)

clouds = Clouds(MAP_W, MAP_H)
helico = helic(MAP_W, MAP_H)

MOVES = {'w': (-1, 0),
         'd':  (0, 1),
         's':  (1, 0),
         'a': (0, -1),
         'ц': (-1, 0),
         'в':  (0, 1),
         'ф': (0, -1),
         'ы':  (1, 0)}

def process_key(key):
    global helico
    c = key.char.lower()
    if c in MOVES.keys():
     dx, dy = MOVES[c][0], MOVES[c][1]
     helico.move(dx, dy)


    
  #  if key == keyboard.Key.esc:
        # Stop listener
       # return False
    
# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=None,
    on_release = process_key)
listener.start()

tick = 1
while True:
    os.system('cls')
    print("TICK", tick)
    field.process_helicoper(helico)
    helico.print_stats()
    field.print_map(helico, clouds) # Печатаем текущее состояние карты
    tick += 1

    if (tick % THREES_UPDATE == 0):
        field.generate_three()  # Генерируем новые деревья
    if (tick % FIRE_UPDATE == 0):
        field.add_fire()
    time.sleep(TICK_SLEEP)
    if (tick % CLOUDS_UPDATE == 0):
        clouds.update()
