import pygame
from Objects.Object import *
from Objects.Menu import *
from Objects.Button import *

class Drop(Object):#sets up all the variables
    def __init__(self,x,y,width,height,texture,text,arr,mp=3):#initializer class
        Object.__init__(self,x,y,width,height,texture,text)#Uses parent's initalizer
        self._ret=None#sets the return value to none

        #Creates a menu
        self._drop_menu= Menu(x,y+height,width,height*mp+20,5,"./Textures/Button_up.png","./Textures/Button_down.png","./Textures/light_gray.png","./Textures/gray.png","./Textures/dark_gray.png","",height)
        self._drop_menu.setFont((0,0,0), 20, 10, 50)#sets the font
        
        self._dropped=False#starts the menu off as not not dropped

        #creates a drop down button
        self._drop_button=Button(x+width-30,y,30,height,0,"./Textures/Drop_up.png","./Textures/Drop_down.png","",None)

        self._types=arr#sets up an array for the drop down choices
        for i in range(len(self._types)):#for every choice
            self.create(self._types[i])#it adds it to the menu and array
            
    def setFont(self,colour, x, y, size):
        Object.setFont(self,colour, x, y, size)
        self._drop_menu.setFont(colour, x, y, size)
        
    def take_in_dlist(self,dlist,func):
        self._drop_menu.take_in_dlist_l(dlist,func)
    def update_dlist(self,dlist):
        self._drop_menu.update_dlist_l(dlist)
    def ret_set(self,string):
        self._ret=string
    def reset(self):
        self._ret=None
        self._dropped=False
    def create(self,string):
        self._drop_menu.add(str(string),lambda: self.ret_set(str(string)))
        
    def get_val(self):
        return self._ret
    
    def show(self):
        self.set_text(self._ret)
        if(self._ret==None):
            self.set_text("-Please choose-")
        Object.show(self)
        if(self._dropped):
            self._drop_menu.show()
        self._drop_button.show()
        
    def CheckPress(self,pos,press):
        self._dropped=self._dropped^self._drop_button.CheckPress(pos,press)
        if(self._dropped):
            self._drop_menu.CheckPress(pos,press)
        
    def updateDrop(self,pos,sc):
        if(self._dropped):
            self._drop_menu.updateMenu(pos,sc)
    
        

            

