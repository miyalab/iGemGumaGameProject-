# iGemGumaGameProject-
Development of iGEM Gunma Cloud founding Game Project
import pygame
from pygame.locals import *
from pygame import Rect

import numpy as np
from random import randint
import os

debug = False # display map as text

TILE_W = 64
TILE_H = 64
TILE_ID_ROAD = 3
TILE_ID_GROUND = 2

class Map():
    """stores map info, and draws tiles.
    Map is stored as an array of int's which correspond to the tile id."""
    def __init__(self,game):
        """set default map"""
        self.game = game
        self.screen = game.screen
        
        self.scrolling = False
        
        self.load_tileset("TF01.PNG")
        
        #ともの素材にした

        self.reset()
        self.randomize()
        
        #スクロールの部分は消した
        
    def load_tileset(self, image="TF01.PNG"):        
        """load tileset image"""
        self.tileset = pygame.image.load(os.path.join("game_materials_tomo", image)).convert()
        self.rect = self.tileset.get_rect()
        
        #ともの素材が入ったフォルダ名を指定した

    def reset(self):
        """clear map, reset to defaults."""
        # calculate number of tiles to fill the screen
        
        """screen size:
        self.tiles_x = self.game.width / TILE_W
        self.tiles_y = self.game.height / TILE_H
        """
        # or fixed size
        self.tiles_x, self.tiles_y = 640, 480

        # create empty array, fill with zeros.                  array[tiles_x, tiles_y]
        self.tiles = np.zeros( (self.tiles_x, self.tiles_y ), dtype=int)        
        
        #if debug: print "\n-- self.tiles = --\n", self.tiles
        #この一行↑赤くなってたけど直し方わからないからとりあえずコメントアウトさせた
        
    def randomize(self):
        """sets tiles to random values"""
        self.offset = (-200, -200)
        # randomize all tiles
        for y in range(self.tiles_y):
            for x in range(self.tiles_x):
                    self.tiles[x,y] = randint(0,TILE_ID_GROUND)

        # example of 2d array slicing, ex: slicing whole column or row
        # set a couple roads: one horizontal, one vertical.
        self.tiles[1,:] = TILE_ID_ROAD
        self.tiles[:,2] = TILE_ID_ROAD
        #if debug: print "\n-- self.tiles = --\n", self.tiles
        #この一行↑赤くなってたけど直し方わからないからとりあえずコメントアウトさせた    

    def draw(self):
        # loop all tiles, and draw        
        for y in range( self.tiles_y ):
                for x in range( self.tiles_x ):
                    # draw tile at (x,y)
                    id = self.tiles[x,y]

                    # get rect() to draw only tile from the tileset that we want
                    dest = Rect( x * TILE_W, y * TILE_H, TILE_W, TILE_H )
                    src = Rect( id * TILE_W, 0, TILE_W, TILE_H )

                    # note, for scrolling tiles, uncomment:
                   # if self.scrolling:
                    #    dest.left += self.offset[0]
                     #   dest.top += self.offset[1]                        

                    #self.screen.blit( self.tileset, dest, src )
 #↑とりあえずコメントアウトさせた                   
                    
        #こういうコードがあると練習問題みたいでいいな

