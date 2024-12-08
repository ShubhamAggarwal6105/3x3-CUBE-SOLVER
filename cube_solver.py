def GLOBALIZE(f1,f2,f3,f4,f5,f6):
    global Top,Front,Right,Back,Left,Bottom,faces,MovesList

    Top = f1
    Front = f2
    Right = f3
    Back = f4
    Left = f5
    Bottom = f6
    faces=[Top,Front,Right,Back,Left,Bottom]
    MovesList = []

def PrintFaces():
    global Top,Front,Right,Back,Left,Bottom
    for i in faces:
        for idx,line in enumerate(i):
            print(line)
        print()
def PrintCube():
    global Top,Front,Right,Left,Bottom
    for i in range(3):
        print("               ",Top[i])
    for i in range(3):
        print(Left[i],Front[i],Right[i])
    for i in range(3):
        print("               ",Bottom[i])
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

def execute(string):
    move=str.lower(string)
    #U
    if move=="u":
        URR()
    elif move=="u'":
        URR();URR();URR()
    elif move=="u2":
        URR();URR()
    #F
    elif move=="f":
        x()
        URR()
        x_()
    elif move=="f'":
        x()
        URR();URR();URR()
        x_()
    elif move=="f2":
        x()
        URR();URR()
        x_()
    #B
    elif move=="b":
        x_()
        URR()
        x()
    elif move=="b'":
        x_()
        URR();URR();URR()
        x()
    elif move=="b2":
        x_()
        URR();URR()
        x()
    #D
    elif move=="d":
        x();x()
        URR()
        x_();x_()
    elif move=="d'":
        x();x()
        URR();URR();URR()
        x_();x_()
    elif move=="d2":
        x();x()
        URR();URR()
        x_();x_()
    #R
    elif move=="r":
        z_()
        URR()
        z()
    elif move=="r'":
        z_()
        URR();URR();URR()
        z()
    elif move=="r2":
        z_()
        URR();URR()
        z()
    #L
    elif move=="l":
        z()
        URR()
        z_()
    elif move=="l'":
        z()
        URR();URR();URR()
        z_()
    elif move=="l2":
        z()
        URR();URR()
        z_()
        
    #M
    # r l' x'
    elif move=="m":
        z_();URR();z()
        z();URR();URR();URR();z_()
        x_()
    # r' l x
    elif move=="m'":
        z_();URR();URR();URR();z()
        z();URR();z_()
        x()
    # r2 l2 x2
    elif move=="m2":
        z_();URR();URR();z()
        z();URR();URR();z_()
        x() ; x()
    #E
    # u d' y'
    elif move=="e":
        URR()
        x();x() ; URR();URR();URR() ; x_();x_()
        y_()
    # u' d y
    elif move=="e'":
        URR();URR();URR()
        x();x() ; URR() ; x_();x_()
        y()
    # u2 d2 y2
    elif move=="e2":
        URR();URR()
        x();x() ; URR();URR() ; x_();x_()
        y();y()
    #S
    # f' b z
    elif move=="s":
        x() ; URR();URR();URR() ; x_()
        x_();URR();x()
        z()
    # f b' z'
    elif move=="s'":
        x() ; URR() ; x_()
        x_();URR();URR();URR();x()
        z_()
    # f2 b2 z2
    elif move=="s2":
        x() ; URR();URR() ; x_()
        x_(); URR();URR() ; x()
        z();z()

    #X Y Z
    elif move=="x":
        x()
    elif move=="x'":
        x_()
    elif move=="y":
        y()
    elif move=="y'":
        y_()
    elif move=="z":
        z()
    elif move=="z'":
        z_()

    else:
        return 0;
        
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

def m(s):
    global MovesList
    k = s.split()
    for move in k:
        MovesList.append(move)
        execute(move)

def simplify_moves(moves_list):
    new_list = []
    prev_move = ""
    
    for move in moves_list:
        if prev_move == "" or prev_move == '':
            prev_move = move
            new_list.append(move)
            continue
        if move[0] == prev_move[0]:
            if len(move) == 1:
                if len(prev_move) <= 1:
                    del new_list[-1]
                    mv = move[0] + "2"
                    new_list.append(mv)
                    prev_move = mv
                    continue
                if prev_move[1] == "'":
                    del new_list[-1]
                    prev_move = new_list[-1] if len(new_list) > 0 else ""
                    continue
                if prev_move[1] == "2":
                    del new_list[-1]
                    mv = move[0] + "'"
                    new_list.append(mv)
                    prev_move = mv
                    continue
            if move[1] == "'":
                if len(prev_move) == 1:
                    del new_list[-1]
                    prev_move = new_list[-1] if len(new_list) > 0 else ""
                    continue
                if prev_move[1] == "'":
                    del new_list[-1]
                    mv = move[0] + "2"
                    new_list.append(mv)
                    prev_move = mv
                    continue
                if prev_move[1] == "2":
                    del new_list[-1]
                    mv = move[0]
                    new_list.append(mv)
                    prev_move = mv
                    continue
            if move[1] == "2":
                if len(prev_move) == 1:
                    del new_list[-1]
                    mv = move[0] + "'"
                    new_list.append(mv)
                    prev_move = mv
                    continue
                if prev_move[1] == "'":
                    del new_list[-1]
                    mv = move[0]
                    new_list.append(mv)
                    prev_move = mv
                    continue
                if prev_move[1] == "2":
                    del new_list[-1]
                    prev_move = new_list[-1] if len(new_list) > 0 else ""
                    continue
        new_list.append(move)
        prev_move = move
    return new_list

def putCrossEdge():
    for i in range(3):
        if i==0:
            for j in range(4):
                for k in range(4):
                    if Bottom[1][1] in [Bottom[0][1], Front[2][1]]:
                        return
                    m("f")
                m("u")
        elif i==1:
            if Right[1][2] == Bottom[1][1] or Back[1][0] == Bottom[1][1]:
                m("r' u r f2")
                return
        elif i==2:
            if Left[1][0] == Bottom[1][1] or Back[1][2] == Bottom[1][1]:
                m("l u' l' f2")
                return

def Cross():
    for i in range(4):
        putCrossEdge()
        assert Bottom[1][1] in [Bottom[0][1], Front[2][1]]
        if Front[2][1] == Bottom[1][1]:
            m("f' d r' d'")   #orient if necessary
        m("d")

    #permute to correct face
    condition = False
    while not condition:
        fSame = Front[1][1] == Front[2][1]
        rSame = Right[1][1] == Right[2][1]
        bSame = Back[1][1] == Back[2][1]
        lSame = Left[1][1] == Left[2][1]
        condition = (fSame, rSame, bSame, lSame).count(True) >= 2
        if not condition:
            m("d")
    if (fSame, rSame, bSame, lSame).count(True) == 4:
        return
    assert (fSame, rSame, bSame, lSame).count(True) == 2
    if not fSame and not bSame:
        m("m2 u2 m2") #swap front-back
    elif not rSame and not lSame:
        m("m2 d2 m2") #swap right-left
    elif not fSame and not rSame:
        m("r d r' d' r") #swap front-right
    elif not rSame and not bSame:
        m("r d' r' d r") #swap right-back
    elif not bSame and not lSame:
        m("l' d l d' l'") #swap back-left
    elif not lSame and not fSame:
        m("l' d' l d l'") #swap left-front

    fSame = Front[1][1] == Front[2][1]
    rSame = Right[1][1] == Right[2][1]
    bSame = Back[1][1] == Back[2][1]
    lSame = Left[1][1] == Left[2][1]        
    assert all([fSame, rSame, bSame, lSame])

def ReturnCorners():
    ## gives the 8 right corners
    ## left,right,up
    Uf = [Front[0][2],Right[0][0],Top[2][2]]
    Ul = [Left[0][2],Front[0][0],Top[2][0]]
    Ub = [Back[0][2],Left[0][0],Top[0][0]]
    Ur = [Right[0][2],Back[0][0],Top[0][2]]
    ## left,right,bottom
    Df = [Front[2][2],Right[2][0],Bottom[0][2]]
    Dl = [Left[2][2],Front[2][0],Bottom[0][0]]
    Db = [Back[2][2],Left[2][0],Bottom[2][0]]
    Dr = [Right[2][2],Back[2][0],Bottom[2][2]]
    return [Uf,Ul,Ub,Ur,Df,Dl,Db,Dr]

def ReturnEdges():
    ## upper edges  TOP-FRONT
    Uf = [Top[2][1],Front[0][1]]
    Ul = [Top[1][0],Left[0][1]]
    Ub = [Top[0][1],Back[0][1]]
    Ur = [Top[1][2],Right[0][1]]
    ## middle edges  LEFT-RIGHT
    Mf = [Front[1][2],Right[1][0]]
    Ml = [Left[1][2],Front[1][0]]
    Mb = [Back[1][2],Left[1][0]]
    Mr = [Right[1][2],Back[1][0]]

    return [Uf,Ul,Ub,Ur,Mf,Ml,Mb,Mr]

def F2L_case1():
    ## 24 F2L Top cases ##
    corner = [Front[0][2],Right[0][0],Top[2][2]]
    Edges = ReturnEdges()[0:4]
    F_mid = Front[1][1]
    R_mid = Right[1][1]
    B_mid = Bottom[1][1]

    # B_mid in front #
    if B_mid == corner[0]:
        # [F_mid,R_mid]
        if Edges[3] == [F_mid,R_mid]:
            m("u r u' r'")
        elif Edges[2] == [F_mid,R_mid]:
            m("u' r u r' u2 r u' r'")
        elif Edges[1] == [F_mid,R_mid]:
            m("u' r u2 r' u2 r u' r'")
        elif Edges[0] == [F_mid,R_mid]:
            m("f' u f u2 r u r'")
        # [R_mid,F_mid]
        elif Edges[3] == [R_mid,F_mid]:
            m("u' r u2 r' u f' u' f")
        elif Edges[2] == [R_mid,F_mid]:
            m("u' r u' r' u f' u' f")
        elif Edges[1] == [R_mid,F_mid]:
            m("f' u' f")
        elif Edges[0] == [R_mid,F_mid]:
            m("u f' u f u' f' u' f")
        else:
            return False

    # B_mid in right #
    elif B_mid == corner[1]:
        # [F_mid,R_mid]
        if Edges[3] == [F_mid,R_mid]:
            m("u' r u' r' u r u r'")
        elif Edges[2] == [F_mid,R_mid]:
            m("r u r'")
        elif Edges[1] == [F_mid,R_mid]:
            m("u' r u r' u r u r'")
        elif Edges[0] == [F_mid,R_mid]:
            if [Right[1][2],Back[1][0]] == [R_mid,Back[1][1]] and [Right[2][2],Back[2][0],Bottom[2][2]] == [R_mid,Back[1][1],B_mid]:
                m("r' u2 r2 u r2 u r")
            else:
                m("r' u2 r2 u r'")
        # [R_mid,F_mid]
        elif Edges[3] == [R_mid,F_mid]:
            m("r u' r' u2 f' u' f")
        elif Edges[2] == [R_mid,F_mid]:
            m("u f' u2 f u2 f' u f")
        elif Edges[1] == [R_mid,F_mid]:
            m("u f' u' f u2 f' u f")
        elif Edges[0] == [R_mid,F_mid]:
            m("u' f' u f")
        else:
            return False

    # B_mid in top #
    elif B_mid == corner[2]:
        # [F_mid,R_mid]
        if Edges[3] == [F_mid,R_mid]:
            m("r u2 r' u' r u r'")
        elif Edges[2] == [F_mid,R_mid]:
            m("u r u2 r' u r u' r'")
        elif Edges[1] == [F_mid,R_mid]:
            m("u2 r u r' u r u' r'")
        elif Edges[0] == [F_mid,R_mid]:
            m("r u r' u2 r u r' u' r u r'")
        # [R_mid,F_mid]
        elif Edges[3] == [R_mid,F_mid]:
            m("r u r' u f' u f u' f' u f")
        elif Edges[2] == [R_mid,F_mid]:
            m("u2 f' u' f u' f' u f")
        elif Edges[1] == [R_mid,F_mid]:
            m("u' f' u2 f u' f' u f")
        elif Edges[0] == [R_mid,F_mid]:
            m("f' u2 f u f' u' f")
        else:
            return False

def F2L_case2():
    ## 24 F2L Middle cases ##
    corner = [Front[0][2],Right[0][0],Top[2][2]]
    Edges = ReturnEdges()[4:8]
    F_mid = Front[1][1]
    R_mid = Right[1][1]
    B_mid = Bottom[1][1]

    # B_mid in front #
    if B_mid == corner[0]:
        # [F_mid,R_mid]
        if Edges[3] == [F_mid,R_mid]:
            m("r' u2 r f' u' f")
        elif Edges[2] == [F_mid,R_mid]:
            m("u b' u' b f' u' f")
        elif Edges[1] == [F_mid,R_mid]:
            m("l' u' l u f' u' f")
        elif Edges[0] == [F_mid,R_mid]:
            m("u' f' u' f u2 f' u' f")
        # [R_mid,F_mid]
        elif Edges[3] == [R_mid,F_mid]:
            m("u b u' b' f' u' f")
        elif Edges[2] == [R_mid,F_mid]:
            m("l u' l' u f' u' f")
        elif Edges[1] == [R_mid,F_mid]:
            m("f u f2 u' f")
        elif Edges[0] == [R_mid,F_mid]:
            m("u' r u r' u f' u' f")

    # B_mid in right #
    if B_mid == corner[1]:
        # [F_mid,R_mid]
        if Edges[3] == [F_mid,R_mid]:
            m("r' u r u' f' u f")
        elif Edges[2] == [F_mid,R_mid]:
            m("u' l u l' r u r'")
        elif Edges[1] == [F_mid,R_mid]:
            m("f u2 f' r u r'")
        elif Edges[0] == [F_mid,R_mid]:
            m("u r u r' u2 r u r'")
        # [R_mid,F_mid]
        elif Edges[3] == [R_mid,F_mid]:
            m("r' u' r2 u r'")
        elif Edges[2] == [R_mid,F_mid]:
            m("b' u b u' r u r'")
        elif Edges[1] == [R_mid,F_mid]:
            m("u' l' u l r u r'")
        elif Edges[0] == [R_mid,F_mid]:
            m("u f' u' f u' r u r'")

    # B_mid in top #
    if B_mid == corner[2]:
        # [F_mid,R_mid]
        if Edges[3] == [F_mid,R_mid]:
            m("b' r b2 u' b' u2 r'")
        elif Edges[2] == [F_mid,R_mid]:
            m("u l u2 l' r u2 r' u r u' r'")
        elif Edges[1] == [F_mid,R_mid]:
            m("l f' l2 u l u2 f")
        elif Edges[0] == [F_mid,R_mid]:
            m("r u r' u' r u r' u' r u r'")
        # [R_mid,F_mid]
        elif Edges[3] == [R_mid,F_mid]:
            m("u' r' u r2 u' r'")
        elif Edges[2] == [R_mid,F_mid]:
            m("u2 l u2 l' f' u f")
        elif Edges[1] == [R_mid,F_mid]:
            m("u f u' f2 u f")
        elif Edges[0] == [R_mid,F_mid]:
            m("r u' r' u f' u f")

def CheckF2L():
    corner = [Front[2][2],Right[2][0],Bottom[0][2]]
    c_check = [Front[1][1],Right[1][1],Bottom[1][1]]
    edge = [Front[1][2],Right[1][0]]
    e_check = [Front[1][1],Right[1][1]]

    if corner == c_check and edge == e_check:
        return True
    else:
        return False

def F2L_corner():
    c1 = Front[1][1]
    c2 = Right[1][1]
    c3 = Bottom[1][1]

    corners = ReturnCorners()
    for i in corners:
        if (c1 in i) and (c2 in i) and (c3 in i):
            corner = i
            break

    if corner == corners[1]:
        m("u'")
    elif corner == corners[2]:
        m("u2")
    elif corner == corners[3]:
        m("u")
    elif corner == corners[4]:
        m("r u' r'")
    elif corner == corners[5]:
        m("l' u' l")
    elif corner == corners[6]:
        m("l u2 l'")
    elif corner == corners[7]:
        m("r' u r u")

def SolveF2L():
    for i in range(4):
        if CheckF2L() == False:
            F2L_corner()
            f2l = F2L_case1()
            if f2l == False:
                F2L_case2()
        m("y")
    m("y'")


def TopCross():
    if Top[0][1] == Top[1][0] == Top[1][2] == Top[2][1] == Top[1][1]:
        return

    else:
        while not(Top[0][1] == Top[1][0] == Top[1][2] == Top[2][1] == Top[1][1]):
            if Top[1][0] == Top[1][2] == Top[1][1]:
                m("f r u r' u' f'") ## vertical_line
            elif Top[0][1] == Top[1][0] == Top[1][1]:
                m("f u r u' r' f'") ## L case
            elif Top[1][1] not in [Top[0][1],Top[1][0],Top[1][2],Top[2][1]]:
                m("f u r u' r' f' u f r u r' u' f'") ## Dot Case
            else:
                m("u")

def OLL_case():
    ## oll cases when top cross is completed ##
    if Top[0][1] == Top[1][0] == Top[1][2] == Top[2][1] == Top[1][1]:
        ## 2 missing ##
        if (Front[0][0] == Front[0][2] == Top[1][1]) and (Top[0][0] == Top[0][2] == Top[1][1]):
            m("r2 d r' u2 r d' r' u2 r'")
        elif (Right[0][0] == Left[0][2] == Top[1][1]) and (Top[0][0] == Top[0][2] == Top[1][1]):
            m("f r b' r' f' r b r'")
        elif (Front[0][0] == Right[0][2] == Top[1][1]) and (Top[0][0] == Top[2][2] == Top[1][1]):
            m("r' f r b' r' f' r b")

        ## 3 missing ##
        elif (Front[0][2] == Right[0][2] == Back[0][2] == Top[1][1]) and (Top[2][0] == Top[1][1]):
            m("r u r' u r u2 r'")
        elif (Front[0][0] == Right[0][0] == Left[0][0] == Top[1][1]) and (Top[0][2] == Top[1][1]):
            m("r u2 r' u' r u' r'")

        ## 4 missing ##
        elif Top[1][1] not in [Top[0][0],Top[0][2],Top[2][0],Top[2][2]]:
            if Right[0][0] == Right[0][2] == Left[0][0] == Left[0][2] == Top[1][1]:
                m("r u r' u r u' r' u r u2 r'")
            elif Front[0][0] == Front[0][2] == Back[0][0] == Back[0][2] == Top[1][1]:
                m("f r u r' u' r u r' u' r u r' u' f'")
            elif Left[0][0] == Left[0][2] == Front[0][2] == Back[0][0] == Top[1][1]:
                m("r u2 r2 u' r2 u' r2 u2 r")

def SolveOLL():
    while (Top != [[Top[1][1],Top[1][1],Top[1][1]],[Top[1][1],Top[1][1],Top[1][1]],[Top[1][1],Top[1][1],Top[1][1]]]):
        m("u")
        OLL_case()


def PLL_case1():
    corners = ReturnCorners()[0:4]
    Edges = ReturnEdges()[0:4]
    
    mid = Top[1][1]
    f_mid = Front[1][1]
    r_mid = Right[1][1]
    l_mid = Left[1][1]
    b_mid = Back[1][1]

    ## Edge Permutations ##
    if corners[0] == [f_mid,r_mid,mid] and corners[1] == [l_mid,f_mid,mid] and corners[2] == [b_mid,l_mid,mid] and corners[3] == [r_mid,b_mid,mid]:
        if [Edges[0][1],Edges[1][1],Edges[2][1],Edges[3][1]] == [b_mid,r_mid,f_mid,l_mid]:
            m("m2 u m2 u2 m2 u m2")
        elif [Edges[0][1],Edges[1][1],Edges[2][1],Edges[3][1]] == [r_mid,b_mid,l_mid,f_mid]:
            m("m2 u m2 u m u2 m2 u2 m u2")
        elif [Edges[0][1],Edges[1][1],Edges[2][1],Edges[3][1]] == [l_mid,r_mid,b_mid,f_mid]:
            m("r2 u r u r' u' r' u' r' u r'")
        elif [Edges[0][1],Edges[1][1],Edges[2][1],Edges[3][1]] == [r_mid,f_mid,b_mid,l_mid]:
            m("r u' r u r u r u' r' u' r2")
        else:
            return False

    ## Corner Permutations ##
    elif [Edges[0][1],Edges[1][1],Edges[2][1],Edges[3][1]] == [f_mid,l_mid,b_mid,r_mid]:
        if (corners[1] == [l_mid,f_mid,mid]) and (corners[0] == [b_mid,l_mid,mid] and corners[2] == [r_mid,b_mid,mid] and corners[3] == [f_mid,r_mid,mid]):
            m("x' r' d r' u2 r d' r' u2 r2")
        elif (corners[1] == [l_mid,f_mid,mid]) and (corners[0] == [r_mid,b_mid,mid] and corners[2] == [f_mid,r_mid,mid] and corners[3] == [b_mid,l_mid,mid]):
            m("x' r2 u2 r d r' u2 r d' r")
        elif [corners[0][1],corners[1][0],corners[2][1],corners[3][0]] == [f_mid,f_mid,b_mid,b_mid]:
                m("r d r' u r d' r' u' r d r' u' r d' r' u' r d r' u r d' r' u")
        else:
            return False
    else:
        return False

def PLL_case2():
    ## Corner and edge permutations ##
    f = Front[1][1]
    r = Right[1][1]
    l = Left[1][1]
    b = Back[1][1]
    
    ## Swap One Set of Adjacent Corners ##
    if Front[0] == [f,f,r] and Left[0] == [l,b,l] and Back[0] == [r,l,b] and Right[0] == [b,r,f]:
        m("r u' r' u' r u r d r' u' r d' r' u2 r' u'")
    elif Front[0] == [f,r,f] and Left[0] == [b,l,l] and Back[0] == [l,b,r] and Right[0] == [r,f,b]:
        m("r' u2 r u2 r' f r u r' u' r' f' r2 u'")
    elif Front[0] == [f,f,f] and Left[0] == [b,b,l] and Back[0] == [l,l,r] and Right[0] == [r,r,b]:
        m("r' u l' u2 r u' r' u2 r l u'")
    elif Front[0] == [f,r,r] and Left[0] == [l,l,l] and Back[0] == [r,b,b] and Right[0] == [b,f,f]:
        m("r u r' f' r u r' u' r' f r2 u' r' u'")
    elif Front[0] == [f,f,r] and Left[0] == [l,r,l] and Back[0] == [r,b,b] and Right[0] == [b,l,f]:
        m("r u r' u' r' f r2 u' r' u' r u r' f'")
    elif Front[0] == [r,f,l] and Left[0] == [l,r,f] and Back[0] == [b,b,b] and Right[0] == [f,l,r]:
        m("r' u2 r' u' y r' f' r2 u' r' u r' f r u' f")

    ## Swap One Set of Diagonal Corners ##
    elif Front[0] == [f,f,b] and Left[0] == [r,l,l] and Back[0] == [b,r,f] and Right[0] == [l,b,r]:
        m("r' u r' u' y r' f' r2 u' r' u r' f r f")
    elif Front[0] == [f,f,b] and Left[0] == [r,b,l] and Back[0] == [b,l,f] and Right[0] == [l,r,r]:
        m("f r u' r' u' r u r' f' r u r' u' r' f r f'")
    elif Front[0] == [b,f,f] and Left[0] == [l,r,r] and Back[0] == [f,b,b] and Right[0] == [r,l,l]:
        m("r u r' u r u r' f' r u r' u' r' f r2 u' r' u2 r u' r'")
    elif Front[0] == [f,f,b] and Left[0] == [r,r,l] and Back[0] == [b,b,f] and Right[0] == [l,l,r]:
        m("r' u r u' r' f' u' f r u r' f r' f' r u' r")

    ## G Permutations (Double cycles) ##
    elif Front[0] == [l,f,f] and Left[0] == [b,r,b] and Back[0] == [f,l,r] and Right[0] == [r,b,l]:
        m("r2 u r' u r' u' r u' r2 d u' r' u r d' u")    
    elif Front[0] == [b,f,f] and Left[0] == [f,b,r] and Back[0] == [l,r,l] and Right[0] == [r,l,b]:
        m("y' d r' u' r u d' r2 u r' u r u' r u' r2' u'")
    elif Front[0] == [r,l,b] and Left[0] == [f,r,f] and Back[0] == [b,b,l] and Right[0] == [l,f,r]:
        m("r2 u' r u' r u r' u r2 d' u r u' r' d u'")
    elif Front[0] == [l,b,f] and Left[0] == [b,f,b] and Back[0] == [f,l,r] and Right[0] == [r,r,l]:
        m("d' r u r' u' d r2 u' r u' r' u r' u r2 u")

    else:
        return False

def CubeSolved():
    faces = [Top,Front,Back,Right,Left,Bottom]

    for i in range(6):
        for j in range(3):
            for k in range(3):
                if faces[i][j][k] != faces[i][1][1]:
                    return False

def SolvePLL():
    for i in range(4):
        for j in range(4):
            case1 = PLL_case1()
            if case1 == False:
                case2 = PLL_case2()
                if case2 == False:
                    case3 = CubeSolved()
                    if case3 != False:
                        return
                else:
                    return
            else:
                return
            m("u")
        m("y")

def Solution():
    global MovesList

    moves = ""
    for i in range(len(MovesList)):
        moves += MovesList[i]
        moves+=" "

    return moves
            
def SolveCube():
    global MovesList
    
    Cross()
    MovesList = simplify_moves(MovesList)

    SolveF2L()
    MovesList = simplify_moves(MovesList)

    TopCross()
    MovesList = simplify_moves(MovesList)

    SolveOLL()
    MovesList = simplify_moves(MovesList)

    SolvePLL()
    MovesList = simplify_moves(MovesList)

    return Solution(),len(MovesList)
