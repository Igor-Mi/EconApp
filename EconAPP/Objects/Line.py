import pygame
import math
class Line:
    def __init__(self,x,y,hx,hy,look,HitBox,screen,back,equation,iden,check):
        self.checkE=check
        self._x=x
        self._y=y
        self._look=pygame.image.load(look).convert_alpha()
        tmp=pygame.image.load(HitBox).convert_alpha()
        self._HitBox=pygame.Surface((tmp.get_width()+hx,tmp.get_height()+hy), pygame.SRCALPHA)
        self._HitBox.blit(tmp,(hx,hy))
        self._VizBox=pygame.Surface((tmp.get_width()+hx,tmp.get_height()+hy), pygame.SRCALPHA)
        self._VizBox.blit(tmp,(hx,hy))
        self._screen=screen
        self._back=back
        self._center=[0,0]
        self.id(self._HitBox,iden)
        self.id(self._VizBox,256*200)
        self._vis=False;
        self._equation=equation
        self._rot=0
        self._ex=0
        self._ey=0
        self._label="text"
        self._fcolour = (0,0,0)
        self._fsize = 20
        self._fy=0
        self._fx=self._look.get_width()
    def set_center(self,center):
        self._center=center
        
    def get_label(self):
        return [self._label,self._fx,self._fy]
        
    def set_label(self,label,x,y):
        self._label=label
        self._fx=x
        self._fy=y
        
    def turn(x,y,cx,cy,rot):
        tmpc=[x-cx,y-cy]
        nx=(math.cos(rot)*tmpc[0]-math.sin(rot)*tmpc[1])
        ny=(math.sin(rot)*tmpc[0]+math.cos(rot)*tmpc[1])
        return [nx-x+cx,ny-y+cy]

        
    def rotation(self,rot):
        self._rot=rot
        rot*=-math.pi/180
        rx=self._look.get_width()/2
        ry=self._look.get_height()/2
        self._ex, self._ey = Line.turn(rx,ry,self._center[0],self._center[1],rot)
        
    def stats(self):
        return [self._x,self._y,self._look.get_width(),self._look.get_height(),self._rot,self._center]
    def show(self):
        d = Line.turn(self._fx,self._fy,self._center[0],self._center[1],self._rot*(-math.pi/180))
        rx=self._x+self._look.get_width()/2+self._ex
        ry=self._y+self._look.get_height()/2+self._ey
        tmp1=pygame.transform.rotate(self._HitBox,self._rot)
        rect = tmp1.get_rect(center = (rx,ry))
        self._back.blit(tmp1,rect)
        if(self._vis):
            tmp1=pygame.transform.rotate(self._VizBox,self._rot)
            rect = tmp1.get_rect(center = (rx,ry))
        
            self._screen.blit(tmp1,rect)
            
        tmp1=pygame.transform.rotate(self._look,self._rot)
        rect = tmp1.get_rect(center = (rx,ry))
        self._screen.blit(tmp1,rect)

        font = pygame.font.SysFont("Arial", self._fsize)
        rend = font.render(self._label,1,self._fcolour)
        self._screen.blit(rend,(d[0]+self._x+self._fx,d[1]+self._y+self._fy))
        
    def actual_width(self):
        rx=self._x+self._look.get_width()/2+self._ex
        ry=self._y+self._look.get_height()/2+self._ey
        tmp1=pygame.transform.rotate(self._look,self._rot)
        rect = tmp1.get_rect(center = (rx,ry))
        return [rect[0],rect[0]+rect[2]]
        
    def calc(self,x):
        return self._equation(x-self._x)+(self._screen.get_height()-(self._y+self._look.get_height()))

    def id(self,screen,iden):
        colour= (iden/(256*256),(iden/256)%256,iden%256)
        width, height = screen.get_size()
        for i in range(width):
            for j in range(height):
                new=screen.get_at((i,j));
                if(new[:3]==0,0,0):
                    new=(colour[0],colour[1],colour[2],new[3])
                    screen.set_at((i,j),new)
        
    def move(self,x,y):
        
        w1=self._screen.get_width()
        w2=self._look.get_width()
        
        self._x+=x
        self._x=max(self._x,-w2/4)
        self._x=min(self._x,w1-(w2*3)/4)

        h1=self._screen.get_height()
        h2=self._look.get_height()
        self._y+=y
        self._y=max(self._y,-h2/4)
        self._y=min(self._y,h1-(h2*3)/4)

    def set_coords(self,x,y):
        self._y=y
        self._x=x

        
        
    
