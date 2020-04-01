import pygame 
from Cell import Cell
import random
import colors
pygame.init()

# window variables, +1 for bottom and right border
win_width   = 500+1     
win_height  = 500+1
win = pygame.display.set_mode((win_width, win_height))


# grid
cell_width = 20
cols = win_width//cell_width
rows = win_height//cell_width
cell_border_width = 1

all_cells = [] # [cols][rows]
count = 1

# creating grid
'''
grid[row][col]
 
j->row
i->col
'''
for j in range(rows):
    col= []
    count+=1
    for i in range(cols):
        cell = Cell(i*cell_width, j*cell_width, cell_width, colors.Black, colors.White)
        col.append(cell)
    all_cells.append(col)


run = True
while run:
    # win.fill(colors.Blue)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    # Printing Grid
    for j in range(rows):
        for i  in range(cols):
            all_cells[i][j].show(win)
            # if all_cells[i][j].fill_color == colors.Purple:
                # print(i,j)

    pygame.display.update()