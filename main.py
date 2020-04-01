import pygame 
from Cell import Cell
import colors
pygame.init()


# window variables, +1 for bottom and right border
win_width=500+1     
win_height= 500+1
win = pygame.display.set_mode((win_width, win_height))


# grid
cell_width = 20
cols = win_width//cell_width
rows = win_height//cell_width
cell_border_width = 1

all_cells = [] # [cols][rows]
count = 1

# creating grid
for i in range(cols):
    col= []
    count+=1
    for j in range(rows):
        cell = Cell(i*cell_width, j*cell_width, cell_width, colors.Blue, colors.Red)
        col.append(cell)
    all_cells.append(col)


run = True
while run:
    # win.fill(colors.Blue)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
    for i in range(rows):
        for j  in range(cols):
            all_cells[j][i].show(win)

    pygame.display.update()