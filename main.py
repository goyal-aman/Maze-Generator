import pygame 
from Cell import Cell
import colors
pygame.init()


# window variables
win_width=500
win_height= 500
win = pygame.display.set_mode((win_width, win_height))


# grid
cell_width = 25
cols = win_width//cell_width
rows = win_height//cell_width
cell_border_width = 1
margin_col = cell_border_width/cols
margin_row = cell_border_width/rows

# Creating Grid
all_cells = []
for i in range(cols):
    col = []
    for j in range(rows):
        cell = Cell(i*(cell_width-margin_col), j*(cell_width-margin_row), cell_width, colors.Blue, colors.Red)
        col.append(cell)
    all_cells.append(col)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
    
    for i in range(rows):
        for j  in range(cols):
            all_cells[i][j].show(win)

    pygame.display.update()