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
cell_width = 70
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


# Current Cell
'''
active cell -> purple color
visited cell -> OrangeRed
unvisited cell -> black
'''
current_cell = all_cells[1][4]
current_cell.visited = True
current_cell.fill_color = colors.Purple
next_cell = None

def FindNextCell() -> Cell:
    global current_cell, next_cell
    row = current_cell.row_index # i -> cols
    col = current_cell.col_index # j -> rows

    # get all neighbors of current cell
    Neighbors =  current_cell.neighbors(all_cells, row, col)

    # choose random neighbor        
    if len(Neighbors):
        random_neighbor = random.choice(Neighbors)
        next_cell = random_neighbor
    
        # removing wall
        current_cell.remove_wall_between(next_cell)

        # modifying cell status
        current_cell.visited = True
        current_cell.fill_color = colors.OrangeRed

        current_cell = next_cell
        current_cell.fill_color = colors.Purple


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
    pygame.time.wait(300)
    FindNextCell()

    pygame.display.update()