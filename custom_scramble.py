from tkinter import *
from vpython import *

screen = Tk()
screen.geometry("600x450")

COLOR = "white"
W=Y=R=G=O=B=1
DICT = {"red":R,"blue":B,"orange":O,"green":G,"white":W,"yellow":Y}

def ReturnPiece(button,Color):
    ## Corners And Edges
    List = [
        [x5y2,x5y3,x6y3],
        [x3y2,x3y3,x2y3],
        [x3y5,x2y5,x3y6],
        [x5y5,x6y5,x5y6],
        [x0y3,x3y0,x11y3],
        [x5y0,x8y3,x9y3],
        [x0y5,x11y5,x3y8],
        [x5y8,x8y5,x9y5],

        [x2y4,x3y4],
        [x4y2,x4y3],
        [x4y5,x4y6],
        [x5y4,x6y4],
        [x1y3,x3y1],
        [x5y1,x7y3],
        [x7y5,x5y7],
        [x3y7,x1y5],
        [x8y4,x9y4],
        [x11y4,x0y4],
        [x4y0,x10y3],
        [x10y5,x4y8]
        ]

    for i in range(len(List)):
        if button in List[i]:
            try:
                piece = [List[i][0]['bg'],List[i][1]['bg'],List[i][2]['bg']]
            except:
                piece = [List[i][0]['bg'],List[i][1]['bg']]
    if Color != "SystemButtonFace":
        if Color in piece:
            return False
        else:
            return True
    else:
        return True
        

def ChangeCOLOR(colour):
    global COLOR
    COLOR = colour

def PutCOLOR(button):
    global COLOR,W,Y,R,G,O,B,DICT

    valid = ReturnPiece(button,COLOR)

    if valid == True:
        if COLOR != "SystemButtonFace":
            if DICT[COLOR] != 9:
                if button['bg'] != "SystemButtonFace":
                    DICT[button['bg']]-=1
                DICT[COLOR]+=1
                button['bg'] = COLOR
                
        else:
            if button['bg'] != "SystemButtonFace":
                DICT[button['bg']]-=1
                button['bg'] = COLOR

def Complete():
    Top = [['','',''],['','W',''],['','','']]
    Left = [['','',''],['','O',''],['','','']]
    Front = [['','',''],['','G',''],['','','']]
    Right = [['','',''],['','R',''],['','','']]
    Back = [['','',''],['','B',''],['','','']]
    Bottom = [['','',''],['','Y',''],['','','']]

    COLOR_dict = {"red":'R',"blue":'B',"orange":'O',"green":'G',"white":'W',"yellow":'Y',"SystemButtonFace":''}
    
    ## Top
    for y in range(3):
        for x in range(3):
            string = "x{}y{}".format(x+3,y)
            exec("Top[y][x] = COLOR_dict[{}['bg']]".format(string))
    ## Left
    for y in range(3):
        for x in range(3):
            string = "x{}y{}".format(x,y+3)
            exec("Left[y][x] = COLOR_dict[{}['bg']]".format(string))
            
    ## Front
    for y in range(3):
        for x in range(3):
            string = "x{}y{}".format(x+3,y+3)
            exec("Front[y][x] = COLOR_dict[{}['bg']]".format(string))
            
    ## Right
    for y in range(3):
        for x in range(3):
            string = "x{}y{}".format(x+6,y+3)
            exec("Right[y][x] = COLOR_dict[{}['bg']]".format(string))
            
    ## Back
    for y in range(3):
        for x in range(3):
            string = "x{}y{}".format(x+9,y+3)
            exec("Back[y][x] = COLOR_dict[{}['bg']]".format(string))
            
    ## Bottom
    for y in range(3):
        for x in range(3):
            string = "x{}y{}".format(x+3,y+6)
            exec("Bottom[y][x] = COLOR_dict[{}['bg']]".format(string))

    #### Checking Empty Spaces ####
    faces = [Top,Front,Right,Back,Left,Bottom]
    check = True
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if faces[i][j][k] == '':
                    check = False
    if check == True:
        for i in range(6):
            for j in range(3):
                for k in range(3):
                    if faces[i][j][k] == "G":
                        Face[i][j][k].color = color.green
                    if faces[i][j][k] == "R":
                        Face[i][j][k].color = color.red
                    if faces[i][j][k] == "O":
                        Face[i][j][k].color = color.orange
                    if faces[i][j][k] == "Y":
                        Face[i][j][k].color = color.yellow
                    if faces[i][j][k] == "B":
                        Face[i][j][k].color = color.blue
                    if faces[i][j][k] == "W":
                        Face[i][j][k].color = color.white
        Hide()

Root = 0
Face = 0
def Hide():
    screen.withdraw()
    if Root != 0:
        Root.update()
        Root.deiconify()

def Show(root = 0,FACE = 0):
    global Root,Face
    Root = root
    Face = FACE
    screen.update()
    screen.deiconify()

ButtonList = []    
## LINE 1
for y in range(3):
    for x in range(3):
        string = "x{}y{}".format(x+3,y)
        exec("{} = Button(screen,width=6,height=3,command = lambda:PutCOLOR({}))".format(string,string))
        exec("{}.place(x=150+(50*x),y=(50*y))".format(string))
        exec("ButtonList.append({})".format(string))

## LINE 2
for y in range(3):
    for x in range(12):
        string = "x{}y{}".format(x,y+3)
        exec("{} = Button(screen,width=6,height=3,command = lambda:PutCOLOR({}))".format(string,string))
        exec("{}.place(x=(50*x),y=150+(50*y))".format(string))
        exec("ButtonList.append({})".format(string))
        
## LINE 3
for y in range(3):
    for x in range(3):
        string = "x{}y{}".format(x+3,y+6)
        exec("{} = Button(screen,width=6,height=3,command = lambda:PutCOLOR({}))".format(string,string))
        exec("{}.place(x=150+(50*x),y=300+(50*y))".format(string))
        exec("ButtonList.append({})".format(string))

ButtonList.remove(x4y1)
ButtonList.remove(x1y4)
ButtonList.remove(x4y4)
ButtonList.remove(x7y4)
ButtonList.remove(x10y4)
ButtonList.remove(x4y7)

def NewCube():
    for i in range(len(ButtonList)):
        ButtonList[i]['bg'] = "SystemButtonFace"

## Defaults
x4y1['bg'] = "white"
x1y4['bg'] = "orange"
x4y4['bg'] = "green"
x7y4['bg'] = "red"
x10y4['bg'] = "blue"
x4y7['bg'] = "yellow"
####
x4y1['state'] = "disabled"
x1y4['state'] = "disabled"
x4y4['state'] = "disabled"
x7y4['state'] = "disabled"
x10y4['state'] = "disabled"
x4y7['state'] = "disabled"

## COLOR selection
white = Button(screen,width=4,height=2,bg="white",command = lambda:ChangeCOLOR("white"))
white.place(x=375,y=25)

green = Button(screen,width=4,height=2,bg="green",command = lambda:ChangeCOLOR("green"))
green.place(x=425,y=25)

red = Button(screen,width=4,height=2,bg="red",command = lambda:ChangeCOLOR("red"))
red.place(x=475,y=25)

yellow = Button(screen,width=4,height=2,bg="yellow",command = lambda:ChangeCOLOR("yellow"))
yellow.place(x=375,y=75)

blue = Button(screen,width=4,height=2,bg="blue",command = lambda:ChangeCOLOR("blue"))
blue.place(x=425,y=75)

orange = Button(screen,width=4,height=2,bg="orange",command = lambda:ChangeCOLOR("orange"))
orange.place(x=475,y=75)

none = Button(screen,width=4,height=2,command = lambda:ChangeCOLOR("SystemButtonFace"))
none.place(x=525,y=50)
## Done or Cancel buttons
done = Button(screen,bg = "light green",text = "DONE {}".format(u"\u2713"),font = ("Arial",12,'bold'),command = Complete)
done.place(x=400,y=350)

cancel = Button(screen,bg = "red",text = "CANCEL X",font = ("Arial",12,'bold'),command = Hide)
cancel.place(x=400,y=400)

