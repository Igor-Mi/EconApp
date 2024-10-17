import pygame
from Objects.Dummy import *
import math
class Point:
    def set():
        Point._vline=pygame.image.load("./Textures/Vline.png").convert_alpha()
        Point._hline=pygame.image.load("./Textures/Hline.png").convert_alpha()
    
    def __init__(self, screen, line1, line2, label1, label2):
        self._screen=screen
        self._line1=line1
        self._line2=line2
        self._label1=label1
        self._label2=label2
        self._fx = 75
        self._fy = screen.get_height()-75
        self._fcolour = (0,0,0)
        self._fsize = 20
        self._label="text"
        
    def set_vars(self,line1, line2, label1, label2):
        self._line1=line1
        self._line2=line2
        self._label1=label1
        self._label2=label2
    def get_vars(self):
        return [self._line1,self._line2,self._label1,self._label2]
    def get_label(self):
        return [self._label,self._fx,self._fy]
        
    def set_label(self,label,x,y):
        self._label=label
        self._fx=x
        self._fy=y
        
    def simple(line1,line2):#finds the intersection of 2 lines that are not rotated
        stat1=line1.stats()#saves information about the first line
        stat2=line2.stats()#saves information about the second line

        #finds where the domains intersect
        l=max(stat1[0],stat2[0]);#picks the right most left side 
        r=min(stat1[0]+stat1[2],stat2[0]+stat2[2]);#pick the left most right side
        
        if(l<=r):#checks if the domains actually intersect
            dif=(r-l)/6# divides the intersection into 6 pieces
            
            for i in range(6):#goes over those pieces
                left=l+dif*i#makes a left bound for the piece
                right=l+dif*(i+1)#makes a right bound for the piece
                
                while(right-left>0.05):#keeps running ternary search until the x is determined upto a 0.05 range
                    mid1=left+(right-left)/3#the x value bettwen the 1st and 2nd third
                    mid2=right-(right-left)/3#the x value bettwen the 2nd and 3rd third
                    
                    value1=abs(line1.calc(mid1)-line2.calc(mid1))#find the y value at mid 1
                    value2=abs(line1.calc(mid2)-line2.calc(mid2))#finds the y value at mid 2
                    
                    if(value1==value2):#if they are equal
                        #the minimum must be in the second third 
                        left=mid1
                        right=mid2
                    elif(value1>value2):#if value 1 is bigger
                        #the minimum cannot be in the first third 
                        left=mid1
                    else:#if value 2 is bigger
                        #the minimum cannot be in the third third
                        right=mid2
                
                x=(left+right)/2#the final x value is set to the middle of the range
                if(abs(line1.calc(x)-line2.calc(x))<0.5):#if the diffrence bettwen the y values of the functions is small
                    return x;#the x value is returned
    
    def intersect(self):#can find an instersection bettwen 2 lines that are rotated
        line1 = self._line1#shortens the name for the sake of simplicty 
        line2 = self._line2#shortens the name for the sake of simplicty 
        og = line2.stats()#saves the orginal line 2 information
        stat1 = line1.stats()#saves information about the first line
        stat2 = line2.stats()#saves information about the second line
        
        stat2[0],stat2[1]=Dummy.turn(stat2[0]+stat2[5][0],
                                     self._screen.get_height()-(stat2[1]+stat2[5][1]),
                                     stat1[0]+stat1[5][0],#gets how much the postion of the image changes when
                                     self._screen.get_height()-(stat1[1]+stat1[5][0]),
                                     -(stat1[4]*math.pi/180))#rotating about the center of line 1
        
        stat2[4]-=stat1[4]#alters the absolute roation of line 2 by how much its roated round line 1
        line2.set_coords(og[0]+stat2[0],og[1]-stat2[1])#moves line 2 to its new corridnates temporarily
        line2.rotation(stat2[4])#roates line 2 to the correct spot 
        bounds=[100000,-100000]#sets up the edges for the roated graph
        
        for i in range(100):#takes 100 points on the line
            x=og[0]+stat2[0]+i*(stat2[2]/100)#find the x cordinate of the point when not rotated
            y=line2.calc(x)#finds the y cordinated when not rotated
            tmp=Dummy.turn(x,y,og[0]+stat2[0]+stat2[5][0]
                           ,self._screen.get_height()-(og[1]-stat2[1]+stat2[5][1])
                           ,(stat2[4]*math.pi/180))#rotates the x and y based on the image roation
            x+=tmp[0]#adjusts x
            y+=tmp[1]#adjusts y
            bounds[0]=min(bounds[0],x)#tries to determine the mnimum x value based on this point
            bounds[1]=max(bounds[1],x)#tries to determind the maximum x value based on this point
            
        def new_f(x):# adjusts the function of line 2 based on the rotation 
            ang=-stat2[4]*math.pi/180# turns the angle into radians 
            cox=og[0]+stat2[0]+stat2[5][0]#center of rotation x coordinates 
            coy=self._screen.get_height()-(og[1]-stat2[1]+stat2[5][1])#center of rotation y coordinates 
            y=line1.calc(x)#since we only need the intersetion we can subsitue the line1 equation for y

            inside_func=(x-cox)*math.cos(ang)-(y-coy)*math.sin(ang)#rotates x using complex numbers adjusting for a diffrent center 
            with_func=line2.calc(inside_func+cox)-coy# finds the left hand side of the equation when in the normal form
            y_sidexbit=(x-cox)*math.sin(ang)#finds the x bit on the y side (created because of the roation)
            y_constant=-coy*math.cos(ang)#finds the extar adjusting constant because of the shifted center 

            return (with_func-y_sidexbit-y_constant)/math.cos(ang)#returns the y value, when the equation is rearranged 
        
        l=max(stat1[0],bounds[0]);
        r=min(stat1[0]+stat1[2],bounds[1]);
        if(l<=r):
            dif=(r-l)/6
            for i in range(6):
                left=l+dif*i
                right=l+dif*(i+1)
                while(right-left>0.05):
                    mid1=left+(right-left)/3
                    mid2=right-(right-left)/3
                    value1=abs(line1.calc(mid1)-new_f(mid1))
                    value2=abs(line1.calc(mid2)-new_f(mid2))
                    if(value1==value2):
                        left=mid1
                        right=mid2
                    elif(value1>value2):
                        left=mid1
                    else:
                        right=mid2
                
                x=(left+right)/2
                if(abs(line1.calc(x)-new_f(x))<0.5):
                    line2.set_coords(og[0],og[1])#puts the line back into its correct place
                    line2.rotation(og[4])#roates the line back into the correct roation 
                    y=line1.calc(x)# finds y,
                    tmp=Dummy.turn(x,y,
                                   stat1[0]+stat1[5][0],#Rotates y and x because we found the intersection
                                   self._screen.get_height()-(stat1[1]+stat1[5][1]),
                                   (stat1[4]*math.pi/180))#when the whole graph was roated so line1 was a function
                    return [x+tmp[0],y+tmp[1]];#returns the adjusted value 
                
        line2.set_coords(og[0],og[1])
        line2.rotation(og[4])
            
              
    def draw(self,x,y):
        pygame.draw.rect(self._screen,(0,0,200),(x-10,y-10,20,20))
        mg=104
        if(self._label1!=""):
            font = pygame.font.SysFont("Arial", self._fsize)
            rend = font.render(self._label1,1,self._fcolour)
            rect=rend.get_rect(center = (self._fx,y))
            self._screen.blit(rend,rect)
            self._screen.blit(Point._hline.subsurface((0,0,x-mg,18)),(mg,y-9))
            
        if(self._label2!=""):
            font = pygame.font.SysFont("Arial", self._fsize)
            rend = font.render(self._label2,1,self._fcolour)
            rect=rend.get_rect(center = (x,self._fy))
            self._screen.blit(rend,rect)
            self._screen.blit(Point._vline.subsurface((0,0,18,self._screen.get_height()-(y+mg))),(x-9,y))
              

              
    def show(self):
        if(self._line1!=None and self._line2!=None):
            tmp=self.intersect()
            if(tmp!=None):
                tmp[1]=self._screen.get_height()-tmp[1]
                x,y=tmp
                self.draw(x,y)
                return [x,y]
        
        
        
        
    
        
        
    
