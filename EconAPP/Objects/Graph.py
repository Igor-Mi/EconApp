import pygame
from Objects.Object import *
from Objects.Line import *
from Objects.Dummy import *
from Objects.Point import *
from Doubly_Linked_list import *
from Objects.Tax import *
class Graph(Object):#sets up all the variables
    def __init__(self,x,y,width,height,colour,texture,text):
        Object.__init__(self,x,y,width,height,texture,text)#Uses parent's initalizer
        self._entities=Dlist()
        self._colour=colour
        self._MainScreen=pygame.Surface((width,height))
        self._BackScreen=pygame.Surface((width,height))
        self._id=1;
        self._current=None
        self._prev=None
        self._pressed=False
        self._prev_pos=[0,0]
        self._lineT=Dummy(0,0,self._MainScreen,lambda x: height-x)
        self._lineF=Dummy(0,0,self._MainScreen,lambda x: x+height-500)
        self._xlabel="Quanity"
        self._ylabel="Price"
        self._fsize=38
        
    def set_xlabel(self,label):
        self._xlabel=label

    def set_ylabel(self,label):
        self._ylabel=label
        
    def show(self):#renders the graph to the screen
        self._MainScreen.fill((255,255,255,255))#colours the main graph screen blank
        self._MainScreen.blit(self._texture,(0,0))#renders the graph texture to the main graph screen
        self._BackScreen.fill((0,0,0))#colours the back screen blank
        self._entities.reset()#resets the Doubly linked list
        while(self._entities.get()!=None):#sees if it can still access an entity
            self._entities.get().value.show()#shows the entity
            self._entities.next()#moves on to the next entity
            
        self.draw_text_back(self._MainScreen,self._xlabel,self._fcolour,self._fsize,930,800)#draws the y axis label
        self.draw_text(self._MainScreen,self._ylabel,self._fcolour,self._fsize,20,5)#draw the x axis label
        self._display.blit(self._MainScreen,(self._x,self._y))#redners the main graph screen to the actual screen
        
    def hold(self):
        return self._current

    def get_list(self):
        return self._entities
    
    def correct(self,pos):
        xratio = self._dowidth/self._new[0]
        yratio = self._doheight/self._new[1]
        return [pos[0]*xratio-self._x, pos[1]*yratio-self._y]
        
        
        
    def CheckPress(self,pos,press):#checks which entity has been pressed in the screen
        if(press and self.IsHoverOver(pos)):#checks if the button is pressed and the press is on the graph
            self._pressed=True#sets its internal pressed variable to true
            PointCoords = self.correct(pos)#adjusts the cursor for screen rescaling
            self._prev_pos=PointCoords#stores where the click on the screen was
            colour=self._BackScreen.get_at((int(PointCoords[0]),int(PointCoords[1])))#gets the colour of the pixel currently being touched
            num = colour[0]*256*256+colour[1]*256+colour[2]#changes the colour into an ID
            
            if(num!=0):#if the ID isn't 0 (0 is the ID for nothing)
                self._current=self._entities.ret(num).value#it changes the current object to the object being touched
                
        else:#if the press conditons are not satisfied 
            self._pressed=False#it sets its internal pressed varible to false
            
    def set(self,new):
        self._current=new
        
    def reset(self):
        self._current=None
                    
    def run(self,pos):
        if(self._pressed):
            Coords=self.correct(pos)
            if(str(type(self._current))=="<class 'Objects.Line.Line'>"):
                x=Coords[0]-self._prev_pos[0]
                y=Coords[1]-self._prev_pos[1]
                self._current.move(x,y)
                self._prev_pos=Coords
    def draw_text_back(self,screen,text,colour,size,x,y):
        font = pygame.font.SysFont("Arial", size)
        rend = font.render(text,1,colour)
        screen.blit(rend,(x-rend.get_width(),y-rend.get_height()))
        
    def add_line(self,tex1,tex2,equation,x,y,hx,hy,check,label,fx,fy):
        self._entities.add(Line(0,0,hx,hy,tex1,tex2,self._MainScreen,self._BackScreen,equation,self._id,check),self._id)
        l1=self._entities.ret(self._id).value
        if(check):
            line=self._lineT
        else:
            line=self._lineF
        nx=Point.simple(l1,line)
        tmp=[nx,self._MainScreen.get_height()-l1.calc(nx)]
        l1.move(x,y)
        l1.set_center(tmp)
        l1.set_label(label,fx,fy)
        self._id+=1
        
    def add_point(self,label1,label2,label):
        point=Point(self._MainScreen,None,None,label1,label2)
        tmp=point.get_label()
        point.set_label(label,tmp[1],tmp[2])
        self._entities.add(point,self._id)
        self._id+=1
    def add_tax(self,amount,label):
        tax=Tax(self._MainScreen,None,None,amount)
        tmp=tax.get_label()
        tax.set_label(label,tmp[1],tmp[2])
        self._entities.add(tax,self._id)
        self._id+=1
    def save(self,name):
        pygame.image.save(self._MainScreen, name+".jpg")
    def get_dlist(self):
        return self._entities
    def special(self):
        typ=str(type(self._current))
        change=self._prev!=self._current
        self._prev=self._current
        if(typ=="<class 'Objects.Line.Line'>"):
            return ["Line",change]
        elif(typ=="<class 'Objects.Point.Point'>"):
            return ["Point",change]
        elif(typ=="<class 'Objects.Tax.Tax'>"):
            if(self._current.get_a()<0):
                return ["Tax",change]
            else:
                return ["Subsidy",change]
        else:
            return ["Nothing",change]
        
    #def Remove(entity):
