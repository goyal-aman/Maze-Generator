import pygame 
from Cell import Cell
import random
import colors
pygame.init()

# window variables, +1 for bottom and right border
win_width   = 700+1     
win_height  = 700+1
win = pygame.display.set_mode((win_width, win_height))


# grid
cell_width = 50
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


# stack
stack = []
max_stack_len = 0
final_cell = None

# Current Cell

'''
active cell -> purple color
visited cell -> OrangeRed
unvisited cell -> black
'''

startX = random.randint(0, cols-1)
startY = random.randint(0, rows-1)

current_cell = all_cells[startX][startY]
current_cell.visited = True
current_cell.fill_color = colors.Purple
stack.append(current_cell)
next_cell = None

def FindNextCell() -> Cell:
    global stack, current_cell, max_stack_len, startX, startY, final_cell

    # current_cell from prev cycle, making it orange
    current_cell.fill_color = colors.OrangeRed

    if len(stack)>max_stack_len:
        max_stack_len = len(stack)
        final_cell = current_cell
    if len(stack)>0:
        current_cell = stack.pop()
        current_cell.fill_color = colors.Purple

        row = current_cell.row_index # i -> cols
        col = current_cell.col_index # j -> rows
        
        # get neighbors of current cell
        Neighbors = current_cell.neighbors(all_cells, row, col)

        if len(Neighbors)>0:
            stack.append(current_cell)

             # choosing random neighbor
            next_cell = random.choice(Neighbors)

            # remove wall 
            current_cell.remove_wall_between(next_cell)

            #modifying cell status
            current_cell.fill_color = colors.OrangeRed
            next_cell.fill_color = colors.Purple

            next_cell.visited = True
            stack.append(next_cell)
    
    elif len(stack)==0:
        home_cell = all_cells[startX][startY]
        home_cell.fill_color = colors.LimeGreen
        final_cell.fill_color = colors.Red
    


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
    pygame.time.wait(90)
    FindNextCell()

    pygame.display.update()