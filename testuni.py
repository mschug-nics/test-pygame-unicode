# -*- coding: utf-8 -*-
# Uses example code from: http://stackoverflow.com/questions/34032668/pygame-reading-font-from-a-file-error
# 
import pygame
import sys
import random
from datetime import datetime

random.seed(datetime.now())

class Coords:
    def __init__(self,x,y):
        self.x = x
        self.y = y


coords = Coords(random.randint(0,500-64), 500/2-32)

mykeys = {
    pygame.K_w: lambda: print("k"),
    pygame.K_s: lambda: print("s"),
    pygame.K_a: lambda: (setattr(coords,'y',0),setattr(coords,'x',random.randint(0,500-64))),
    pygame.K_ESCAPE: lambda: pygame.quit() & sys.exit()
}

unistr = "演"
pygame.font.init()
srf = pygame.display.set_mode((500,500))
f = pygame.font.Font("wts11.ttf",64)
srf.blit(f.render(unistr,True,(255,255,255)),(coords.x,coords.y))
pygame.display.flip()
pygame.time.Clock().tick(30)

while True:
    coords.y = coords.y + 0.01
    srf.fill((0,0,0))
    srf.blit(f.render(unistr,True,(255,255,255)),(coords.x,coords.y))
    pygame.display.flip()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.KEYDOWN:
            #if e.key == pygame.K_w:
            func = mykeys.get(e.key,lambda:print("No such key."))
            func()
