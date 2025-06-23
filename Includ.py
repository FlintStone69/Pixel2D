import pygame
import time
import win32gui
import pyautogui
from Colors import *
from Materials import *

HEIGHT = 600
WIDTH = 800
FPS = 60


class Particles:
    def __init__(self, x: int, y: int, color, dt):
        self.X = x
        self.Y = y
        self.Color = color
        self._Mat = None
        self.Velocity = 0  
        self.FallB = False
        self.dt = dt

    def AddMaterial(self, Mat):
        if isinstance(Mat, Material):
            self._Mat = Mat
            self.Color = Mat.Color
            self.FallB = Mat.FallB
            self.Velocity = 0

    def RmvMaterial(self):
            self._Mat = None
            self.Color = WHITE
            self.FallB = None
            self.Velocity = 0

    def MoveDown(self):

        if not self._Mat or not self.FallB:
            return
        
        current_row += 1 





class Window:
    def __init__(self):
        pygame.init()
        self.WIDTH: int = WIDTH
        self.HEIGHT: int = HEIGHT
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.TITLE = pygame.display.set_caption("Pixel Game")
        self.running = True
        self.Clock = pygame.time.Clock()
        self.tick = 0
        self.grid = Grid(5, self.tick)  # init Grid
        self.Leftmouse_down = False
        self.Rightmouse_down = False
        self.SCREEN.fill(WHITE)
        AddMaterial2List(Material("Sand", SKIN, 50, True))


    def start(self):
        while self.running:
            self.GameLoop()

    def LeftMouseDown(self):
        if self.Leftmouse_down:
            MouseX, MouseY = self.GetMouseCords()
            if MouseX != None or MouseY != None:
                particle = self.grid.get_particle_at(MouseX, MouseY)

                particle.AddMaterial(Materials[0])

    def RightMouseDown(self):
        if self.Rightmouse_down:
                MouseX, MouseY = self.GetMouseCords()
                if MouseX != None or MouseY != None:
                    particle = self.grid.get_particle_at(MouseX, MouseY)
                    if particle != None:
                        particle.RmvMaterial()
    
    def GetMouseCords(self):
        x, y = pygame.mouse.get_pos()


        while x < 0 or y < 0:
            if x > 0 or y > 0:
                return None, None
            else:
                time.sleep(1)
                continue
        return x, y
    
    def GameLoop(self):

        for event in pygame.event.get():
            self.tick = self.Clock.tick(FPS)
            match event.type:
                case pygame.QUIT:
                    self.running = False
                case pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        self.Leftmouse_down = True
                    if event.button == 3:
                        self.Rightmouse_down = True
                case pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.Leftmouse_down = False
                    if event.button == 3:
                        self.Rightmouse_down = False
                

            
            self.RightMouseDown()
            self.LeftMouseDown()
                


            self.grid.draw(self.SCREEN)
            pygame.display.update()




class Grid:
    def __init__(self, Cell_size: int, dt):
        self.CELL_SIZE = Cell_size
        self.HEIGHT = HEIGHT / self.CELL_SIZE
        self.WIDTH = WIDTH / self.CELL_SIZE
        self.COLOR = WHITE
        self.Cords = []
        self.dt = dt

        for row in range(0, WIDTH, self.CELL_SIZE):
            for column in range(0, HEIGHT, self.CELL_SIZE):
                Cell = Particles(row, column, WHITE, self.dt)
                self.Cords.append(Cell)


    
    def draw_circle(self, center_x, center_y, radius, material):
        ... 

    def draw(self, screen):
        for cells in self.Cords:
            pygame.draw.rect(
                screen,
                cells.Color,
                (cells.X, cells.Y, self.CELL_SIZE, self.CELL_SIZE),
                0,
            )

    def get_particle_at(self, x, y):
        grid_x = (x // self.CELL_SIZE) * self.CELL_SIZE
        grid_y = (y // self.CELL_SIZE) * self.CELL_SIZE
        for particle in self.Cords:
            if particle.X == grid_x and particle.Y == grid_y:
                return particle
        return None, None

 