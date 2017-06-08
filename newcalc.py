from tkinter import *
from tkinter import messagebox

calculator = Tk()
calculator.title ("Calculator")
calculator.resizable(0, 0)

class Application(Frame):
    def __init__(self, master, *args,**kwargs):
       Frame.__init__(self, master, *args,**kwargs)
       self.createWidgets()

    def replaceText(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)

    def calculateExpression(self):
        self.expression = self.display.get()
        self.expression = self.expression.replace("%", "/100")

        try: 
            self.result = eval(self.expression)
            self.replaceText(self.result)
        except:
            messagebox.showinfo("Error!", "Invalid Input")

  
    def appendToDisplay (self,text):
        self.entryText = self.display.get()
        self.textLenght = len(self.entryText)

        if self.entryText == "0":
            self.replaceText (text)
        else:
            self.display.insert(self.textLenght, text)

    def clearText (self):
        self.replaceText ("0")

    def createWidgets (self):
        self.display = Entry(self, font=("Helvetica", 20), borderwidth=0, relief=RAISED, justify=RIGHT)
        self.display.insert (0, "0")
        self.display.grid (row=0, column=0, columnspan=5)

        self.sevenButton = Button(self, font =("Helvetica", 16), text="7", borderwidth=0, command =lambda: self.appendToDisplay("7"))
        self.sevenButton.grid(row=1, column =0, sticky="NWNESWSE")
        
        self.eightButton = Button(self, font =("Helvetica", 16), text="8", borderwidth=0, command =lambda: self.appendToDisplay("8"))
        self.eightButton.grid(row=1, column =1, sticky="NWNESWSE")
        
        self.nineButton = Button(self, font =("Helvetica", 16), text="9", borderwidth=0, command =lambda: self.appendToDisplay("9"))
        self.nineButton.grid(row=1, column =2, sticky="NWNESWSE")

        self.multiplyButton = Button(self, font =("Helvetica", 16), text="*", borderwidth=0, command =lambda: self.appendToDisplay("*"))
        self.multiplyButton.grid(row=1, column =3,sticky="NWNESWSE")

        self.clearButton = Button(self, font =("Helvetica", 16), text="C", borderwidth=0, command=lambda: self.clearText())
        self.clearButton.grid(row=1, column =4, sticky="NWNESWSE")


        
        self.fourButton = Button(self, font =("Helvetica", 16), text="4", borderwidth=0, command =lambda: self.appendToDisplay("4"))
        self.fourButton.grid(row=2, column =0, sticky="NWNESWSE")
        
        self.fiveButton = Button(self, font =("Helvetica", 16), text="5", borderwidth=0, command =lambda: self.appendToDisplay("5"))
        self.fiveButton.grid(row=2, column =1, sticky="NWNESWSE")
        
        self.sixButton = Button(self, font =("Helvetica", 16), text="6", borderwidth=0, command =lambda: self.appendToDisplay("6"))
        self.sixButton.grid(row=2, column =2, sticky="NWNESWSE")

        self.divideButton = Button(self, font =("Helvetica", 16), text="/", borderwidth=0, command =lambda: self.appendToDisplay("/"))
        self.divideButton.grid(row=2, column =3,sticky="NWNESWSE")
        
        self.percentageButton = Button(self, font =("Helvetica", 16), text="%", borderwidth=0, command =lambda: self.appendToDisplay("%"))
        self.percentageButton.grid(row=2, column =4, sticky="NWNESWSE")

        
        
        self.oneButton = Button(self, font =("Helvetica", 16), text="1", borderwidth=0, command =lambda: self.appendToDisplay("1"))
        self.oneButton.grid(row=3, column =0, sticky="NWNESWSE")
        
        self.twoButton = Button(self, font =("Helvetica", 16), text="2", borderwidth=0, command =lambda: self.appendToDisplay("2"))
        self.twoButton.grid(row=3, column =1, sticky="NWNESWSE")
        
        self.threeButton = Button(self, font =("Helvetica", 16), text="3", borderwidth=0, command =lambda: self.appendToDisplay("3"))
        self.threeButton.grid(row=3, column =2, sticky="NWNESWSE")
        
        self.minusButton = Button(self, font =("Helvetica", 16), text="-", borderwidth=0, command =lambda: self.appendToDisplay("-"))
        self.minusButton.grid(row=3, column =3,sticky="NWNESWSE")

        self.equalsButton = Button(self, font =("Helvetica", 16), text="=", borderwidth=0, command =lambda: self.calculateExpression())
        self.equalsButton.grid(row=3, column =4, sticky="NWNESWSE", rowspan=2)

        

        self.zeroButton = Button(self, font =("Helvetica", 16), text="0", borderwidth=0, command =lambda: self.appendToDisplay("0"))
        self.zeroButton.grid(row=4, column =0, columnspan = 2, sticky="NWNESWSE")
        
        self.dotButton = Button(self, font =("Helvetica", 16), text=".", borderwidth=0, command =lambda: self.appendToDisplay("."))
        self.dotButton.grid(row=4, column =2, sticky="NWNESWSE")
        
        self.plusButton = Button(self, font =("Helvetica", 16), text="+", borderwidth=0, command =lambda: self.appendToDisplay("+"))
        self.plusButton.grid(row=4, column =3, sticky="NWNESWSE")

        
app = Application(calculator).grid()
calculator,mainloop()

