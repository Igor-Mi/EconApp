import pygame
import math
class Fline:
    def __init__(self,line,shift,label):
        self._line=line
        self._shift=shift
        self._label=label
    def set_vars(self,line,shift,label):
        self._line=line
        self._shift=shift
        self._label=label
        
        
    def set_center(self,center):
        self._line.set_center(center)
        
    def rotation(self,rot):
        self._line.rotation(rot)
        
    def stats(self):
        self._line.move(0,self._shift)
        tmp = self._line.stats()
        self._line.move(0,-self._shift)
        return tmp
        
    def show(self):
        self._line.move(0,self._shift)
        tmp=self._line.get_label()
        self._line.set_label(self._label,tmp[1],tmp[2])
        self._line.show()
        self._line.set_label(tmp[0],tmp[1],tmp[2])
        self._line.move(0,-self._shift)
        
    def actual_width(self):
        self._line.move(0,self._shift)
        tmp = self._line.actual_width()
        self._line.move(0,-self._shift)
        return tmp
    def calc(self,x):
        self._line.move(0,self._shift)
        tmp = self._line.calc(x)
        self._line.move(0,-self._shift)
        return tmp
        
    def id(self,screen,iden):
        self._line.id(screen,iden)
        
    def move(self,x,y):
        self._line.move(x,y)
    def set_coords(self,x,y):
        self._line.set_coords(x,y)

        
        
    
