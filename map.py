from utils import randbool
from utils import randcell
from utils import randcell2


CELL_TYPES = "🟩🌳🌊🏥🏠🔥"


class Map:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]
    
    def chek_bounds(self, x, y):
       if (x < 0 or y < 0 or x >= self.h or y >= self.w):
          return False
       return True
              
    def print_map(self, helico, clouds): 
     print('⬛' * (self.w + 2))  # Верхняя рамка
     for ri in range(self.h):
        print('⬛', end="")
        for ci in range(self.w):
            cell = self.cells[ri][ci]
            cloud = clouds.cells[ri][ci]
            if cloud == 1:
                print("⬜", end="")
            elif cloud == 2:
                print("⬛", end="")
            elif (helico.x == ri and helico.y == ci):
                print("🚁", end="")
            elif (cell >=0 and cell < len(CELL_TYPES)):
                print(CELL_TYPES[cell], end="")
            else:
                print(" ", end="")
        print('⬛')  # Правая рамка
     print('⬛' * (self.w + 2))  # Нижняя рамка


    def generate_river(self, l):
       rc = randcell(self.w, self.h)
       rx, ry =rc[0], rc[1] 
       self.cells[rx][ry] = 2
       while l > 0 :
          rc2 = randcell2(rx, ry)
          rx2, ry2 = rc2[0], rc2[1]
          if (self.chek_bounds(rx2, ry2)):
             self.cells[rx2][ry2] = 2
             rx, ry = rx2, ry2
             l -= 1

    def generate_forest(self, r, mxr):
       for ri in range(self.h):
          for ci in range(self.w):
             if randbool(r, mxr):
                self.cells[ri][ci] = 1

    def generate_three(self):
       c = randcell(self.w, self.h)
       cx, cy = c[0], c[1]
       if (self.chek_bounds(cx, cy) and self.cells[cx][cy] == 0):
            self.cells[cx][cy] = 1
   

    def add_fire(self):
      c = randcell(self.w, self.h)
      cx, cy = c[0], c[1]   
      if self.cells[cx][cy] == 1:
        self.cells[cx][cy] = 5

    def update_fire(self):
       for ri in range(self.h):
          for ci in range(self.w):
             cell = self.cells[ri][ci] #бесполезная механика удаления огня через время
             if cell == 5:
                self.cells[ri][ci] = 0

    def process_helicoper(self, helico):
       c = self.cells[helico.x][helico.y]
       if (c == 2):
          helico.tank = helico.mxtank
       elif (c == 5 and helico.tank > 0):
          helico.tank -= 1
          self.cells[helico.x][helico.y] = 0
          helico.point += 1
       elif (c == 5 and helico.tank == 0):
          helico.point -= 10
          helico.live -= 1
          self.cells[helico.x][helico.y] = 0