from tkinter import *
import random
# back #666666 button black #4c4c4c salmon #ff9a81 orange #ed9916
syntax = []
disp1 = []
disp2 = []
disp3 = []

def NASA():
    global base
    global lsyn
    global dissyntax
    global matc
    base = Tk()
    base.title('Matrix Calculator')
    base.geometry('700x500')
    base.config(background = '#32353e')
    base.resizable(0,0)
    dissyntax = StringVar()

    genpanel()



    Label(base, text = 'MATRIX A', font = ('Arial', 15), background = '#32353e', foreground = '#4380b0').place(x = 15, y = 11)
    Label(base, text = 'MATRIX B', font = ('Arial', 15), background = '#32353e', foreground = '#4380b0').place(x = 250, y = 11)

    matc = Label(base, text = 'RESULT', font = ('Arial', 15), background = '#32353e', foreground = '#4380b0')
    matc.place(x = 485, y = 11)

    lsyn = Entry(base, textvariable = dissyntax, font = ('Arial', 15), relief = 'flat', background = '#060912', width = 50, foreground = '#4380b0')
    lsyn.place(x = 70, y = 267)    
    

    Button(text = 'Addition', font = ('Arial', 15), height = 1, width = 20, background = '#29455b', foreground = 'white', relief = 'flat', command = addop).place (x = 70, y = 320)
    Button(text = 'Subtraction', font = ('Arial', 15), height = 1, width = 20, background = '#29455b', foreground = 'white', relief = 'flat', command = subop).place (x = 70, y = 370)
    Button(text = 'Multiplication', font = ('Arial', 15), height = 1, width = 20, background = '#29455b', foreground = 'white', relief = 'flat', command = mulop).place (x = 70, y = 420)
    
    Button(text = '1', font = ('Arial', 15), height = 1, width = 3, background = '#4c4c4c', foreground = 'white', relief = 'flat', command = in1).place (x = 325, y = 320)
    Button(text = '2', font = ('Arial', 15), height = 1, width = 3, background = '#4c4c4c', foreground = 'white', relief = 'flat', command = in2).place (x = 325, y = 370)
    Button(text = '3', font = ('Arial', 15), height = 1, width = 3, background = '#4c4c4c', foreground = 'white', relief = 'flat', command = in3).place (x = 325, y = 420)
    Button(text = '4', font = ('Arial', 15), height = 1, width = 3, background = '#4c4c4c', foreground = 'white', relief = 'flat', command = in4).place (x = 380, y = 320)
    Button(text = '5', font = ('Arial', 15), height = 1, width = 3, background = '#4c4c4c', foreground = 'white', relief = 'flat', command = in5).place (x = 380, y = 370)

    Button(text = 'Calculate', font = ('Arial', 15), height = 1, width = 15, background = '#3a668b', foreground = 'white', relief = 'flat', command = calc).place (x = 446, y = 320)
    Button(text = 'Reset', font = ('Arial', 15), height = 1, width = 15, background = '#ed9916', foreground = 'white', relief = 'flat', command = res).place (x = 446, y = 370)
    
    base.mainloop()
#BUTTON FUNCTIONS ----------------------------------------------------------------------------------------------------------------------------------
#Concatenate lsyn
def concatenatesyn (h):
    dissyntax.set('{}'.format(h))

def op (o,h):
    if len(syntax) == 0:
        syntax.append('Operation:')
        syntax.append(o)
        syntax.append('Column:')
        concatenatesyn(h)
        print(syntax)   
    else:
        concatenatesyn('invalid input')
        print('invalid input')
#Button add
def addop ():
    op('Addition,','Operation: Addition')
#Button Sub
def subop ():
    op('Subtraction,','Operation: Subtraction')
#Button Mul
def mulop ():
    op('Multiplication,','Operation: Multiplication')
#Button Num
def buttonnum (x,y):
    if len(syntax) > 0:
        if syntax[1] != 'Multiplication,':
            if len(syntax) == 3:
                syntax.append(x)
                syntax.append('Row:')
                concatenatesyn('Matrix A and Matrix B - Column: {}'.format(y))
                print(syntax)
            elif len(syntax) == 5:
                syntax.append(x)
                concatenatesyn('Matrix A and Matrix B - Row: {}'.format(y))
                print(syntax)
            elif len(syntax) == 6:
                concatenatesyn('invalid input')
                print('invalid input')

        if syntax[1] == 'Multiplication,':
            if len(syntax) == 3:
                syntax.append(x)
                syntax.append('Row:')
                concatenatesyn('Matrix A - Column: {}'.format(y))
                print(syntax)
            elif len(syntax) == 5:
                syntax.append(x)
                syntax.append('Column:')
                concatenatesyn('Matrix A - Row: {}'.format(y))
                print(syntax)
            elif len(syntax) == 7:
                syntax.append(x)
                syntax.append('Row:')
                concatenatesyn('Matrix B - Column: {}'.format(y))
                print(syntax)
            elif len(syntax) == 9:
                syntax.append(x)
                concatenatesyn('Matrix B - Row: {}'.format(y))
                print(syntax)
            elif len(syntax) == 10:
                concatenatesyn('invalid input')
                print('invalid input')
    else:
        concatenatesyn('invalid input')
        print('invalid input')
#Button1
def in1 ():
    buttonnum(1,'1')
#Button2
def in2 ():
    buttonnum(2,'2')
#Button 3
def in3 ():
    buttonnum(3,'3')
#Button 4
def in4 ():
    buttonnum(4,'4')
#Button 5
def in5 ():
    buttonnum(5,'5')
#ButtonReset
def res ():
    syntax.clear()
    lsyn.delete(0, 'end')
    print(syntax)
    matc.config(text = 'RESULT')
    if len(syntax) == 6 or len(syntax) == 10:
        a1.destroy()
        a2.destroy()
        a3.destroy()
    
    

    panel1.destroy()
    panel2.destroy()
    panel3.destroy()

    disp1.clear()
    disp2.clear()
    disp3.clear()

    
#GENERATE PANELS
def genpanel ():
    global panel1
    global panel2
    global panel3
    panel1 = PanedWindow(base, background = '#32353e', height = 200, width = 200)
    panel2 = PanedWindow(base, background = '#32353e', height = 200, width = 200)
    panel3 = PanedWindow(base, background = '#32353e', height = 200, width = 200)
       
    panel1.place(x = 15, y = 40)
    panel2.place(x = 250, y = 40)
    panel3.place(x = 485, y = 40)
#ADD SUB MATRIX GENERATE---------------------------------------------------------------------------------------------------------
def addsubrandomgenerate ():
    global aa
    global bb
    aa = []
    bb = []
    for a in range (syntax[3]):
        aa.append(random.randint(10,20))
        bb.append(random.randint(10,20))
#Appending by rows
def addsubgenerate():
    for a in range (syntax[5]):
        addsubrandomgenerate()
        disp1.append(aa)
        disp2.append(bb)

    print('MATRIX A')
    for b in range (syntax[5]):
        print(disp1[b])

    print('MATRIX B')
    for b in range (syntax[5]):
        print(disp2[b])

#Generate Random MUL
def mulrandomgenerate ():
    global aa
    global bb
    aa = []
    bb = []
    for a in range (syntax[3]):
        aa.append(random.randint(10,20))
    for a in range (syntax[7]):
        bb.append(random.randint(10,20))
#Appending by rows MUL
def mulgenerate ():
    for a in range (syntax[5]):
        mulrandomgenerate()
        disp1.append(aa)
    for a in range (syntax[9]):
        mulrandomgenerate()
        disp2.append(bb)

    print('MATRIX A')
    for b in range (len(disp1)):
        print(disp1[b])

    print('MATRIX B')
    for b in range (len(disp2)):
        print(disp2[b])

#Generate Product
def genrandproduct ():
    global aaa
    aaa = []
    for a in range (len(disp2[0])):
        aaa.append(int(0))

def genproductmatrix():
    for a in range (len(disp1)):
        genrandproduct()
        disp3.append(aaa)
#ADD
def add():
    for a in range (len(disp1)):
        ch = []
        for b in range (len(disp1[0])):
            solved = disp1[a][b] + disp2[a][b]
            ch.append(solved)
        disp3.append(ch)
 
    print('ADD RESULT')
    for b in range (syntax[5]):
        print(disp3[b])        
#SUB
def sub():
    for a in range (len(disp1)):
        ch = []
        for b in range (len(disp1[0])):
            solved = disp1[a][b] - disp2[a][b]
            ch.append(solved)
        disp3.append(ch)
 
    print('SUB RESULT')
    for b in range (syntax[5]):
        print(disp3[b])
#MUL
def mul():
    for a in range (len(disp1)):
        for b in range (len(disp2[0])):
            for c in range (len(disp2)):
                disp3[a][b] += disp1[a][c] * disp2[c][b]

    print('MUL RESULT')
    for b in range (len(disp1)):
        print(disp3[b])

#DISPLAY MATRIX
def displaymatrix ():
    global a1
    global a2
    global a3
    genpanel()

    for a in range (len(disp1)):
        a1 = Label(panel1, text = (disp1[a]), font = ('Arial', 20), foreground = 'white', background = '#32353e')
        a1.pack()
    for a in range (len(disp2)):
        a2 = Label(panel2, text = (disp2[a]), font = ('Arial', 20), foreground = 'white', background = '#32353e')
        a2.pack()
    for a in range (len(disp3)):
        a3 = Label(panel3, text = (disp3[a]), font = ('Arial', 20), foreground = 'white', background = '#32353e')
        a3.pack() 

#lisa = [[76,26,37,58,59],[43,67,57,48,78],[57,48,59,67,67],[43,67,57,48,78],[76,26,37,58,59]]
#def show():
#    for b in range (len(lisa)):
#        a1 = Label(panel3, text = (lisa[b]), font = ('Arial', 20), foreground = 'white', background = 'black').pack()



def calc ():
    
    if len(syntax) == 6 and syntax[1] == 'Addition,':
        addsubgenerate()
        add()
        displaymatrix()
        matc.config(text = 'MATRIX A+B')
    elif len(syntax) == 6 and syntax[1] == 'Subtraction,':
        addsubgenerate()
        sub()
        displaymatrix()
        matc.config(text = 'MATRIX A-B')
    elif len(syntax) == 10 and syntax[1] == 'Multiplication,':
        if syntax[3] == syntax[9]:
            mulgenerate()
            genproductmatrix()
            mul()
            displaymatrix()
            matc.config(text = 'MATRIX A*B')
        else:
            concatenatesyn('Matrix A Column != Matrix B Row')
            print('invalid input')
    else:
        concatenatesyn('invalid input')
        print('invalid input')
    
    syntax.clear()


NASA()