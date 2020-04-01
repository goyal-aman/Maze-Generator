import pygame
import colors
from typing import List

class Cell:
    '''

    A()         B()


    D()         C()

    '''
    def __init__(self, i, j, width, fill_color, border_color, border_width=1):
        self.i              = i # x pixel
        self.j              = j # y pixel
        self.width          = width
        self.fill_color     = fill_color
        self.border_color   = border_color
        self.border_width   = border_width
        self.row_index      = j//width
        self.col_index      = i//width

        self.visited = False
        
        # Cell Coords
        self.A              = (i,       j)
        self.B              = (i+width-border_width, j)
        self.C              = (i+width-border_width, j+width-border_width)
        self.D              = (i,       j+width-border_width)

        # Cell Border
        self.top_boder      = True
        self.bottom_border  =  True
        self.left_border    = True
        self.right_border   = True


    def show(self, screen):

        # Rect
        pygame.draw.rect(screen, self.fill_color, (self.i, self.j, self.width, self.width))

        # border
        if self.top_boder:
            pygame.draw.line(screen, self.border_color, self.A, self.B, 2) # topline
        if self.right_border:
            pygame.draw.line(screen, self.border_color, self.B, self.C, 2) # right line
        if self.bottom_border:
            pygame.draw.line(screen, self.border_color, self.C, self.D, 2) # bottom line
        if self.left_border:
            pygame.draw.line(screen, self.border_color, self.D, self.A, 2) # leftline

    def neighbors(self,grid:List[List], row_index:int, col_index:int) -> List:
        '''
        @param:
        -grid -> grid of all the cells
        -row_index, col_index -> row, col index of current cell
        
        @algorithm:
        -> find left, right, top, bottom neighbor of current cell
        -> for each neighbor, if they have not visited, add them to Neighbors List

        @return : Neighbors (list)
        '''
        Neighbors = []
        rows = len(grid)
        cols = len(grid[0])
        
        if col_index-1>=0: # left neighbor
            left_neighbor = grid[row_index][col_index-1]
            if left_neighbor.visited==False:
                Neighbors.append(left_neighbor)
    
        if col_index+1<cols:
            right_neighbor = grid[row_index][col_index+1]
            if right_neighbor.visited == False:
                Neighbors.append(right_neighbor)
        
        if row_index+1<rows: # bottom_neighbor
            bottom_neighbor = grid[row_index+1][col_index]
            if bottom_neighbor.visited == False:
                Neighbors.append(bottom_neighbor)
        
        if row_index-1>=0: # top neighbor
            top_neighbor = grid[row_index-1][col_index] 
            if top_neighbor.visited == False:
                Neighbors.append(top_neighbor)
        return Neighbors

    def remove_wall_between(self,next_cell):
        # next cell to the right
        if next_cell.col_index-self.col_index>=1:
            print('moving right')
            self.right_border = False
            next_cell.left_border = False
        
        # if next cell is to the left
        if next_cell.col_index-self.col_index<=-1:
            self.left_border = False
            next_cell.right_border = False

        # if next cell is to top
        if next_cell.row_index - self.row_index <= -1:
            self.top_boder = False
            next_cell.bottom_border = False
        
        # if next cell is to bottom
        if next_cell.row_index-self.row_index>=1:
            self.bottom_border = False
            next_cell.top_boder =False
