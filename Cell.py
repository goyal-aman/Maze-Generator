import pygame

class Cell:
    '''

    A()         B()


    D()         C()

    '''
    def __init__(self, i, j, width, fill_color, border_color, border_width=1):
        self.i              = i
        self.j              = j
        self.width          = width
        self.fill_color     = fill_color
        self.border_color   = border_color
        self.border_width   = border_width
        
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

