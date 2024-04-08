from utils import randcell
class Helicopter:
    def __init__(self, w, h):
        self.w = w  # сохраняем ширину как атрибут объекта
        self.h = h  # сохраняем высоту как атрибут объекта
        rc = randcell(w, h)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.y = ry
        self.tank = 0
        self.mxtank = 1
        self.point = 0
        self.live = 3
    def move(self, dx, dy): 
        nx = dx + self.x
        ny = dy + self.y
        if (nx >= 0 and ny >= 0 and nx < self.h and ny < self.w):
            self.x, self.y = nx, ny
 
    def print_stats(self):
        print('💦 ', self.tank, '/', self.mxtank, sep="", end=" | ")
        print('🏆 ', self.point, end=" | ")
        print('🧡 ', self.live)
 