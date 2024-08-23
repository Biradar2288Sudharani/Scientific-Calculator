from tkinter import *
from calculator import Calculator

class CalculatorGui:
    def __init__(self):
        
        self.root = Tk()
        self.root.title("Scientific Calculator")

        self.root.configure(background="white")
        self.root.resizable(width=False, height=False)
        self.root.geometry("790x560+400+100")

        self.calc = Frame(self.root)
        self.calc.grid()

        self.textInput = StringVar()

        self.txtDisplay = Entry(self.calc, font=('arial', 20, 'bold'), textvariable=self.textInput, bg="white", 
                                    bd=15, width=50, justify=RIGHT)
        self.txtDisplay.grid(row=0, column=0, columnspan=7, pady=1)
        self.txtDisplay.insert(0, "0")

        self.numbers = "789456123"

        self.allcharacters = ["C", "CE", "√", "+", "π", "cos", "tan", 
                        "7", "8", "9", "-", "sin", "cosh", "tanh", 
                        "4", "5", "6", "*", "sinh", "exp", "mod",
                        "1", "2", "3", "/", "%", "deg", "log",
                        "0", ".", "±", "=", "log10", "x!", "e"]

    def init_calc_window(self):
        calculator = Calculator()
        i = 0
        btn = []
        # showing all button of characters
        for j in range(2,7):
            for k in range(7):
                btn.append(Button(self.calc, width=4, height=2, font=('arial', 20, 'bold'), bd=4, text=self.allcharacters[i]))
                btn[i].grid(row=j, column=k, pady=1)
                if btn[i]['text'] not in self.numbers:
                    btn[i]['bg'] = "white"
                
                btn[i]['command'] = lambda x = btn[i]['text']:calculator.btn_click_func(x, self.textInput)
                i += 1

        self.root.mainloop()