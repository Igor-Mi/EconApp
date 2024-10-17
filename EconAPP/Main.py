import pygame
import math
import time  
from Objects.Object import *
from Objects.Button import *
from Objects.Graph import *
from Objects.Slider import *
from Objects.Menu import *
from Objects.Line import *
from Objects.Input import *
from Objects.Drop import *
from Keyboard import *
import sys
import os

def resource_path(relative_path):
    return os.path.join(os.path.dirname(sys.executable), relative_path)

#Main loop
pygame.init()#Initializes all of the pygame modules


pygame.display.set_caption("Econmics App")#Sets the name of the window to what is in teh brackets

display_width = 1600
display_height = 1000

display = pygame.display.set_mode((display_width/2,display_height/2),pygame.RESIZABLE)#Creates the display
draw_screen=pygame.Surface((display_width,display_height))
new=[display_width/2,display_height/2]
Object.set_screen(draw_screen,new)#sets up the display for objects
def elastic(score):
    return score
    
#Special objects
#nothing
Back=Object(1100,5,440,375,"./Textures/light_gray.png","")
#line
Line_name_label=Object(1110,20,0,0,"./Textures/light_gray.png","Name")
Line_name_label.setFont((0,0,0), 120, 0, 54)
Line_label=Input(1100,100,440,80,"./Textures/light_gray.png","")
Line_label.setFont((0,0,0), 5, 10, 54)
ElasticitySlider = Slider(1100,300,440,80,0,"./Textures/slide_back.png","./Textures/Slide_up.png","./Textures/Slide_down.png","Elasticity: 1",elastic,80,False,0.5)
ElasticitySlider.setFont((0,0,0), 80, -60, 54)

#point
Point_name_label=Object(1110,10,0,0,"./Textures/light_gray.png","Name")
Point_name_label.setFont((0,0,0), 155, 10, 24)
Point_label=Input(1100,60,440,60,"./Textures/light_gray.png","")
Point_label.setFont((0,0,0), 5, 15, 20)
Point_label1=Input(1100,140,200,60,"./Textures/light_gray.png","")
Point_label1.setFont((0,0,0), 5, 15, 20)
Point_label2=Input(1320,140,200,60,"./Textures/light_gray.png","")
Point_label2.setFont((0,0,0), 5, 15, 20)
Point_line1=Drop(1100,220,200,60,"./Textures/light_gray.png","",[],2)
Point_line1.setFont((0,0,0), 5, 15, 20)
Point_line2=Drop(1320,220,200,60,"./Textures/light_gray.png","",[],2)
Point_line2.setFont((0,0,0), 5, 15, 20)
Point_lines=[None,None]

def Point_add1(val):
    def tmp():
        Point_lines[0]=val
        Point_line1.ret_set(str(val.get_label()[0]))
    return tmp
def Point_add2(val):
    def tmp():
        Point_lines[1]=val
        Point_line2.ret_set(str(val.get_label()[0]))
    return tmp

#tax and subsidy
Tax_name_label=Object(1110,10,0,0,"./Textures/light_gray.png","Name")
Tax_name_label.setFont((0,0,0), 155, 10, 24)
Tax_label=Input(1100,60,440,60,"./Textures/light_gray.png","")
Tax_label.setFont((0,0,0), 5, 15, 20)
Tax_p1=Input(1100,140,125,60,"./Textures/light_gray.png","")
Tax_p1.setFont((0,0,0), 5, 15, 20)
Tax_p2=Input(1255,140,125,60,"./Textures/light_gray.png","")
Tax_p2.setFont((0,0,0), 5, 15, 20)
Tax_qt=Input(1410,140,125,60,"./Textures/light_gray.png","")
Tax_qt.setFont((0,0,0), 5, 15, 20)
Amount_Slider = Slider(1130,235,375,60,0,"./Textures/slide_back.png","./Textures/Slide_up.png","./Textures/Slide_down.png","Amount: 10",elastic,30,False,0.5)
Amount_Slider.setFont((0,0,0), 145, -25, 20)
Tax_line1=Drop(1100,300,200,50,"./Textures/light_gray.png","",[],1)
Tax_line1.setFont((0,0,0), 5, 15, 20)
Tax_line2=Drop(1330,300,200,50,"./Textures/light_gray.png","",[],1)
Tax_line2.setFont((0,0,0), 5, 15, 20)

Tax_lines=[None,None]#sets up the in main tax lines

def Tax_add1(val):#changes the tax supply line
    def tmp():
        Tax_lines[0]=val#sets the in main supply line
        Tax_line1.ret_set(str(val.get_label()[0]))#sets the label on the drop down menu
    return tmp#returns the function
def Tax_add2(val):#changes the tax demand line
    def tmp():
        Tax_lines[1]=val#sets the in main demand line
        Tax_line2.ret_set(str(val.get_label()[0]))#sets the label on the drop down menu
    return tmp#returns the function


#Main screen objects
MainKey=Keyboard()
Input.setKeyboard(MainKey)

AddObjectButton = Button(1216,400,200,60,0,"./Textures/AO_up.png","./Textures/AO_down.png","",None)
AddObjectButton.setFont((0,0,0), 16, 20, 64)

ObjectMenu = Menu(1100,480,460,460,5,"./Textures/Button_up.png","./Textures/Button_down.png","./Textures/light_gray.png","./Textures/gray.png","./Textures/dark_gray.png","",80)
ObjectMenu.setFont((0,0,0), 16, 8, 50)

Xlab = Input(720,770,250,60,"./Textures/Blue.png","Q")
Ylab = Input(30,20,250,60,"./Textures/blue.png","P")

TmpMenu = Object(200,100,1200,650,"./Textures/gray.png","")

TmpInput = Input(400,250,800,100,"./Textures/light_gray.png","")
TmpInput.setFont((0,0,0), 0, 16, 54)

TmpList = Drop(400,500,800,100,"./Textures/light_gray.png","",["Straight supply line","Straight demand line","Point","Tax","Subsidy","Quadratic supply line","Exponential supply line"])
TmpList.setFont((0,0,0), 0, 16, 54)

def addObject():
    name = TmpInput.get_val()
    types = TmpList.get_val()
    if(types=="Straight supply line"):
        MainGraph.add_line("./Textures/x.png","./Textures/back_x.png",lambda x: x,70,70,0,0,True,name,500,0)
    elif(types=="Straight demand line"):
        MainGraph.add_line("./Textures/500-x.png","./Textures/back_-x.png",lambda x: 500-x,98,98,0,0,False,name,500,500)
    elif(types=="Point"):
        MainGraph.add_point("P","Q",name)
    elif(types=="Tax"):
        MainGraph.add_tax(-50,name)
    elif(types=="Subsidy"):
        MainGraph.add_tax(50,name)
    elif(types=="Quadratic supply line"):
        MainGraph.add_line("./Textures/0.002x^2.png","./Textures/back_^2.png",lambda x: 0.002*x*x,98,98,20,20,True,name,500,0)
    elif(types=="Exponential supply line"):
        MainGraph.add_line("./Textures/1.0125^x.png","./Textures/back_^x.png",lambda x: pow(1.0125,x),20,20,20,20,True,name,500,0)
    return True
def change(val):
    return lambda: MainGraph.set(val)

TmpButton = Button(1230,650,150,75,0,"./Textures/Save_up.png","./Textures/Save_down.png","",addObject)

MainGraph = Graph(20,20,1060,820,(200,0,0),"./Textures/Graph_background.png","")

def save():
    #try:
    MainGraph.save(resource_path("Screenshots/Taken at "+str(int(time.time()))))
      #  t=0
    #except:
       # t=0
    
SaveButton = Button(20,860,220,120,0,"./Textures/Save_up.png","./Textures/Save_down.png","",save)
SaveButton.setFont((0,0,0), 10, 10, 82)


#variables for the latch
con=False
PointCoords=(0,0,0)
sc=[0,0]
Point.set()
main = True
while(True):#Main loop
    #board
    draw_screen.fill((255,255,255))
    new[0]=display.get_width()
    new[1]=display.get_height()

    current=MainGraph.hold()#get currently held item
    special=MainGraph.special()

    #this code is a latch so that buttons stop pressing properly 
    LeftMousePressed = pygame.mouse.get_pressed()[0]
    PointCoords = pygame.mouse.get_pos()
    if(LeftMousePressed and not con):#Code at the start of the press
        if(main):
            #main checks
            SaveButton.CheckPress(PointCoords,True)
            main = not(AddObjectButton.CheckPress(PointCoords,True))
            ObjectMenu.CheckPress(PointCoords,True)
            MainGraph.CheckPress(PointCoords,True)
            Xlab.CheckPress(PointCoords,True)
            Ylab.CheckPress(PointCoords,True)

            #Line
            if(special[0]=="Line"):
                ElasticitySlider.CheckPress(PointCoords,True)
                Line_label.CheckPress(PointCoords,True)
            #Point
            if(special[0]=="Point"):
                Point_label.CheckPress(PointCoords,True)
                Point_label1.CheckPress(PointCoords,True)
                Point_label2.CheckPress(PointCoords,True)
                Point_line1.CheckPress(PointCoords,True)
                Point_line2.CheckPress(PointCoords,True)
            
            #Tax and Subsidy
            if(special[0]=="Tax" or special[0]=="Subsidy"):
                Tax_label.CheckPress(PointCoords,True)
                Tax_p1.CheckPress(PointCoords,True)
                Tax_p2.CheckPress(PointCoords,True)
                Tax_qt.CheckPress(PointCoords,True)
                Amount_Slider.CheckPress(PointCoords,True)
                Tax_line1.CheckPress(PointCoords,True)
                Tax_line2.CheckPress(PointCoords,True)
            
        else:
            TmpList.CheckPress(PointCoords,True)
            TmpInput.CheckPress(PointCoords,True)
            main = TmpButton.CheckPress(PointCoords,True)
            if(main):
                ObjectMenu.take_in_dlist(MainGraph.get_dlist(),change)
                Point_line1.take_in_dlist(MainGraph.get_dlist(),Point_add1)
                Point_line2.take_in_dlist(MainGraph.get_dlist(),Point_add2)
                Tax_line1.take_in_dlist(MainGraph.get_dlist(),Tax_add1)
                Tax_line2.take_in_dlist(MainGraph.get_dlist(),Tax_add2)
                TmpList.reset()
                TmpInput.set_text("")
        con=True;
        
    if(con):
        if(not LeftMousePressed):#Code at the end of the press
            if(main):
                #Main checks
                SaveButton.CheckPress(PointCoords,False)
                AddObjectButton.CheckPress(PointCoords,False)
                ObjectMenu.CheckPress(PointCoords,False)
                MainGraph.CheckPress(PointCoords,False)
                Xlab.CheckPress(PointCoords,False)
                Ylab.CheckPress(PointCoords,False)

                #Line
                if(special[0]=="Line"):
                    ElasticitySlider.CheckPress(PointCoords,False)
                    Line_label.CheckPress(PointCoords,False)
                #Point
                if(special[0]=="Point"):
                    Point_label.CheckPress(PointCoords,False)
                    Point_label1.CheckPress(PointCoords,False)
                    Point_label2.CheckPress(PointCoords,False)
                    Point_line1.CheckPress(PointCoords,False)
                    Point_line2.CheckPress(PointCoords,False)
                
                #tax and subsidy
                if(special[0]=="Tax" or special[0]=="Subsidy"):
                    Tax_label.CheckPress(PointCoords,False)
                    Tax_p1.CheckPress(PointCoords,False)
                    Tax_p2.CheckPress(PointCoords,False)
                    Tax_qt.CheckPress(PointCoords,False)
                    Amount_Slider.CheckPress(PointCoords,False)
                    Tax_line1.CheckPress(PointCoords,False)
                    Tax_line2.CheckPress(PointCoords,False)
            else:
                TmpList.CheckPress(PointCoords,False)
                TmpInput.CheckPress(PointCoords,False)
                TmpButton.CheckPress(PointCoords,False)
            con=False;
        #Code during the press
        if(main):
            #line
            if(special[0]=="Line"):
                slide = ElasticitySlider.CheckSlide(PointCoords)
                
                if(slide!=None):
                    current.rotation((slide-0.5)*90)
                    if(current.checkE):
                        el=str(round(math.tan((1-slide)*(math.pi/2)),2))
                        if((1-slide)*(math.pi/2)>=math.pi/2):
                            el="∞"
                    else:
                        el=str(round(math.tan((slide)*(math.pi/2)),2))
                        if((slide)*(math.pi/2)>=math.pi/2):
                            el="∞"
                    ElasticitySlider.set_text("Elasticity: "+el)
            #tax
            if(special[0]=="Tax"):
                slide = Amount_Slider.CheckSlide(PointCoords)
                if(slide!=None):
                    current.set_a(slide*-100-0.001)
                    Amount_Slider.set_text("Amount: "+str(round(slide*100,2)))
            #subsidy
            if(special[0]=="Subsidy"):
                slide = Amount_Slider.CheckSlide(PointCoords)
                if(slide!=None):
                    current.set_a(slide*100+0.001)
                    Amount_Slider.set_text("Amount: "+str(round(slide*100,2)))
            MainGraph.run(PointCoords);
    #always runs
    #main
    if(main):
        ObjectMenu.updateMenu(PointCoords,sc)
        Point_line1.updateDrop(PointCoords,sc)
        Point_line2.updateDrop(PointCoords,sc)
        Tax_line1.updateDrop(PointCoords,sc)
        Tax_line2.updateDrop(PointCoords,sc)
    else:
        TmpList.updateDrop(PointCoords,sc)
    sc[0]=0
    sc[1]=0
    ObjectMenu.update_dlist(MainGraph.get_dlist())
            
    #line
    if(special[0]=="Line"):
        tmp_label=current.get_label()
        if(special[1]):
            Line_label.set_text(tmp_label[0])
            slide=current.stats()[4]/90+0.5
            ElasticitySlider.setSlide(slide)
            el=str(round(math.tan((slide)*(math.pi/2)),2))
            if((slide)*(math.pi/2)>=math.pi/2):
                el="∞"
            ElasticitySlider.set_text("Elasticity: "+el)
        else:
            tmp_label[0]=Line_label.get_val()
            current.set_label(tmp_label[0],tmp_label[1],tmp_label[2])
    #point
    if(special[0]=="Point"):
        Point_line1.update_dlist(MainGraph.get_dlist())
        Point_line2.update_dlist(MainGraph.get_dlist())
        tmp_label=current.get_label()
        tmp_vars=current.get_vars()
        if(special[1]):
            Point_line1.reset()
            Point_line2.reset()
            Point_label.set_text(tmp_label[0])
            Point_lines[0]=tmp_vars[0]
            Point_lines[1]=tmp_vars[1]
            if(Point_lines[0]!=None):
                Point_line1.ret_set(Point_lines[0].get_label()[0])
            else:
                Point_line1.ret_set(Point_lines[0])
                
            if(Point_lines[1]!=None):
                Point_line2.ret_set(Point_lines[1].get_label()[0])
            else:
                Point_line2.ret_set(Point_lines[1])
            Point_label1.set_text(tmp_vars[2])
            Point_label2.set_text(tmp_vars[3])
        else:
            tmp_label[0]=Point_label.get_val()
            current.set_label(tmp_label[0],tmp_label[1],tmp_label[2])
            current.set_vars(Point_lines[0],Point_lines[1],Point_label1.get_val(),Point_label2.get_val())
            
    
    #tax and subsidy
    if(special[0]=="Tax" or special[0]=="Subsidy"):
        Tax_line1.update_dlist(MainGraph.get_dlist())
        Tax_line2.update_dlist(MainGraph.get_dlist())
        tmp_label=current.get_label()
        tmp_vars=current.get_vars()
        if(special[1]):
            Tax_line1.reset()
            Tax_line2.reset()
            Tax_label.set_text(tmp_label[0])
            Tax_lines[0]=tmp_vars[0]
            Tax_lines[1]=tmp_vars[1]
            if(Tax_lines[0]!=None):
                Tax_line1.ret_set(Tax_lines[0].get_label()[0])
            else:
                Tax_line1.ret_set(Tax_lines[0])
                
            if(Tax_lines[1]!=None):
                Tax_line2.ret_set(Tax_lines[1].get_label()[0])
            else:
                Tax_line2.ret_set(Tax_lines[1])
            Tax_p1.set_text(tmp_vars[3])
            Tax_p2.set_text(tmp_vars[4])
            Tax_qt.set_text(tmp_vars[5])
            if(special[0]=="Tax"):
                slide=(current.get_a()+0.001)/-100
                Amount_Slider.setSlide(slide)
                Amount_Slider.set_text("Amount: "+str(round(current.get_a()*-1,2)))
            else:
                slide=(current.get_a()-0.001)/100
                Amount_Slider.setSlide(slide)
                Amount_Slider.set_text("Amount: "+str(round(current.get_a(),2)))
            
            ElasticitySlider.setSlide(slide)
            
        else:
            tmp_label[0]=Tax_label.get_val()
            current.set_label(tmp_label[0],tmp_label[1],tmp_label[2])
            current.set_vars(Tax_lines[0],Tax_lines[1],tmp_vars[2],Tax_p1.get_val(),Tax_p2.get_val(),Tax_qt.get_val())
            
            
    
    #rendering
    #Main
    SaveButton.show()
    AddObjectButton.show()
    ObjectMenu.show()
    Xlab.show(False)
    Ylab.show(False)
    MainGraph.set_xlabel(Xlab.get_text_val())
    MainGraph.set_ylabel(Ylab.get_text_val())
    MainGraph.show()
    #nothing
    if(special[0]=="Nothing"):
        Back.show()
    #line
    if(special[0]=="Line"):
        ElasticitySlider.show()
        Line_label.show()
        Line_name_label.show()
    #point
    if(special[0]=="Point"):
        Point_name_label.show()
        Point_label.show()
        Point_label1.show()
        Point_label2.show()
        Point_line1.show()
        Point_line2.show()
    
    #tax and subsidy
    if(special[0]=="Tax" or special[0]=="Subsidy"):
        Tax_name_label.show()
        Tax_label.show()
        Tax_p1.show()
        Tax_p2.show()
        Tax_qt.show()
        Amount_Slider.show()
        Tax_line1.show()
        Tax_line2.show()
    
    if(not main):
        TmpMenu.show()
        TmpInput.show()
        TmpList.show()
        TmpButton.show()
    
    #to here
    display.blit(pygame.transform.scale(draw_screen,(display.get_width(),display.get_height())),(0,0))
    pygame.display.update()#Updating the display
    
    for event in pygame.event.get():#Checking for inputs
        if event.type == pygame.QUIT:#Checking for closing
            pygame.quit()
            quit()
        MainKey.ev(event)
        if event.type == pygame.MOUSEWHEEL:
            sc[0]=-3*event.x
            sc[1]=-3*event.y
    MainKey.update()#deletes
       
            
        
    



