import pygame
<<<<<<< HEAD
import sys
import time

window = pygame.display.set_mode((400,400))
o,oo = 200,200
s = pygame.Surface([o,oo])
x,y = 0,0
p = s.blit(pygame.image.load('S:/pygame/leftsit.png'),(x,y))
s = s.get_rect()
while 1:

    while True:
        try:
            event = next(iter(pygame.event.get()))
            if (event.type)==32787:
                pygame.quit()
                exit()
        except:
            break
    window.blit(s,(0,0))
    pygame.display.update()

=======
>>>>>>> 36d4c510ec930594b4677a1cc42194afa02bdbcd

