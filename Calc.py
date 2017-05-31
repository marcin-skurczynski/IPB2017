from __future__ import division
from Tkinter import *
import tkMessageBox
import math

################################ BUTTON CLICK FUNCTIONS ################################
def ButtonClick(numbers):
    global operator
    operator = operator + str(numbers)
    display_input.set(operator)

def ButtonClear():
    global operator
    operator = ""
    display_input.set("")

def ButtonEqual():
    global operator
    sumup = str(eval(operator))
    display_input.set(sumup)
    #operator = ""

def ButtonPOW():
    global operator
    sumup = str(eval(operator))
    sumup = float(sumup)
    power = math.pow(sumup,2)
    display_input.set(power)

def ButtonSQRT():
    global operator
    sumup = str(eval(operator))
    sumup = float(sumup)
    sqrt = math.sqrt(sumup)
    display_input.set(sqrt)

def ButtonBSPC():
    global operator
    operator = operator[:-1]
    display_input.set(operator)

def ButtonLN():
    global operator
    sumup = str(eval(operator))
    sumup = float(sumup)
    ln = math.log(sumup)
    display_input.set(ln)

def ButtonSIN():
    global operator
    sumup = str(eval(operator))
    sumup = float(sumup)
    sumup = math.radians(sumup)
    sin = math.sin(sumup)
    display_input.set(sin)

def ButtonCOS():
    global operator
    sumup = str(eval(operator))
    sumup = float(sumup)
    sumup = math.radians(sumup)
    cos = math.cos(sumup)
    display_input.set(cos)

def ButtonTG():
    global operator
    sumup = str(eval(operator))
    sumup = float(sumup)
    if sumup == 90:
        display_input.set('Does not exist')

    else:
        sumup = math.radians(sumup)
        tan = math.tan(sumup)
        display_input.set(tan)

def ButtonCTG():
    global operator
    sumup = str(eval(operator))
    sumup = float(sumup)
    if sumup == 0:
        display_input.set('Does not exist')

    elif sumup == 90:
        display_input.set('0.0')

    else:        
        sumup = math.radians(sumup)
        ctan = 1/math.tan(sumup)
        display_input.set(ctan)


def ButtonLESS():

    root.geometry('416x423')
    
    button18 = Button(root, relief = RIDGE, activebackground = 'white', padx = 0, pady = 0, border = 2, text = 'M\nO\nR\nE\n\nO\nP\nT\nI\nO\nN\nS', fg = 'black', bg = 'white',
                 font = ('Serif', 15), command = lambda: ButtonMORE())
    button18.grid(
                     row = 1,
                     column = 4,
                     columnspan = 1,
                     rowspan = 5,
                     sticky = N+S+W+E)

    def Highlight(event):
        button18.configure(bg = 'light grey')
    def unHighlight(event):
        button18.configure(bg = 'white')
    button18.bind('<Enter>', Highlight)
    button18.bind('<Leave>', unHighlight)
    
def ButtonMORE():

    root.geometry('547x423')

    buttonPI = Button(root, relief = FLAT, activebackground = 'white', padx = 7, pady = 5, border = 3, text = 'π', fg = 'black', bg = 'white',
                 font =('Serif', 20),command = lambda: ButtonClick('pi'))
    buttonPI.grid(
                     row = 1,
                     column = 4,
                     columnspan = 1,
                     sticky = W+E+N+S)

    def Highlight(event):
        buttonPI.configure(bg = 'light grey')
    def unHighlight(event):
        buttonPI.configure(bg = 'white')
    buttonPI.bind('<Enter>', Highlight)
    buttonPI.bind('<Leave>', unHighlight)
    

    buttonPOW = Button(root, relief = FLAT, activebackground = 'white', padx = 0, pady = 5, border = 3, text = 'x^2', fg = 'black', bg = 'white',
                 font =('Serif', 20),command = lambda: ButtonPOW())
    buttonPOW.grid(
                     row = 2,
                     column = 4,
                     columnspan = 1,
                     sticky = W+E+N+S)

    def Highlight(event):
        buttonPOW.configure(bg = 'light grey')
    def unHighlight(event):
        buttonPOW.configure(bg = 'white')
    buttonPOW.bind('<Enter>', Highlight)
    buttonPOW.bind('<Leave>', unHighlight)
    
    
    buttonSQRT = Button(root, relief = FLAT, activebackground = 'white', padx = 0, pady = 5, border = 3, text = 'sqrt', fg = 'black', bg = 'white',
                 font =('Serif', 20),command = lambda: ButtonSQRT())
    buttonSQRT.grid(
                     row = 3,
                     column = 4,
                     columnspan = 1,
                     sticky = W+E+N+S)

    def Highlight(event):
        buttonSQRT.configure(bg = 'light grey')
    def unHighlight(event):
        buttonSQRT.configure(bg = 'white')
    buttonSQRT.bind('<Enter>', Highlight)
    buttonSQRT.bind('<Leave>', unHighlight)

    button20 = Button(root, relief = FLAT, activebackground = 'white', padx = 0, pady = 5, border = 3, text = '(', fg = 'black', bg = 'white',
                 font =('Serif', 20),command = lambda: ButtonClick('('))
    button20.grid(
                     row = 4,
                     column = 4,
                     columnspan = 1,
                     sticky = W+E+N+S)

    def Highlight(event):
        button20.configure(bg = 'light grey')
    def unHighlight(event):
        button20.configure(bg = 'white')
    button20.bind('<Enter>', Highlight)
    button20.bind('<Leave>', unHighlight)
    
    
    button21 = Button(root, relief = FLAT, activebackground = 'white', padx = 0, pady = 5, border = 3, text = ')', fg = 'black', bg = 'white',
                 font =('Serif', 20),command = lambda: ButtonClick(')'))
    button21.grid(
                     row = 5,
                     column = 4,
                     columnspan = 1,
                     sticky = W+E+N+S)

    def Highlight(event):
        button21.configure(bg = 'light grey')
    def unHighlight(event):
        button21.configure(bg = 'white')
    button21.bind('<Enter>', Highlight)
    button21.bind('<Leave>', unHighlight)


def About():
    tkMessageBox.showinfo("About Calculator", "This calculator was made using informations mostly from:\n"
                          "- tutorialspoint.com\n"
                          "- docs.python.org\n"
                          "- stackoverflow.com\n\n\n"
                          "                THANK YOU FOR USING THIS APP :)             \n"
                          "                   Application made for IPB Classes            ")

################################        G U I          ################################
root = Tk()
root.title('Calculator')
root.geometry('416x423')
root.resizable(0,0)

operator=""
pi = math.pi

#DISPLAY
display_input = StringVar()
display = Entry(root, relief = FLAT, textvariable = display_input, bd = '15', font = ('Arial', '20'),insertwidth = 4, justify = 'right').grid(
    row = 0,
    columnspan = 4,
    sticky = "")

#FIRST LINE OF BUTTONS
button1 = Button(root, relief = FLAT, activebackground = 'white', padx = 7, pady = 5, border = 3, text = 'C', fg = 'blue', bg = 'white',
                 font =('Serif', 20,'bold'),command = lambda: ButtonClear())
button1.grid(
                     row = 1,
                     column = 0,
                     columnspan = 1,
                     sticky = W+E+N+S)

def Highlight(event):
    button1.configure(bg = 'light grey')
def unHighlight(event):
    button1.configure(bg = 'white')
button1.bind('<Enter>', Highlight)
button1.bind('<Leave>', unHighlight)


button2 = Button(root, relief = FLAT, activebackground = 'white', padx = 13, pady = 5, border = 3, text = '/', fg = 'blue', bg = 'white',
                 font = ('Serif', 20, 'bold'), command = lambda: ButtonClick('/'))
button2.grid(
                     row = 1,
                     column = 1,
                     columnspan = 1,
                     sticky = W+E+N+S)

def Highlight(event):
    button2.configure(bg = 'light grey')
def unHighlight(event):
    button2.configure(bg = 'white')
button2.bind('<Enter>', Highlight)
button2.bind('<Leave>', unHighlight)


button3 = Button(root, relief = FLAT, activebackground = 'white', padx = 13, pady = 5, border = 3, text = '*', fg = 'blue', bg = 'white',
                 font = ('Serif', 20, 'bold'), command = lambda: ButtonClick('*'))
button3.grid(
                     row = 1,
                     column = 2,
                     columnspan = 1,
                     sticky = W+E+N+S)

def Highlight(event):
    button3.configure(bg = 'light grey')
def unHighlight(event):
    button3.configure(bg = 'white')
button3.bind('<Enter>', Highlight)
button3.bind('<Leave>', unHighlight)


button4 = Button(root, relief = FLAT, activebackground = 'white', padx = 13, pady = 5, border = 3, text = '-', fg = 'blue', bg = 'white',
                 font = ('Serif', 20, 'bold'), command = lambda: ButtonClick('-'))
button4.grid(
                     row = 1,
                     column = 3,
                     columnspan = 1,
                     sticky = W+E+N+S)

def Highlight(event):
    button4.configure(bg = 'light grey')
def unHighlight(event):
    button4.configure(bg = 'white')
button4.bind('<Enter>', Highlight)
button4.bind('<Leave>', unHighlight)


#SECOND LINE OF BUTTONS
button5 = Button(root, relief = FLAT, activebackground = 'white', padx = 10, pady = 5, border = 3, text = '7', fg = 'black', bg = 'white',
                 font = ('Serif', 20, 'bold'), command = lambda: ButtonClick(7))
button5.grid(
                     row = 2,
                     column = 0,
                     columnspan = 1,
                     sticky = W+E+N+S)

def Highlight(event):
    button5.configure(bg = 'light grey')
def unHighlight(event):
    button5.configure(bg = 'white')
button5.bind('<Enter>', Highlight)
button5.bind('<Leave>', unHighlight)


button6 = Button(root, relief = FLAT, activebackground = 'white', padx = 10, pady = 5, border = 3, text = '8', fg = 'black', bg = 'white',
                 font = ('Serif', 20, 'bold'), command = lambda: ButtonClick(8))
button6.grid(
                     row = 2,
                     column = 1,
                     columnspan = 1,
                     sticky = W+E+N+S)

def Highlight(event):
    button6.configure(bg = 'light grey')
def unHighlight(event):
    button6.configure(bg = 'white')
button6.bind('<Enter>', Highlight)
button6.bind('<Leave>', unHighlight)


button7 = Button(root, relief = FLAT, activebackground = 'white', padx = 10, pady = 5, border = 3, text = '9', fg = 'black', bg = 'white',
                 font = ('Serif', 20, 'bold'), command = lambda: ButtonClick(9))
button7.grid(
                     row = 2,
                     column = 2,
                     columnspan = 1,
                     sticky = W+E+N+S)

def Highlight(event):
    button7.configure(bg = 'light grey')
def unHighlight(event):
    button7.configure(bg = 'white')
button7.bind('<Enter>', Highlight)
button7.bind('<Leave>', unHighlight)


button8 = Button(root, relief = FLAT, activebackground = 'white', padx = 10, pady = 45, border = 3, text = '+', fg = 'blue', bg = 'white',
                 font = ('Serif', 20, 'bold'), command = lambda: ButtonClick('+'))
button8.grid(
                     row = 2,
                     column = 3,
                     columnspan = 1,
                     rowspan = 2,
                     sticky = W+E+N+S)

def Highlight(event):
    button8.configure(bg = 'light grey')
def unHighlight(event):
    button8.configure(bg = 'white')
button8.bind('<Enter>', Highlight)
button8.bind('<Leave>', unHighlight)


#THIRD LINE OF BUTTONS
button9 = Button(root, relief = FLAT, activebackground = 'white', padx = 10, pady = 5, border = 3, text = '4', fg = 'black', bg = 'white',
                 font = ('Serif', 20, 'bold'), command = lambda: ButtonClick(4))
button9.grid(
                     row = 3,
                     column = 0,
                     columnspan = 1,
                     sticky = W+E+N+S)

def Highlight(event):
    button9.configure(bg = 'light grey')
def unHighlight(event):
    button9.configure(bg = 'white')
button9.bind('<Enter>', Highlight)
button9.bind('<Leave>', unHighlight)


button10 = Button(root, relief = FLAT, activebackground = 'white', padx = 10, pady = 5, border = 3, text = '5', fg = 'black', bg = 'white',
                 font = ('Serif', 20, 'bold'), command = lambda: ButtonClick(5))
button10.grid(
                     row = 3,
                     column = 1,
                     columnspan = 1,
                     sticky = W+E+N+S)

def Highlight(event):
    button10.configure(bg = 'light grey')
def unHighlight(event):
    button10.configure(bg = 'white')
button10.bind('<Enter>', Highlight)
button10.bind('<Leave>', unHighlight)


button11 = Button(root, relief = FLAT, activebackground = 'white', padx = 10, pady = 5, border = 3, text = '6', fg = 'black', bg = 'white',
                 font = ('Serif', 20, 'bold'), command = lambda: ButtonClick(6))
button11.grid(
                     row = 3,
                     column = 2,
                     columnspan = 1,
                     sticky = W+E+N+S)

def Highlight(event):
    button11.configure(bg = 'light grey')
def unHighlight(event):
    button11.configure(bg = 'white')
button11.bind('<Enter>', Highlight)
button11.bind('<Leave>', unHighlight)


#FOURTH LINE OF BUTTONS
button12 = Button(root, relief = FLAT, activebackground = 'white', padx = 10, pady = 5, border = 3, text = '1', fg = 'black', bg = 'white',
                 font = ('Serif', 20, 'bold'), command = lambda: ButtonClick(1))
button12.grid(
                     row = 4,
                     column = 0,
                     columnspan = 1,
                     sticky = W+E+N+S)

def Highlight(event):
    button12.configure(bg = 'light grey')
def unHighlight(event):
    button12.configure(bg = 'white')
button12.bind('<Enter>', Highlight)
button12.bind('<Leave>', unHighlight)


button13 = Button(root, relief = FLAT, activebackground = 'white', padx = 10, pady = 5, border = 3, text = '2', fg = 'black', bg = 'white',
                 font = ('Serif', 20, 'bold'), command = lambda: ButtonClick(2))
button13.grid(
                     row = 4,
                     column = 1,
                     columnspan = 1,
                     sticky = W+E+N+S)

def Highlight(event):
    button13.configure(bg = 'light grey')
def unHighlight(event):
    button13.configure(bg = 'white')
button13.bind('<Enter>', Highlight)
button13.bind('<Leave>', unHighlight)


button14 = Button(root, relief = FLAT, activebackground = 'white', padx = 10, pady = 5, border = 3, text = '3', fg = 'black', bg = 'white',
                 font = ('Serif', 20, 'bold'), command = lambda: ButtonClick(3))
button14.grid(
                     row = 4,
                     column = 2,
                     columnspan = 1,
                     sticky = W+E+N+S)

def Highlight(event):
    button14.configure(bg = 'light grey')
def unHighlight(event):
    button14.configure(bg = 'white')
button14.bind('<Enter>', Highlight)
button14.bind('<Leave>', unHighlight)


button15 = Button(root, relief = FLAT, activebackground = 'white', padx = 10, pady = 45, border = 3, text = '=', fg = 'blue', bg = 'white',
                 font = ('Serif', 20, 'bold'), command = lambda: ButtonEqual())
button15.grid(
                     row = 4,
                     column = 3,
                     columnspan = 1,
                     rowspan = 2,
                     sticky = W+E+N+S)

def Highlight(event):
    button15.configure(bg = 'light grey')
def unHighlight(event):
    button15.configure(bg = 'white')
button15.bind('<Enter>', Highlight)
button15.bind('<Leave>', unHighlight)


#FIFTH LINE OF BUTTONS
button16 = Button(root, relief = FLAT, activebackground = 'white', padx = 52, pady = 5, border = 3, text = '0', fg = 'black', bg = 'white',
                 font = ('Serif', 20, 'bold'), command = lambda: ButtonClick(0))
button16.grid(
                     row = 5,
                     column = 0,
                     columnspan = 2,
                     sticky = W+E+N+S)

def Highlight(event):
    button16.configure(bg = 'light grey')
def unHighlight(event):
    button16.configure(bg = 'white')
button16.bind('<Enter>', Highlight)
button16.bind('<Leave>', unHighlight)


button17 = Button(root, relief = FLAT, activebackground = 'white', padx = 13, pady = 5, border = 3, text = '.', fg = 'black', bg = 'white',
                 font = ('Serif', 20, 'bold'), command = lambda: ButtonClick('.'))
button17.grid(
                     row = 5,
                     column = 2,
                     columnspan = 1,
                     sticky = W+E+N+S)

def Highlight(event):
    button17.configure(bg = 'light grey')
def unHighlight(event):
    button17.configure(bg = 'white')
button17.bind('<Enter>', Highlight)
button17.bind('<Leave>', unHighlight)


#ADDITIONAL BUTTONS

button18 = Button(root, relief = RIDGE, activebackground = 'white', padx = 0, pady = 0, border = 2, text = 'M\nO\nR\nE\n\nO\nP\nT\nI\nO\nN\nS', fg = 'black', bg = 'white',
                 font = ('Serif', 15), command = lambda: ButtonMORE())
button18.grid(
                     row = 1,
                     column = 4,
                     columnspan = 1,
                     rowspan = 5,
                     sticky = N+S+W+E)

def Highlight(event):
    button18.configure(bg = 'light grey')
def unHighlight(event):
    button18.configure(bg = 'white')
button18.bind('<Enter>', Highlight)
button18.bind('<Leave>', unHighlight)


buttonBSPC = Button(root, relief = RIDGE, activebackground = 'white', padx = 4, pady = 0, border = 2, text = 'Backspace', fg = 'black', bg = 'white',
                 font =('Serif', 10),command = lambda: ButtonBSPC())
buttonBSPC.grid(
                     row = 0,
                     column = 4,
                     columnspan = 1,
                     sticky = W+E+N+S)

def Highlight(event):
    buttonBSPC.configure(bg = 'light grey')
def unHighlight(event):
    buttonBSPC.configure(bg = 'white')
buttonBSPC.bind('<Enter>', Highlight)
buttonBSPC.bind('<Leave>', unHighlight)


#HIDDEN BUTTONS

buttonLN = Button(root, relief = FLAT, activebackground = 'white', padx = 0, pady = 5, border = 3, text = 'ln(x)', fg = 'black', bg = 'white',
                 font =('Serif', 20),command = lambda: ButtonLN())
buttonLN.grid(
                     row = 1,
                     column = 5,
                     columnspan = 1,
                     sticky = W+E+N+S)

def Highlight(event):
    buttonLN.configure(bg = 'light grey')
def unHighlight(event):
    buttonLN.configure(bg = 'white')
buttonLN.bind('<Enter>', Highlight)
buttonLN.bind('<Leave>', unHighlight)


buttonSIN = Button(root, relief = FLAT, activebackground = 'white', padx = 0, pady = 5, border = 3, text = 'sin(a)', fg = 'black', bg = 'white',
                 font =('Serif', 20),command = lambda: ButtonSIN())
buttonSIN.grid(
                     row = 2,
                     column = 5,
                     columnspan = 1,
                     sticky = W+E+N+S)

def Highlight(event):
    buttonSIN.configure(bg = 'light grey')
def unHighlight(event):
    buttonSIN.configure(bg = 'white')
buttonSIN.bind('<Enter>', Highlight)
buttonSIN.bind('<Leave>', unHighlight)


buttonCOS = Button(root, relief = FLAT, activebackground = 'white', padx = 0, pady = 5, border = 3, text = 'cos(a)', fg = 'black', bg = 'white',
                 font =('Serif', 20),command = lambda: ButtonCOS())
buttonCOS.grid(
                     row = 3,
                     column = 5,
                     columnspan = 1,
                     sticky = W+E+N+S)

def Highlight(event):
    buttonCOS.configure(bg = 'light grey')
def unHighlight(event):
    buttonCOS.configure(bg = 'white')
buttonCOS.bind('<Enter>', Highlight)
buttonCOS.bind('<Leave>', unHighlight)


buttonTG = Button(root, relief = FLAT, activebackground = 'white', padx = 0, pady = 5, border = 3, text = 'tg(a)', fg = 'black', bg = 'white',
                 font =('Serif', 20),command = lambda: ButtonTG())
buttonTG.grid(
                     row = 4,
                     column = 5,
                     columnspan = 1,
                     sticky = W+E+N+S)

def Highlight(event):
    buttonTG.configure(bg = 'light grey')
def unHighlight(event):
    buttonTG.configure(bg = 'white')
buttonTG.bind('<Enter>', Highlight)
buttonTG.bind('<Leave>', unHighlight)


buttonCTG = Button(root, relief = FLAT, activebackground = 'white', padx = 0, pady = 5, border = 3, text = 'ctg(a)', fg = 'black', bg = 'white',
                 font =('Serif', 20),command = lambda: ButtonCTG())
buttonCTG.grid(
                     row = 5,
                     column = 5,
                     columnspan = 1,
                     sticky = W+E+N+S)

def Highlight(event):
    buttonCTG.configure(bg = 'light grey')
def unHighlight(event):
    buttonCTG.configure(bg = 'white')
buttonCTG.bind('<Enter>', Highlight)
buttonCTG.bind('<Leave>', unHighlight)


buttonLESS = Button(root, relief = RIDGE, activebackground = 'white', padx = 0, pady = 0, border = 2, text = 'L\nE\nS\nS\n\nO\nP\nT\nI\nO\nN\nS', fg = 'black', bg = 'white',
                 font = ('Serif', 15), command = lambda: ButtonLESS())
buttonLESS.grid(
                     row = 1,
                     column = 6,
                     columnspan = 1,
                     rowspan = 5,
                     sticky = N+S)

def Highlight(event):
    buttonLESS.configure(bg = 'light grey')
def unHighlight(event):
    buttonLESS.configure(bg = 'white')
buttonLESS.bind('<Enter>', Highlight)
buttonLESS.bind('<Leave>', unHighlight)


ButtonABOUT = Button(root, relief = RIDGE, activebackground = 'white', padx = 0, pady = 0, border = 2, text = 'About', fg = 'black', bg = 'white',
                 font = ('Arial', 12), command = About)
ButtonABOUT.grid(
                     row = 0,
                     column = 5,
                     columnspan = 2,
                     rowspan = 1,
                     sticky = N+S+W+E)

def Highlight(event):
    ButtonABOUT.configure(bg = 'light grey')
def unHighlight(event):
    ButtonABOUT.configure(bg = 'white')
ButtonABOUT.bind('<Enter>', Highlight)
ButtonABOUT.bind('<Leave>', unHighlight)

root.mainloop()
