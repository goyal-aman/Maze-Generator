import pygame

class Cell:
    '''
    @param:
    i -> row
    j -> col
    '''
    def __init__(self, i:int, j:int, width:int, fill_color=None, border_color=None):
        self.i            = i
        self.j            = j
        self.width        = width
        self.fill_color   = fill_color
        self.border_color = border_color 
        self.top_line     = [(i, j), (i+width, j)]
        self.right_line   = [(i+width, j),( i+width, j+width)]
        self.bottom_line  = [(i+width, j+width), (i, j+width)]
        self.left_line    = [(i, j+width),(i, j)]

    
    def show(self, screen):
        ''' 
        drawing react and then rendering lines to show border
        '''
        # rect
        pygame.draw.rect(screen, self.fill_color, (self.i, self.j, self.width, self.width) )
        
        # border lines
        pygame.draw.line(screen, self.border_color, self.top_line[0], self.top_line[1], 2)
        pygame.draw.line(screen, self.border_color, self.bottom_line[0], self.bottom_line[1] )
        pygame.draw.line(screen, self.border_color, self.left_line[0], self.left_line[1] )
        pygame.draw.line(screen, self.border_color, self.right_line[0], self.right_line[1] )
    
