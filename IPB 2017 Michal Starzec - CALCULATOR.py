from __future__ import division
from Tkinter import *
import math

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
    operator = ""

root = Tk()
root.title('ABACUS')
root.configure(background='black')
root.resizable(FALSE, FALSE)

operator=""

display_input = StringVar(root, '0')
display = Entry(root,relief = SUNKEN, textvariable = display_input, bd = '15', font = ('Calibri', '20'), fg = 'white', bg = 'black', insertwidth = 4, justify = 'right').grid(
    row = 0,
    columnspan = 4,
    sticky = "")

button1 = Button(root, relief =SOLID, activebackground = 'orange', padx = 5, pady = 5, border = 1, text = 'C', fg = 'black', bg = 'orange',
                 font =('Calibri', 20, 'bold'),command = lambda: ButtonClear()).grid(
                     row = 1,
                     column = 0,
                     columnspan = 1,
                     sticky = W+E+N+S)
button2 = Button(root,relief =SOLID, activebackground = 'orange', padx = 5, pady = 5, border = 1, text = 'X', fg = 'black', bg = 'orange',
                 font = ('Calibri', 20, 'bold'), command = lambda: ButtonClick('*')).grid(
                     row = 1,
                     column = 1,
                     columnspan = 1,
                     sticky = W+E+N+S)
button3 = Button(root,relief =SOLID, activebackground = 'orange', padx = 5, pady = 5, border = 1, text = '/', fg = 'black', bg = 'orange',
                 font = ('Calibri', 20, 'bold'), command = lambda: ButtonClick('/')).grid(
                     row = 1,
                     column = 2,
                     columnspan = 1,
                     sticky = W+E+N+S)
button4 = Button(root,relief =SOLID, activebackground = 'orange', padx = 5, pady = 5, border = 1, text = '-', fg = 'black', bg = 'orange',
                 font = ('Calibri', 20, 'bold'), command = lambda: ButtonClick('-')).grid(
                     row = 1,
                     column = 3,
                     columnspan = 1,
                     sticky = W+E+N+S)


button5 = Button(root,relief =SOLID, padx = 5, pady = 5, border = 1, text = '7', fg = 'black',
                 font = ('Calibri', 20, 'bold'), command = lambda: ButtonClick(7)).grid(
                     row = 2,
                     column = 0,
                     columnspan = 1,
                     sticky = W+E+N+S)
button6 = Button(root,relief =SOLID, padx = 5, pady = 5, border = 1, text = '8', fg = 'black',
                 font = ('Calibri', 20, 'bold'), command = lambda: ButtonClick(8)).grid(
                     row = 2,
                     column = 1,
                     columnspan = 1,
                     sticky = W+E+N+S)
button7 = Button(root,relief =SOLID, padx = 5, pady = 5, border = 1, text = '9', fg = 'black',
                 font = ('Calibri', 20, 'bold'), command = lambda: ButtonClick(9)).grid(
                     row = 2,
                     column = 2,
                     columnspan = 1,
                     sticky = W+E+N+S)
button8 = Button(root,relief =SOLID, activebackground = 'orange', padx = 5, pady = 5, border = 1, text = '+', fg = 'black', bg = 'orange',
                 font = ('Calibri', 20, 'bold'), command = lambda: ButtonClick('+')).grid(
                     row = 2,
                     column = 3,
                     columnspan = 1,
                     rowspan = 2,
                     sticky = W+E+N+S)


button9 = Button(root,relief =SOLID, padx = 5, pady = 5, border = 1, text = '4', fg = 'black',
                 font = ('Calibri', 20, 'bold'), command = lambda: ButtonClick(4)).grid(
                     row = 3,
                     column = 0,
                     columnspan = 1,
                     sticky = W+E+N+S)
button10 = Button(root,relief =SOLID, padx = 5, pady = 5, border = 1, text = '5', fg = 'black',
                 font = ('Calibri', 20, 'bold'), command = lambda: ButtonClick(5)).grid(
                     row = 3,
                     column = 1,
                     columnspan = 1,
                     sticky = W+E+N+S)
button11 = Button(root,relief =SOLID, padx = 5, pady = 5, border = 1, text = '6', fg = 'black',
                 font = ('Calibri', 20, 'bold'), command = lambda: ButtonClick(6)).grid(
                     row = 3,
                     column = 2,
                     columnspan = 1,
                     sticky = W+E+N+S)


button12 = Button(root,relief =SOLID, padx = 5, pady = 5, border = 1, text = '1', fg = 'black',
                 font = ('Calibri', 20, 'bold'), command = lambda: ButtonClick(1)).grid(
                     row = 4,
                     column = 0,
                     columnspan = 1,
                     sticky = W+E+N+S)
button13 = Button(root,relief =SOLID, padx = 5, pady = 5, border = 1, text = '2', fg = 'black',
                 font = ('Calibri', 20, 'bold'), command = lambda: ButtonClick(2)).grid(
                     row = 4,
                     column = 1,
                     columnspan = 1,
                     sticky = W+E+N+S)
button14 = Button(root,relief =SOLID, padx = 5, pady = 5, border = 1, text = '3', fg = 'black',
                 font = ('Calibri', 20, 'bold'), command = lambda: ButtonClick(3)).grid(
                     row = 4,
                     column = 2,
                     columnspan = 1,
                     sticky = W+E+N+S)
button15 = Button(root,relief =SOLID, activebackground = 'orange', padx = 5, pady = 5, border = 1, text = '=', fg = 'black', bg = 'orange',
                 font = ('Calibri', 20, 'bold'), command = lambda: ButtonEqual()).grid(
                     row = 4,
                     column = 3,
                     columnspan = 1,
                     rowspan = 2,
                     sticky = W+E+N+S)


button16 = Button(root,relief =SOLID, padx = 5, pady = 5, border = 1, text = '0', fg = 'black',
                 font = ('Calibri', 20, 'bold'), command = lambda: ButtonClick(0)).grid(
                     row = 5,
                     column = 0,
                     columnspan = 2,
                     sticky = W+E+N+S)
button17 = Button(root,relief =SOLID, activebackground = 'grey', padx = 5, pady = 5, border = 1, text = '.', fg = 'black', bg = 'grey',
                 font = ('Calibri', 20, 'bold'), command = lambda: ButtonClick('.')).grid(
                     row = 5,
                     column = 2,
                     columnspan = 1,
                     sticky = W+E+N+S)


root.mainloop()

