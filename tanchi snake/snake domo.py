#-*- codeing = utf-8 -*-
#@Time : 2020/6/28 16:16
#@Author : 许鑫
#@File : snake domo.py
#@Software : PyCharm

import pygame, sys, random
# 这个模块包含所有pygame所使用的常亮
from pygame.locals import *

import sys,random,pygame,time

from pygame.locals import *

black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)

def main():
    pygame.init()
    fpsClock = pygame.time.Clock()
    playerSurface = pygame.display.set_mode((640,480))
    pygame.display.set_caption('贪吃蛇')
    snakePositon = [100,100]
    snakelength = [[100,100],[100,80],[100,60]]
    award = [300,300]
    award_dec = 1
    derection = "right"
    changeDerection = derection

    while True:
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()

            # 绘制画面
            for positon in snakelength:
                pygame.draw.rect(playerSurface,white,Rect(positon[0],positon[1],20,20))
            pygame.draw.rect(playerSurface,white,Rect(award[0],award[1],20,20))
            pygame.display.flip()
            fpsClock.tick(5)




if __name__ == '__main__':
    main()