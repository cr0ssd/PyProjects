from gridworld.grid import Grid
import pygame

myimage = pygame.image.load("car.png")

def draw_car(grid, cell_dimensions):
    grid.screen.blit(myimage, cell_dimensions)

grid = Grid(3, 3, 90, 90, title='Tic Tac Toe', margin=1)
grid.set_drawaction('O', draw_car)

grid[1,1] = 'O'
grid.run()

maxx = 5
maxy = 5
x = maxx // 2
y = maxy // 2

grid = Grid(maxx, maxy, 90, 90, title='Gridworld', margin=1)

def key_action(key):    
    global x, y
    oldx, oldy = x, y
    if key == pygame.K_LEFT and x > 0:
        x = x - 1
    grid[oldx, oldy] = ''
    grid[x, y] = 'O'

grid.set_key_action(key_action) 