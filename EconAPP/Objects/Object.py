import pygame
class Object:
    def set_screen(display,new):#determines which display to write to for all object
        Object._display = display
        Object._dowidth = display.get_width()
        Object._doheight = display.get_height()
        Object._new=new
        
    def Pscreen(self,display,new):#determines which display to write to for this object
        self._display = display
        self._dowidth = display.get_width()
        self._doheight = display.get_height()
        self._new=new
    def set_tex(self,texture):
        self._texture=texture
    def __init__(self,x,y,width,height,texture,text):#sets up defult parameters
        #basic variables
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        if(texture!=None):
            self._texture = pygame.transform.scale(pygame.image.load(texture).convert_alpha(),(width,height))
        self._text = text

        #font variables
        self._fx = 0
        self._fy = 0
        self._fcolour = (0,0,0)
        self._fsize = 100

        #display related variables
        self._display=Object._display
        self._dowidth = Object._display.get_width()
        self._doheight = Object._display.get_height()
        self._new=Object._new #new size of the screen
        self._shift=[0,0]#shift of the object, which is quicker than move in some cases
        
    def move(self,x,y):#moves object
        self._x = x
        self._y = y
        
    def get(self):#gets the x and y positon
        return [self._x,self._y]
    
    def show(self):#draws object ot the screen
        #draws to the screen
        self._display.blit(self._texture, (self._x+self._shift[0], self._y+self._shift[1]))
        
        #draws label if its not empty
        if(self._text!=""):
            self.draw_text(self._display,self._text,self._fcolour,self._fsize,(self._fx+self._x+self._shift[0]),(self._fy+self._y+self._shift[1]))
            
    def draw_text(self,screen,text,colour,size,x,y):
        font = pygame.font.SysFont("Arial", size)
        rend = font.render(text,1,colour)
        screen.blit(rend,(x,y))
            
    def IsHoverOver(self,pos):#checks if the positon at pos is in the object
        #the rescaling ratios
        xratio = self._new[0]/self._dowidth
        yratio = self._new[1]/self._doheight
        
        if((self._x+self._shift[0])*xratio<=pos[0] and pos[0]<=(self._x+self._width+self._shift[0])*xratio):
            if((self._y+self._shift[1])*yratio<=pos[1] and pos[1]<=(self._y+self._height+self._shift[1])*yratio):
                return True
        return False
    
    def setFont(self,colour, x, y, size):# writes text
        self._fx = x
        self._fy = y
        self._fcolour = colour
        self._fsize = size
        
    def set_text(self,text):
        self._text=text
        
                    
    def shift(self,x):#sets the shifts
        self._shift=x

