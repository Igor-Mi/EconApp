import pygame
from Objects.Button import *
class Slider(Button):#sets up all the variables
    def __init__(self,x,y,width,height,shift,texture,btexture,stexture,text,action,swidth,by,slide=0):
        Button.__init__(self,x,y,width,height,shift,texture,stexture,text,action)#Uses parent's initalizer
        self._PercentageSlid=slide
        self._swidth=swidth#width of the slider
        self._by=by#wheter the slider is veritical or not
        if(by):
            bwidth=width
            bheight=swidth
        else:
            bwidth=swidth
            bheight=height
        self._stexture=pygame.transform.scale(self._stexture,(bwidth,bheight))
        self._btexture=pygame.transform.scale(pygame.image.load(btexture).convert_alpha(),(bwidth,bheight))

        
    def CheckPress(self,pos,press):#checks if there is a button pressed over the button
        if(press and self.IsHoverOver(pos)):
            self._pressed=True
        else:
            self._pressed=False
            
    def CheckSlide(self,pos):#updates the slider when its being held
        if(self._pressed):
            #works out the percentage it has been slid depending on the slider width and orgientation
            if(self._by):
                yratio = self._new[1]/self._doheight
                rel_pos=pos[1]-(self._y+self._swidth/2)*yratio
                rel_pos=max(0,rel_pos)
                rel_pos=min((self._height-self._swidth)*yratio,rel_pos)
                self._PercentageSlid=(rel_pos/((self._height-self._swidth)*yratio))
            else:
                xratio = self._new[0]/self._dowidth
                rel_pos=pos[0]-(self._x+self._swidth/2)*xratio
                rel_pos=max(0,rel_pos)
                rel_pos=min((self._width-self._swidth)*xratio,rel_pos)
                self._PercentageSlid=(rel_pos/((self._width-self._swidth)*xratio))
                
            #performes the action with the precetnage slid
            if(self._action!=None):
                return self._action(self._PercentageSlid)

    
    def scroll(self,sc):
        prev=self._pressed
        self._pressed=True
        yratio = self._new[1]/self._doheight
        xratio = self._new[0]/self._dowidth
        tmp=[0,0]
        if(self._by):
            tmp[1]=self._PercentageSlid*((self._height-self._swidth)*yratio)
            tmp[1]+=(self._y+self._swidth/2)*yratio
        else:
            tmp[0]=self._PercentageSlid*((self._width-self._swidth)*xratio)
            tmp[0]+=(self._x+self._swidth/2)*xratio
        tmp[0]+=sc[0]
        tmp[1]+=sc[1]
        x=self.CheckSlide(tmp)
        self._pressed=prev
        return x
            
    def show(self):
        #shows the background of the slider
        Object.show(self)

        #checks wheter the slider is press
        if(self._pressed):
            tex=self._stexture
        else:
            tex=self._btexture
            
        #draws the slider depending on the rotaition
        if(self._by):
            y=self._y+self._PercentageSlid*(self._height-self._swidth)
            self._display.blit(tex, (self._x, y))
        else:
            x=self._x+self._PercentageSlid*(self._width-self._swidth)
            self._display.blit(tex, (x, self._y))

    def getSlide(self):#return the percantage slid
        return self._PercentageSlid
    def setSlide(self,slide):#return the percantage slid
        self._PercentageSlid=slide
        
