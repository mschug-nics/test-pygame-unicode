# -*- coding: utf-8 -*-
# Uses example code from: http://stackoverflow.com/questions/34032668/pygame-reading-font-from-a-file-error
# 
import pygame
import sys


unistr = "演"
pygame.font.init()
srf = pygame.display.set_mode((500,500))
f = pygame.font.Font("wts11.ttf",64)
srf.blit(f.render(unistr,True,(255,255,255)),(500/2-32,500/2-32))
pygame.display.flip()

while True:
    srf.blit(f.render(unistr,True,(255,255,255)),(0,0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if e.type == pygame.KEYDOWN:
            
