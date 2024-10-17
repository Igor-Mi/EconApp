import pygame
from Objects.Line import *
class Dummy(Line):
    def __init__(self,x,y,screen,equation):
        self._x=x
        self._y=y
        self._screen=screen
        self._equation=equation
        self._look=screen
        self._rot=0
        self._center=[0,0]
