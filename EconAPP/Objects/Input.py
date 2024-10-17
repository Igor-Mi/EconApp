import pygame
from Objects.Button import *
class Input(Button):
    def setKeyboard(key):
        Input._keyboard=key
        Input._pt=None
    def __init__(self,x,y,width,height,texture,text):#sets up defult parameters
        Button.__init__(self,x,y,width,height,0,texture,texture,text,None)
        self._interval=0
        self._flick=False
        self._aval=self._text      
    def CheckPress(self,PointCoords,press):
        Button.CheckPress(self,PointCoords,press)
        if(self._pressed==True):
            Input._pt=self
            Input._keyboard.flush()
            Input._keyboard.set(self._text)
            self._interval=0
            self._flick=False
        elif(press==True):
            if(Input._pt==self):
                Input._pt=None
            self._flick=False
    def show(self,show=True):
        if(Input._pt==self):
            ct=pygame.time.get_ticks()
            if(self._text!=Input._keyboard.ret()):
                self._flick=True
                self._interval=ct
                
            self._text=Input._keyboard.ret()
            
            if(ct-self._interval>500):
                self._flick^=1
                self._interval=ct
                
            if(self._flick):
                self._text+='|'
        self._aval=self._text
        if(show==True):
            Button.show(self)
        if(Input._pt==self):
            self._text=Input._keyboard.ret()
    def get_val(self):
        return self._text
    def get_text_val(self):
        return self._aval
            
        
        
        
        
