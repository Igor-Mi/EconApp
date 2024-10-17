import pygame
from Objects.Object import *
class Button(Object):#sets up all the variables
    def __init__(self,x,y,width,height,shift,texture,stexture,text,action):
        Object.__init__(self,x,y,width,height,texture,text)#Uses parent's initalizer
        self._action=action;
        self._pressed=False;
        self._pressed_shift=shift
        self._oy=self._fy;
        if(texture!=None):
            self._otexture=self._texture;#sets sup ogiginal button colour
        if(stexture!=None):
            self._stexture=pygame.transform.scale(pygame.image.load(stexture).convert_alpha(),(width,height))

    def setFont(self,colour, x, y, size):# writes text
        Object.setFont(self,colour, x, y, size)
        self._oy=y
        
    def set_tex(self,texture):
        self._texture=texture
        self._otexture=texture
        
    def set_stex(self,texture):
        self._stexture=texture
        
    def CheckPress(self,pos,press):#checks if there is a button pressed over the button
        if(press and self.IsHoverOver(pos)):
            self._pressed=True
            if(self._action!=None):
                return self._action()#runs the function of the button
        else:
            self._pressed=False
        return self._pressed
            
    def show(self):#shows the button depending on wheter it is pressed
        if(self._pressed):
            self._texture=self._stexture
            self._fy=self._oy+self._pressed_shift
        else:
            self._texture=self._otexture
            self._fy=self._oy
            
        Object.show(self)#uses the parent's show method
            

