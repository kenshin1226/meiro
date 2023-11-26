import pygame
from pygame.locals import *
import sys
import random
def main():
    pygame.init()                                 # Pygameの初期化
    x=0
    y=0
    while True:
        r=random.randint(1,2)
        if r==1:
            x=x+1
        elif r==2:
            y=y+1 
        print(x,y)
        if x==5:
            break