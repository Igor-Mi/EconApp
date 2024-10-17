import pygame
from Objects.Object import *
from Objects.Slider import *
from Objects.Button import *
class Menu(Object):#sets up all the variables
    def __init__(self,x,y,width,height, shift,texture,stexture,btexture1,btexture2,btexture3,text,bwidth):
        Object.__init__(self,x,y,width,height,texture,text)#Uses parent's initalizer
        self._sidebar=Slider(x+width-30,y,30,height,0,btexture1,btexture2,btexture3,"",None,40,True)
        self._buttons=[]#list of all buttons
        self._bwidth=bwidth#Button width
        self._btexture=pygame.transform.scale(pygame.image.load(texture).convert_alpha(),(self._width-30,self._bwidth))
        self._bstexture=pygame.transform.scale(pygame.image.load(stexture).convert_alpha(),(self._width-30,self._bwidth))
        self._screen=pygame.Surface((width-30,height))#surafce on which buttons in the menu are
        self._screen.fill((230,230,230))
        self._csize=[width,height]#current size of the menu
        self._slide=[0,0]#shift on the menu
        self._bshift=shift;
        
    def show(self):#displays the menu
        #works out the size of the rescaled menu size
        self._csize[0] = (self._width-30)*(self._new[0]/self._dowidth)
        self._csize[1] = (self._height)*(self._new[1]/self._doheight)
        
        self._sidebar.show()#shows the scroll bar
        
        for c in self._buttons:#shows all the buttons
            c.show()
            
        self._display.blit(self._screen,(self._x,self._y))#places the menu on the screen

    def CheckPress(self,pos,press):
        if(Object.IsHoverOver(self,pos) or not(press)):#makes sure interactions only happen in the menu
            self._sidebar.CheckPress(pos,press)#check is the sidebar is being held

            #workd out the scaling
            xratio = (self._new[0]/self._dowidth)
            yratio = (self._new[1]/self._doheight)
            
            for c in self._buttons:#checks if the buttons are pressed, it also adds a shift since the buttons start at (0,0)
                c.CheckPress((pos[0]-self._x*xratio,pos[1]-self._y*yratio),press)

    def updateMenu(self,pos,sc):#checks for bar slide
        self._sidebar.CheckSlide(pos)#slides the sidebar accordingly
        if(self.IsHoverOver(pos)):
            self._sidebar.scroll(sc)
        

        #shifts the buttons menu according to the slide 
        length=max(self._bwidth*len(self._buttons),self._height)-self._height
        self._slide[1]=-length*self._sidebar.getSlide()
            

    def add(self,text,action):#adds a button
        self._buttons.append(Button(0,self._bwidth*len(self._buttons),self._width-30,self._bwidth,self._bshift,None,None,text,action))#actually adds button to the array
        self._buttons[len(self._buttons)-1].set_tex(self._btexture)#sets the correct up button texture 
        self._buttons[len(self._buttons)-1].set_stex(self._bstexture)#sets the correct down button texture
        self._buttons[len(self._buttons)-1].Pscreen(self._screen,self._csize)#places it on the button surface
        self._buttons[len(self._buttons)-1].setFont(self._fcolour, self._fx, self._fy,self._fsize)#sets the font correctly 
        self._buttons[len(self._buttons)-1].shift(self._slide)#sets the shift when pressing to the class variable 

    def take_in_dlist(self,dlist,func):
        self._buttons=[]
        dlist.reset()
        while(dlist.get()!=None):
            tmp=dlist.get().value
            self.add(tmp.get_label()[0],func(tmp))
            dlist.next()
    def take_in_dlist_l(self,dlist,func):
        self._buttons=[]
        dlist.reset()
        while(dlist.get()!=None):
            tmp=dlist.get().value
            if(str(type(tmp))=="<class 'Objects.Line.Line'>"):
                self.add(tmp.get_label()[0],func(tmp))
            dlist.next()
    def update_dlist(self,dlist):
        dlist.reset()
        i=0
        while(dlist.get()!=None):
            tmp=dlist.get().value
            self._buttons[i].set_text(tmp.get_label()[0])
            i+=1
            dlist.next()
    def update_dlist_l(self,dlist):
        dlist.reset()
        i=0
        while(dlist.get()!=None):
            tmp=dlist.get().value
            if(str(type(tmp))=="<class 'Objects.Line.Line'>"):
                self._buttons[i].set_text(tmp.get_label()[0])
                i+=1
            dlist.next()
