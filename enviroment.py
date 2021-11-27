

import numpy as np
import pygame as pg

class Environment():
    
    def __init__(self, waitTime):
        
        self.width = 880
        self.height = 880
        self.nRows = 10
        self.nColumns = 10
        self.initSnakelen = 2
        self.defReward = -0.03
        self.negReward = -1.
        self.posReward = 2.
        self.waitTime = waitTime
        
        
        if self.initSnakelen > self.nRows / 2:
            self.initSnakelen = int(self.nRows / 2)
            
        self.screen = pg.display.set_mode((self.width, self.height))
        
        self.snakePos = list()
        self.screenMap = np.zeros((self.nRows, self.nColumns))
        
        for i in range (self.initSnakelen):
            self.snakePos.append((int(self.nRows / 2) + i, int(self.nColumns / 2)))
            self.screenMap[int(self.nRows / 2) + i][int(self.nColumns / 2)] = 0.5
            
        self.applePos = self.placeApple()
        
        self.drawSrceen()
        self.collected = False
        
        self.lastMove = 0
        
    def placeApple(self):
        posx = np.random.randint(0, self.nColumns)
        posy = np.random.randint(0, self.nRows)
        while self.screenMap[posy][posx] == 0.5:
            posx = np.random.randint(0, self.nColumns)
            posy = np.random.randint(0, self.nColumns)
            
        