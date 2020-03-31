import pygame 
from Cell import Cell
import colors
pygame.init()


# window variables
win_width=500
win_height= 500
win = pygame.display.set_mode((win_width, win_height))



run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
    

    pygame.display.update()