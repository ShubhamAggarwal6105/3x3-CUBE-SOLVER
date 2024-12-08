from vpython import *
import time
import cube_solver
from tkinter import *
from random import randint
import custom_scramble as Cs
Cs.Hide()

l = 5
w = 0.05
gap = 5.1
center = vector(5.1,7.6,2.6)

front = []
side = []
top = []

t_col = 0
Y_list = [1,2,3,13,14,15,25,26,27]
W_list = [10,11,12,22,23,24,34,35,36]
for i in range(3):
    for j in range(4):
        for k in range(3):
            t_col+=1
            pos = vector(i*gap,j*gap,k*gap-2.5)
            if t_col in Y_list:
                quad = box(pos = pos,length=l,height=w,width=l,color=color.yellow)
            elif t_col in W_list:
                quad = box(pos = pos,length=l,height=w,width=l,color=color.white)
            else:
                quad = "NoObject"
            top.append(quad)

s_col = 0
O_list = [i for i in range(1,10)]
R_list = [i for i in range(28,37)]
for i in range(4):
    for j in range(3):
        for k in range(3):
            s_col+=1
            pos = vector(i*gap-2.5,j*gap+2.5,k*gap-2.5)
            if s_col in O_list:
                quad = box(pos = pos,length=w,height=l,width=l,color=color.orange)
            elif s_col in R_list:
                quad = box(pos = pos,length=w,height=l,width=l,color=color.red)
            else:
                quad = "NoObject"
            side.append(quad)
            
f_col = 0
B_list = [i for i in range(1,37,4)]
G_list = [i for i in range(4,37,4)]
for i in range(3):
    for j in range(3):
        for k in range(4):
            f_col+=1
            pos = vector(i*gap,j*gap+2.5,k*gap-5)
            if f_col in B_list:
                quad = box(pos = pos,length=l,height=l,width=w,color = color.blue)
            elif f_col in G_list:
                quad = box(pos = pos,length=l,height=l,width=w,color = color.green)
            else:
                quad = "NoObject"
            front.append(quad)

####################################
Top = [[top[9], top[21],top[33]],
       [top[10],top[22],top[34]],
       [top[11],top[23],top[35]]]
Front = [[front[11],front[23],front[35]],
         [front[7], front[19],front[31]],
         [front[3], front[15],front[27]]]
Right = [[side[35],side[34],side[33]],
         [side[32],side[31],side[30]],
         [side[29],side[28],side[27]]]

Back = [[front[32],front[20],front[8]],
        [front[28],front[16],front[4]],
        [front[24],front[12],front[0]]]
Left = [[side[6],side[7],side[8]],
        [side[3],side[4],side[5]],
        [side[0],side[1],side[2]]]
Bottom = [[top[2],top[14],top[26]],
          [top[1],top[13],top[25]],
          [top[0],top[12],top[24]]]

####################################
####################################
def rotate_left(face):
    #Rotate corners
    temp = face[0][0]
    face[0][0] = face[0][2]
    face[0][2] = face[2][2]
    face[2][2] = face[2][0]
    face[2][0] = temp
    #Rotate edges
    temp = face[0][1]
    face[0][1] = face[1][2]
    face[1][2] = face[2][1]
    face[2][1] = face[1][0]
    face[1][0] = temp

def rotate_right(face):
    rotate_left(face)
    rotate_left(face)
    rotate_left(face)

def URR():
    global Top,Front,Bottom,Back,Right,Left
    rotate_right(Top)
    #edges
    temp = Front[0][1]
    Front[0][1] = Right[0][1]
    Right[0][1] = Back[0][1]
    Back[0][1] = Left[0][1]
    Left[0][1] = temp
    #left-corners
    temp = Front[0][0]
    Front[0][0] = Right[0][0]
    Right[0][0] = Back[0][0]
    Back[0][0] = Left[0][0]
    Left[0][0] = temp
    #right-corners
    temp = Front[0][2]
    Front[0][2] = Right[0][2]
    Right[0][2] = Back[0][2]
    Back[0][2] = Left[0][2]
    Left[0][2] = temp

def x():
    global Top,Front,Bottom,Back,Left,Right
    temp=Front
    Front=Bottom
    Bottom=Back
    Back=Top
    Top=temp
    rotate_left(Left)
    rotate_right(Right)
    rotate_left(Bottom);rotate_left(Bottom);rotate_left(Back);rotate_left(Back)
def x_():
    x();x();x()    
def y():
    global Top,Front,Bottom,Back,Left,Right
    temp=Front
    Front=Right
    Right=Back
    Back=Left
    Left=temp
        
    rotate_right(Top)
    rotate_left(Bottom)
def y_():
    y();y();y()
def z_():
    y();x();y_()
def z():
    z_();z_();z_()

####################################
####################################
speed=18
Time=0.5
    
def R():
    global speed,Time
    RList = [Front[0][2],Front[1][2],Front[2][2],Back[0][0],Back[1][0],Back[2][0]] + [Bottom[0][2],Bottom[1][2],Bottom[2][2],Top[0][2],Top[1][2],Top[2][2]] + Right[0][0:3]+Right[1][0:3]+Right[2][0:3]
    for i in range(speed):
        for i in range(len(RList)):
            RList[i].rotate(angle = (-pi/2)/speed , origin = center,axis = vector(RList[i].length,0,0))
        time.sleep(Time/speed)

def R_():
    global speed,Time
    RList = [Front[0][2],Front[1][2],Front[2][2],Back[0][0],Back[1][0],Back[2][0]] + [Bottom[0][2],Bottom[1][2],Bottom[2][2],Top[0][2],Top[1][2],Top[2][2]] + Right[0][0:3]+Right[1][0:3]+Right[2][0:3]
    for i in range(speed):
        for i in range(len(RList)):
            RList[i].rotate(angle = (pi/2)/speed , origin = center,axis = vector(RList[i].length,0,0))
        time.sleep(Time/speed)


def L_():
    global speed,Time
    RList = [Front[0][0],Front[1][0],Front[2][0],Back[0][2],Back[1][2],Back[2][2]] + [Bottom[0][0],Bottom[1][0],Bottom[2][0],Top[0][0],Top[1][0],Top[2][0]] + Left[0][0:3]+Left[1][0:3]+Left[2][0:3]
    for i in range(speed):
        for i in range(len(RList)):
            RList[i].rotate(angle = (-pi/2)/speed , origin = center,axis = vector(RList[i].length,0,0))
        time.sleep(Time/speed)

def L():
    global speed,Time
    RList = [Front[0][0],Front[1][0],Front[2][0],Back[0][2],Back[1][2],Back[2][2]] + [Bottom[0][0],Bottom[1][0],Bottom[2][0],Top[0][0],Top[1][0],Top[2][0]] + Left[0][0:3]+Left[1][0:3]+Left[2][0:3]
    for i in range(speed):
        for i in range(len(RList)):
            RList[i].rotate(angle = (pi/2)/speed , origin = center,axis = vector(RList[i].length,0,0))
        time.sleep(Time/speed)


def U():
    global speed,Time
    RList = Back[0]+Front[0] + Top[0][0:3]+Top[1][0:3]+Top[2][0:3] + Left[0]+Right[0]
    for i in range(speed):
        for i in range(len(RList)):
            RList[i].rotate(angle = (-pi/2)/speed , origin = center,axis = vector(0,RList[i].height,0))
        time.sleep(Time/speed)
   
def U_():
    global speed,Time
    RList = Back[0]+Front[0] + Top[0][0:3]+Top[1][0:3]+Top[2][0:3] + Left[0]+Right[0]
    for i in range(speed):
        for i in range(len(RList)):
            RList[i].rotate(angle = (pi/2)/speed , origin = center,axis = vector(0,RList[i].height,0))
        time.sleep(Time/speed)

        
def D_():
    global speed,Time
    RList = Back[2]+Front[2] + Bottom[0][0:3]+Bottom[1][0:3]+Bottom[2][0:3] + Left[2]+Right[2]
    for i in range(speed):
        for i in range(len(RList)):
            RList[i].rotate(angle = (-pi/2)/speed , origin = center,axis = vector(0,RList[i].height,0))
        time.sleep(Time/speed)

def D():
    global speed,Time
    RList = Back[2]+Front[2] + Bottom[0][0:3]+Bottom[1][0:3]+Bottom[2][0:3] + Left[2]+Right[2]
    for i in range(speed):
        for i in range(len(RList)):
            RList[i].rotate(angle = (pi/2)/speed , origin = center,axis = vector(0,RList[i].height,0))
        time.sleep(Time/speed)


def F_():
    global speed,Time
    RList = Front[0][0:3]+Front[1][0:3]+Front[2][0:3] + [Left[0][2],Left[1][2],Left[2][2],Right[0][0],Right[1][0],Right[2][0]] + Bottom[0]+Top[2]
    for i in range(speed):
        for i in range(len(RList)):
            RList[i].rotate(angle = (pi/2)/speed , origin = center,axis = vector(0,0,RList[i].width))
        time.sleep(Time/speed)

def F():
    global speed,Time
    RList = Front[0][0:3]+Front[1][0:3]+Front[2][0:3] + [Left[0][2],Left[1][2],Left[2][2],Right[0][0],Right[1][0],Right[2][0]] + Bottom[0]+Top[2]
    for i in range(speed):
        for i in range(len(RList)):
            RList[i].rotate(angle = (-pi/2)/speed , origin = center,axis = vector(0,0,RList[i].width))
        time.sleep(Time/speed)


def B_():
    global speed,Time
    RList = Back[0][0:3]+Back[1][0:3]+Back[2][0:3] + [Left[0][0],Left[1][0],Left[2][0],Right[0][2],Right[1][2],Right[2][2]] + Bottom[2]+Top[0]
    for i in range(speed):
        for i in range(len(RList)):
            RList[i].rotate(angle = (-pi/2)/speed , origin = center,axis = vector(0,0,RList[i].width))
        time.sleep(Time/speed)

def B():
    global speed,Time
    RList = Back[0][0:3]+Back[1][0:3]+Back[2][0:3] + [Left[0][0],Left[1][0],Left[2][0],Right[0][2],Right[1][2],Right[2][2]] + Bottom[2]+Top[0]
    for i in range(speed):
        for i in range(len(RList)):
            RList[i].rotate(angle = (pi/2)/speed , origin = center,axis = vector(0,0,RList[i].width))
        time.sleep(Time/speed)


def X():
    global speed,Time
    RList = Back[0][0:3]+Back[1][0:3]+Back[2][0:3] + Front[0][0:3]+Front[1][0:3]+Front[2][0:3] + Top[0][0:3]+Top[1][0:3]+Top[2][0:3] + Bottom[0][0:3]+Bottom[1][0:3]+Bottom[2][0:3] + Left[0][0:3]+Left[1][0:3]+Left[2][0:3] + Right[0][0:3]+Right[1][0:3]+Right[2][0:3]
    for i in range(speed):
        for i in range(len(RList)):
            RList[i].rotate(angle = (-pi/2)/speed , origin = center,axis = vector(RList[i].length,0,0))
        time.sleep(Time/speed)

def X_():
    global speed,Time
    RList = Back[0][0:3]+Back[1][0:3]+Back[2][0:3] + Front[0][0:3]+Front[1][0:3]+Front[2][0:3] + Top[0][0:3]+Top[1][0:3]+Top[2][0:3] + Bottom[0][0:3]+Bottom[1][0:3]+Bottom[2][0:3] + Left[0][0:3]+Left[1][0:3]+Left[2][0:3] + Right[0][0:3]+Right[1][0:3]+Right[2][0:3]
    for i in range(speed):
        for i in range(len(RList)):
            RList[i].rotate(angle = (pi/2)/speed , origin = center,axis = vector(RList[i].length,0,0))
        time.sleep(Time/speed)


def Y():
    global speed,Time
    RList = Back[0][0:3]+Back[1][0:3]+Back[2][0:3] + Front[0][0:3]+Front[1][0:3]+Front[2][0:3] + Top[0][0:3]+Top[1][0:3]+Top[2][0:3] + Bottom[0][0:3]+Bottom[1][0:3]+Bottom[2][0:3] + Left[0][0:3]+Left[1][0:3]+Left[2][0:3] + Right[0][0:3]+Right[1][0:3]+Right[2][0:3]
    for i in range(speed):
        for i in range(len(RList)):
            RList[i].rotate(angle = (-pi/2)/speed , origin = center,axis = vector(0,RList[i].height,0))
        time.sleep(Time/speed)

def Y_():
    global speed,Time
    RList = Back[0][0:3]+Back[1][0:3]+Back[2][0:3] + Front[0][0:3]+Front[1][0:3]+Front[2][0:3] + Top[0][0:3]+Top[1][0:3]+Top[2][0:3] + Bottom[0][0:3]+Bottom[1][0:3]+Bottom[2][0:3] + Left[0][0:3]+Left[1][0:3]+Left[2][0:3] + Right[0][0:3]+Right[1][0:3]+Right[2][0:3]
    for i in range(speed):
        for i in range(len(RList)):
            RList[i].rotate(angle = (pi/2)/speed , origin = center,axis = vector(0,RList[i].height,0))
        time.sleep(Time/speed)


def Z():
    global speed,Time
    RList = Back[0][0:3]+Back[1][0:3]+Back[2][0:3] + Front[0][0:3]+Front[1][0:3]+Front[2][0:3] + Top[0][0:3]+Top[1][0:3]+Top[2][0:3] + Bottom[0][0:3]+Bottom[1][0:3]+Bottom[2][0:3] + Left[0][0:3]+Left[1][0:3]+Left[2][0:3] + Right[0][0:3]+Right[1][0:3]+Right[2][0:3]
    for i in range(speed):
        for i in range(len(RList)):
            RList[i].rotate(angle = (-pi/2)/speed , origin = center,axis = vector(0,0,RList[i].width))
        time.sleep(Time/speed)

def Z_():
    global speed,Time
    RList = Back[0][0:3]+Back[1][0:3]+Back[2][0:3] + Front[0][0:3]+Front[1][0:3]+Front[2][0:3] + Top[0][0:3]+Top[1][0:3]+Top[2][0:3] + Bottom[0][0:3]+Bottom[1][0:3]+Bottom[2][0:3] + Left[0][0:3]+Left[1][0:3]+Left[2][0:3] + Right[0][0:3]+Right[1][0:3]+Right[2][0:3]
    for i in range(speed):
        for i in range(len(RList)):
            RList[i].rotate(angle = (pi/2)/speed , origin = center,axis = vector(0,0,RList[i].width))
        time.sleep(Time/speed)


def M():
    global speed,Time
    RList = [Front[i][1] for i in range(3)]+[Top[i][1] for i in range(3)] + [Back[i][1] for i in range(3)]+[Bottom[i][1] for i in range(3)]
    for i in range(speed):
        for i in range(len(RList)):
            RList[i].rotate(angle = (pi/2)/speed , origin = center,axis = vector(RList[i].length,0,0))
        time.sleep(Time/speed)
    
def M_():
    global speed,Time
    RList = [Front[i][1] for i in range(3)]+[Top[i][1] for i in range(3)] + [Back[i][1] for i in range(3)]+[Bottom[i][1] for i in range(3)]
    for i in range(speed):
        for i in range(len(RList)):
            RList[i].rotate(angle = (-pi/2)/speed , origin = center,axis = vector(RList[i].length,0,0))
        time.sleep(Time/speed)
    

def E():
    global speed,Time
    RList = Front[1]+Left[1]+Right[1]+Back[1]
    for i in range(speed):
        for i in range(len(RList)):
            RList[i].rotate(angle = (pi/2)/speed , origin = center,axis = vector(0,RList[i].height,0))
        time.sleep(Time/speed)
    
def E_():
    global speed,Time
    RList = Front[1]+Left[1]+Right[1]+Back[1]
    for i in range(speed):
        for i in range(len(RList)):
            RList[i].rotate(angle = (-pi/2)/speed , origin = center,axis = vector(0,RList[i].height,0))
        time.sleep(Time/speed)
        

def S():
    global speed,Time
    RList = Top[1]+Bottom[1]+ [Left[i][1] for i in range(3)] + [Right[i][1] for i in range(3)]
    for i in range(speed):
        for i in range(len(RList)):
            RList[i].rotate(angle = (-pi/2)/speed , origin = center,axis = vector(0,0,RList[i].width))
        time.sleep(Time/speed)
  
def S_():
    global speed,Time
    RList = Top[1]+Bottom[1]+ [Left[i][1] for i in range(3)] + [Right[i][1] for i in range(3)]
    for i in range(speed):
        for i in range(len(RList)):
            RList[i].rotate(angle = (pi/2)/speed , origin = center,axis = vector(0,0,RList[i].width))
        time.sleep(Time/speed)

######################################################################################################
######################################################################################################
def execute(string):
    move=str.lower(string)
    #U
    if move=="u":
        URR()
        U()
    elif move=="u'":
        URR();URR();URR()
        U_()
    elif move=="u2":
        URR();URR()
        U();U()
    #F
    elif move=="f":
        x()
        URR()
        x_()
        F()
    elif move=="f'":
        x()
        URR();URR();URR()
        x_()
        F_()
    elif move=="f2":
        x()
        URR();URR()
        x_()
        F();F()
    #B
    elif move=="b":
        x_()
        URR()
        x()
        B()
    elif move=="b'":
        x_()
        URR();URR();URR()
        x()
        B_()
    elif move=="b2":
        x_()
        URR();URR()
        x()
        B();B()
    #D
    elif move=="d":
        x();x()
        URR()
        x_();x_()
        D()
    elif move=="d'":
        x();x()
        URR();URR();URR()
        x_();x_()
        D_()
    elif move=="d2":
        x();x()
        URR();URR()
        x_();x_()
        D();D()
    #R
    elif move=="r":
        z_()
        URR()
        z()
        R()
    elif move=="r'":
        z_()
        URR();URR();URR()
        z()
        R_()
    elif move=="r2":
        z_()
        URR();URR()
        z()
        R();R()
    #L
    elif move=="l":
        z()
        URR()
        z_()
        L()
    elif move=="l'":
        z()
        URR();URR();URR()
        z_()
        L_()
    elif move=="l2":
        z()
        URR();URR()
        z_()
        L();L()
        
    #M
    # r l' x'
    elif move=="m":
        z_();URR();z()
        z();URR();URR();URR();z_()
        x_()
        M()
    # r' l x
    elif move=="m'":
        z_();URR();URR();URR();z()
        z();URR();z_()
        x()
        M_()
    # r2 l2 x2
    elif move=="m2":
        z_();URR();URR();z()
        z();URR();URR();z_()
        x() ; x()
        M();M()
    #E
    # u d' y'
    elif move=="e":
        URR()
        x();x() ; URR();URR();URR() ; x_();x_()
        y_()
        E()
    # u' d y
    elif move=="e'":
        URR();URR();URR()
        x();x() ; URR() ; x_();x_()
        y()
        E_()
    # u2 d2 y2
    elif move=="e2":
        URR();URR()
        x();x() ; URR();URR() ; x_();x_()
        y();y()
        E();E()
    #S
    # f' b z
    elif move=="s":
        x() ; URR();URR();URR() ; x_()
        x_();URR();x()
        z()
        S()
    # f b' z'
    elif move=="s'":
        x() ; URR() ; x_()
        x_();URR();URR();URR();x()
        z_()
        S_()
    # f2 b2 z2
    elif move=="s2":
        x() ; URR();URR() ; x_()
        x_(); URR();URR() ; x()
        z();z()
        S();S()

    #X Y Z
    elif move=="x":
        x()
        X()
    elif move=="x'":
        x_()
        X_()
    elif move=="x2":
        x();x()
        X();X()
        
    elif move=="y":
        y()
        Y()
    elif move=="y'":
        y_()
        Y_()
    elif move=="y2":
        y();y()
        Y();Y()
        
    elif move=="z":
        z()
        Z()
    elif move=="z'":
        z_()
        Z_()
    elif move=="z2":
        z();z()
        Z();Z()

    else:
        return 0;
                
def NewRubiksCube():
    Faces = [Top,Front,Right,Back,Left,Bottom]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if i==0:
                    Faces[i][j][k].color = color.white
                if i==1:
                    Faces[i][j][k].color = color.green
                if i==2:
                    Faces[i][j][k].color = color.red
                if i==3:
                    Faces[i][j][k].color = color.blue
                if i==4:
                    Faces[i][j][k].color = color.orange
                if i==5:
                    Faces[i][j][k].color = color.yellow

def Draw_Scramble():
    root.withdraw()
    Cs.NewCube()
    Cs.Show(root = root,FACE = [Top,Front,Right,Back,Left,Bottom])
         
##############################################################################################################################################
######################## TKINTER GUI PART ###################### TKINTER GUI PART ############################################################
##############################################################################################################################################

root = Tk()
root.title("Cube Solver")
root.geometry("500x350")

shuffle = ""

def Execute():
    moves = str(MoveEntry.get())
    moves_list = str.split(moves)
    for Move in range(len(moves_list)):
        execute(moves_list[Move])
        
def CustomScramble():
    global shuffle,speed
    NewRubiksCube()
    shuffle = (CustomScramEntry.get())
    ScrambleLabel['text'] = shuffle
    root.update()
    
    speed = 1
    moves_list = str.split(shuffle)
    for Move in range(len(moves_list)):
        execute(moves_list[Move])
    speed = 90
    
def GUItoClipboard(word):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(word)
    r.destroy()

def GUIScramble(moves = 25):
    global shuffle,speed
    NewRubiksCube()
    shuffle = ""
    prevMove = ""
    for i in range(moves):
        while True:
            thisMove = ""
            r = randint(0, 5)
            if r == 0:
                thisMove += "u"
            elif r == 1:
                thisMove += "f"
            elif r == 2:
                thisMove += "r"
            elif r == 3:
                thisMove += "l"
            elif r == 4:
                thisMove += "d"
            elif r == 5:
                thisMove += "b"
            if thisMove == "u" and prevMove != "u" and prevMove != "d":
                break
            if thisMove == "f" and prevMove != "f" and prevMove != "b":
                break
            if thisMove == "r" and prevMove != "r" and prevMove != "l":
                break
            if thisMove == "l" and prevMove != "l" and prevMove != "r":
                break
            if thisMove == "d" and prevMove != "d" and prevMove != "u":
                break
            if thisMove == "b" and prevMove != "b" and prevMove != "f":
                break
        r = randint(0, 3)
        if r == 1:
            move = thisMove + "'"
        elif r == 2:
            move = thisMove + "2"
        else:
            move = thisMove
        shuffle+=move
        shuffle += " "
        prevMove = thisMove
    ScrambleLabel['text'] = shuffle
    root.update()
    
    speed = 1
    moves_list = str.split(shuffle)
    for Move in range(len(moves_list)):
        execute(moves_list[Move])
    speed = 90
    
def GUInewCube():
    global shuffle
    NewRubiksCube()
    ScrambleLabel['text'] = "Scramble will be displayed here"
    SolutionLabel['text'] = "Solution will be displayed here"
    SolutionNumberLabel['text'] = "0"
    MoveEntry.delete(0,END)
    CustomScramEntry.delete(0,END)
    shuffle = ""

def GUISolve():
    ###########################################################
    ## CUBE SOLVING PART IN MODULE : cube_solver             ##
    ###########################################################
    TOP = [['','',''],['','',''],['','','']]
    FRONT = [['','',''],['','',''],['','','']]
    RIGHT = [['','',''],['','',''],['','','']]
    BACK = [['','',''],['','',''],['','','']]
    LEFT = [['','',''],['','',''],['','','']]
    BOTTOM = [['','',''],['','',''],['','','']]
    FACES = [TOP,FRONT,RIGHT,BACK,LEFT,BOTTOM]
    Faces = [Top,Front,Right,Back,Left,Bottom]

    for i in range(6):
        for j in range(3):
            for k in range(3):
                if Faces[i][j][k].color == color.green:
                    FACES[i][j][k] = "G"
                if Faces[i][j][k].color == color.red:
                    FACES[i][j][k] = "R"
                if Faces[i][j][k].color == color.blue:
                    FACES[i][j][k] = "B"
                if Faces[i][j][k].color == color.yellow:
                    FACES[i][j][k] = "Y"
                if Faces[i][j][k].color == color.white:
                    FACES[i][j][k] = "W"
                if Faces[i][j][k].color == color.orange:
                    FACES[i][j][k] = "O"

    cube_solver.GLOBALIZE(TOP,FRONT,RIGHT,BACK,LEFT,BOTTOM)
    solve,length = cube_solver.SolveCube()

    SolutionLabel['text'] = solve
    SolutionNumberLabel['text'] = str(length)
    root.update()

    SolveList = str.split(solve)
    for Move in range(len(SolveList)):
        execute(SolveList[Move])
  
#Frame for controls
frame = Frame(root)
frame.grid(row=0,column=1, sticky="n")

#Frame for cube rotations
Rframe = Frame(root)
Rframe.grid(row=0, column=0, sticky = "n")

#row 1 - welcome label and new cube button
Welcome = Label(frame, text = "Welcome to the Cube Solver").grid(row=1,column=0)
NewCubeButton = Button(frame,text="New Cube", command = lambda: GUInewCube())
NewCubeButton.grid(row=1, column=1)
#row 2 - label to tell you to enter a move for execution
EnterMove = Label(frame, text ="Enter move(s):").grid(row=2,column=0)
#row 3 - Has entry for custom moves as well as button to execute them
MoveEntry = Entry(frame)
MoveEntry.grid(row = 3, column=0)
ExecuteButton = Button(frame,text="Execute", command = lambda: Execute()).grid(row = 3,column = 1, sticky="w")
#row 4 - The label that will print out the current scramble after generation
ScrambleLabel = Label(frame, text="Scramble will be displayed here",wraplength=180, justify=CENTER, height = 2)
ScrambleLabel.grid(row=4,column=0, columnspan=2)
#row 5 - The scramble button to generate new scramble and copy scramble to clipboard
ScrambleButton = Button(frame, text="Shuffle",bg="lightgreen", command = lambda: GUIScramble()).grid(row = 5, column = 0)
CopyScrambleButton = Button(frame, text="Copy Scramble",bg="#EF9", command = lambda: GUItoClipboard(ScrambleLabel['text'])).grid(row = 5, column = 1)
#row 6 - entry for custom scramble and button to apply custom scramble to cube
CustomScramEntry = Entry(frame)
CustomScramEntry.grid(row=6,column=0,sticky="w")
CustomScramButton = Button(frame,text="Custom Scramble",bg="lightgreen", command = lambda: CustomScramble())
CustomScramButton.grid(row=6,column=1)
#row 7 - Slow solve (using timer to do it slowly), instant solve(quick and instant solution), copy solution to clipboard buttons
#SolveTimerButton = Button(frame, text="Slow Solve", bg="#D53", command = lambda: GUIautomateSolve()).grid(row=7, column=0, sticky="w", pady=5)
SolveButton = Button(frame, text="Solve Cube",bg="#D53",command = lambda: GUISolve()).grid(row = 7, column = 0) #sticky="e" if using timer button as well
CopyScrambleButton = Button(frame, text="Copy Solution",bg="#EF9", command = lambda: GUItoClipboard(SolutionLabel['text'])).grid(row = 7, column = 1)
#row 8 - the label that contains the solution that will be generated
SolutionLabel = Label(frame, text="Solution will be displayed here", wraplength = 250, justify=CENTER, height = 8)
SolutionLabel.grid(row=8, column=0, columnspan=2)
#row 9 - Labels for number of moves needed to solve 
SolutionNumberInfoLabel = Label(frame, text="Total number of moves used:")
SolutionNumberInfoLabel.grid(row=9, column=0,sticky="e")
SolutionNumberLabel = Label(frame, text="0")
SolutionNumberLabel.grid(row=9, column=1,sticky="w")

#In Rframe, buttons for rotation
RotationLabel = Label(Rframe,text="Use the buttons below to rotate the cube").grid(row=0,column=0, columnspan=3)
YrotationButton = Button(Rframe,font = ('Arial',10,'bold'), text="{} Y".format(u"\u2190"), command = lambda: execute("y"))
YrotationButton.grid(row=1, column=0)
YirotationButton = Button(Rframe,font = ('Arial',10,'bold'), text="Y' {}".format(u"\u2192"), command = lambda: execute("Y'"))
YirotationButton.grid(row=1, column=2)

XrotationButton = Button(Rframe,font = ('Arial',10,'bold'), text="X {}".format(u"\u2191"), command = lambda: execute("x"))
XrotationButton.grid(row=2, column=1)
XirotationButton = Button(Rframe,font = ('Arial',10,'bold'), text="X' {}".format(u"\u2193"), command = lambda: execute("x'"))
XirotationButton.grid(row=3, column=1)

ZrotationButton = Button(Rframe,font = ('Arial',10,'bold'), text="{} Z".format(u"\u293E"), command = lambda: execute("z"))
ZrotationButton.grid(row=4, column=0)
ZirotationButton = Button(Rframe,font = ('Arial',10,'bold'), text="Z' {}".format(u"\u293F"), command = lambda: execute("z'"))
ZirotationButton.grid(row=4, column=2)

## CustomScramble BUTTON
csLabel = Label(Rframe,text = "Use the button below to \ndraw the Custom Scramble of cube")
csLabel.grid(row=5,column=0, columnspan=3)

cs = Button(Rframe,text = "Draw\nScramble",bg = "light green",fg = "red",font = ('Arial',10,'bold'),command = Draw_Scramble)
cs.grid(row = 7,column = 1)

root.mainloop()
##############################################################################################################################################
##############################################################################################################################################