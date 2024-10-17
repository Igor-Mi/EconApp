import pygame
from Objects.Fline import *
from Objects.Point import *
class Tax:
    def __init__(self,screen,supply,demand,amount):
        self._supply=supply
        self._demand=demand
        self._aount=amount
        self._screen=screen
        self._newline=Fline(supply,amount,"Supply+Tax")
        self._point1=Point(screen,supply,demand,"","")
        self._point2=Point(screen,self._newline,demand,"P2","Qt")
        self._point3=Point(screen,None,None,"P1","")
        self._x1=0
        self._x2=0
        self._y1=0
        self._y2=0
        self._ymid=0
        self._flag=True
        self._label="text"
        self._fx=0
        self._fy=0
        
    def set_vars(self,supply,demand,amount,p1,p2,qt):
        self._supply=supply
        self._demand=demand
        self._aount=amount
        self._newline.set_vars(supply,amount,self._label)
        self._point1.set_vars(supply,demand,"","")
        self._point2.set_vars(self._newline,demand,p2,qt)
        self._point3.set_vars(None,None,p1,"")
    def get_vars(self):
        tmp1=self._point2.get_vars()
        tmp2=self._point3.get_vars()
        return [self._supply,self._demand,self._aount,tmp1[2],tmp2[2],tmp1[3]]
        
    def get_label(self):
        return [self._label,self._fx,self._fy]
        
    def set_label(self,label,x,y):
        self._label=label
        self._fx=x
        self._fy=y
        
    def set_a(self,amount):
        self._aount=amount
    def get_a(self):
        return self._aount
        
    def show(self):
        if(self._supply!=None and self._demand!=None):
            self._flag=True
            
            tmp=self._point1.intersect()
            if(tmp!=None):
                self._x1,self._ymid = tmp
                self._ymid=self._screen.get_height()-self._ymid
            else:
                self._flag=False
                
            tmp=self._point2.intersect()
            if(tmp!=None):
                self._x2,self._y2 = tmp
                self._y2=self._screen.get_height()-self._y2
                self._y1=self._screen.get_height()-(tmp[1]+self._aount)
            else:
                self._flag=False
                
            if(self._flag):
                t=0
                pygame.draw.rect(self._screen,(255,165,0),(104,min(self._y2,self._y1),self._x2-104,int(abs(self._y2-self._y1))))
                pygame.draw.polygon(self._screen,(0,150,150),((self._x2,self._y1),(self._x2,self._y2),(self._x1,self._ymid)))
            self._newline.show()
            self._supply.show()
            self._demand.show()
            if(self._flag):
                self._point2.draw(self._x2,self._y2)
                self._point3.draw(self._x2,self._y1)
