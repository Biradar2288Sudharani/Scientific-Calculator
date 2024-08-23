import math

class Calculator:
    def __init__(self):

        self.standardCalcCharacters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
                                    '+', '-', '*', '/', '.']
        self.operatorCharacters = ['+', '-', '*', '/', '=', 'x!', '%']

        self.constantChars = ["π", "e"]

        self.operator = [] # to store operation for calculate later. ex: 4*5 or math.sqrt(9)
        self.operatorDisplay = [] # to store operation for display on screen. ex: 4*5 or √9
        self.oldBtnValue = '' # to store current BtnValue
        self.oldBtnValueForDisplay = '' # for display
        self.answer = '' # result after calculating operation

    def btn_click_func(self, btnValue, textInput):
        
        # if previous btn value is "=" and current btn value is in operatorCharacters, set operator = [result]
        # ex: 4*5 = 20, after click =, and then click + and 5 => answer = 20+5 = 25
        # if we dont do this, operator will be set at empty and ex above will get error
        if self.oldBtnValue == "=" and btnValue in self.operatorCharacters:

            self.operator = [self.answer]
            self.operatorDisplay = [self.answer]
        
        # if previous btn value is "=" and current btn value is not in operatorCharacters, set operatorDisplay = []
        if self.oldBtnValue == "=" and btnValue not in self.operatorCharacters:
            self.operatorDisplay = []
        
        # ex: 4*5, 5.6
        if btnValue in self.standardCalcCharacters:
            
            self.oldBtnValue = btnValue
            self.oldBtnValueForDisplay = btnValue
            self.operator.append(self.oldBtnValue)
            self.operatorDisplay.append(self.oldBtnValueForDisplay)
        else:
            operatorStr = ''.join(self.operator)
            if btnValue == '√':
                # if operator is number or previous btn value is number or previous btn value is constant like pi or e
                # do *math.sqrt(. ex: 4*5, then click √, and 5, we have 4*5*math.sqrt(5) for calculate later if click "="
                # but for display: we have 4*5*√5
                if operatorStr.isdigit() or self.oldBtnValue.isdigit() or self.oldBtnValueForDisplay in self.constantChars:
                    self.oldBtnValue = '*math.sqrt('
                    self.oldBtnValueForDisplay = '*√'
                else:
                    self.oldBtnValue = 'math.sqrt('
                    self.oldBtnValueForDisplay = '√'
                
                self.operator.append(self.oldBtnValue)
                self.operatorDisplay.append(self.oldBtnValueForDisplay)
            # similar with √
            elif btnValue == 'cos':
                if operatorStr.isdigit() or self.oldBtnValue.isdigit() or self.oldBtnValueForDisplay in self.constantChars:
                    self.oldBtnValue = '*math.cos(math.radians('
                    self.oldBtnValueForDisplay = '*cos'
                else:
                    self.oldBtnValue = 'math.cos(math.radians('
                    self.oldBtnValueForDisplay = 'cos'
                
                self.operator.append(self.oldBtnValue)
                self.operatorDisplay.append(self.oldBtnValueForDisplay)
            elif btnValue == 'tan':
                if operatorStr.isdigit() or self.oldBtnValue.isdigit() or self.oldBtnValueForDisplay in self.constantChars:
                    self.oldBtnValue = '*math.tan(math.radians('
                    self.oldBtnValueForDisplay = '*tan'
                else:
                    self.oldBtnValue = 'math.tan(math.radians('
                    self.oldBtnValueForDisplay = 'tan'
                
                self.operator.append(self.oldBtnValue)
                self.operatorDisplay.append(self.oldBtnValueForDisplay)
            elif btnValue == 'sin':
                if operatorStr.isdigit() or self.oldBtnValue.isdigit() or self.oldBtnValueForDisplay in self.constantChars:
                    self.oldBtnValue = '*math.sin(math.radians('
                    self.oldBtnValueForDisplay = '*sin'
                else:
                    self.oldBtnValue = 'math.sin(math.radians('
                    self.oldBtnValueForDisplay = 'sin'
                
                self.operator.append(self.oldBtnValue)
                self.operatorDisplay.append(self.oldBtnValueForDisplay)
            elif btnValue == 'cosh':
                if operatorStr.isdigit() or self.oldBtnValue.isdigit() or self.oldBtnValueForDisplay in self.constantChars:
                    self.oldBtnValue = '*math.cosh(math.radians('
                    self.oldBtnValueForDisplay = '*cosh'
                else:
                    self.oldBtnValue = 'math.cosh(math.radians('
                    self.oldBtnValueForDisplay = 'cosh'
                
                self.operator.append(self.oldBtnValue)
                self.operatorDisplay.append(self.oldBtnValueForDisplay)
            elif btnValue == 'tanh':
                if operatorStr.isdigit() or self.oldBtnValue.isdigit() or self.oldBtnValueForDisplay in self.constantChars:
                    self.oldBtnValue = '*math.tanh(math.radians('
                    self.oldBtnValueForDisplay = '*tanh'
                else:
                    self.oldBtnValue = 'math.tanh(math.radians('
                    self.oldBtnValueForDisplay = 'tanh'
                
                self.operator.append(self.oldBtnValue)
                self.operatorDisplay.append(self.oldBtnValueForDisplay)
            elif btnValue == 'sinh':
                if operatorStr.isdigit() or self.oldBtnValue.isdigit() or self.oldBtnValueForDisplay in self.constantChars:
                    self.oldBtnValue = '*math.sinh(math.radians('
                    self.oldBtnValueForDisplay = '*sinh'
                else:
                    self.oldBtnValue = 'math.sinh(math.radians('
                    self.oldBtnValueForDisplay = 'sinh'
                
                self.operator.append(self.oldBtnValue)
                self.operatorDisplay.append(self.oldBtnValueForDisplay)
            elif btnValue == 'exp':
                if operatorStr.isdigit() or self.oldBtnValue.isdigit() or self.oldBtnValueForDisplay in self.constantChars:
                    self.oldBtnValue = '*math.exp('
                    self.oldBtnValueForDisplay = '*exp'
                else:
                    self.oldBtnValue = 'math.exp('
                    self.oldBtnValueForDisplay = 'exp'
                
                self.operator.append(self.oldBtnValue)
                self.operatorDisplay.append(self.oldBtnValueForDisplay)
            elif btnValue == 'log':
                if operatorStr.isdigit() or self.oldBtnValue.isdigit() or self.oldBtnValueForDisplay in self.constantChars:
                    self.oldBtnValue = '*math.log('
                    self.oldBtnValueForDisplay = '*log'
                else:
                    self.oldBtnValue = 'math.log('
                    self.oldBtnValueForDisplay = 'log'
                
                self.operator.append(self.oldBtnValue)
                self.operatorDisplay.append(self.oldBtnValueForDisplay)
            elif btnValue == 'log10':
                if operatorStr.isdigit() or self.oldBtnValue.isdigit() or self.oldBtnValueForDisplay in self.constantChars:
                    self.oldBtnValue = '*math.log10('
                    self.oldBtnValueForDisplay = '*log10'
                else:
                    self.oldBtnValue = 'math.log10('
                    self.oldBtnValueForDisplay = 'log10'
                
                self.operator.append(self.oldBtnValue)
                self.operatorDisplay.append(self.oldBtnValueForDisplay)
            # ex: 8%3 = 2
            elif btnValue == 'mod':
                self.oldBtnValue = btnValue
                self.oldBtnValueForDisplay = btnValue
                self.operator.append("%")
                self.operatorDisplay.append("%")
            elif btnValue == 'π':
                if operatorStr.isdigit():
                    self.oldBtnValue = '*math.pi'
                    self.oldBtnValueForDisplay = '*π'
                else:
                    self.oldBtnValue = 'math.pi'
                    self.oldBtnValueForDisplay = 'π'

                self.operator.append(self.oldBtnValue)
                self.operatorDisplay.append(self.oldBtnValueForDisplay)
            elif btnValue == 'e':
                if operatorStr.isdigit():
                    self.oldBtnValue = '*math.e'
                    self.oldBtnValueForDisplay = '*e'
                else:
                    self.oldBtnValue = 'math.e'
                    self.oldBtnValueForDisplay = 'e'
            
                self.operator.append(self.oldBtnValue)
                self.operatorDisplay.append(self.oldBtnValueForDisplay)
            elif btnValue == '%':
                if "(" in operatorStr: 
                    num_parentheses = operatorStr.count('(')
                    self.operator.append(num_parentheses * ")")
                    # close all existing parentheses before doing %. ex: sin(30)% = 0.005
                    operatorStr = ''.join(self.operator) # join again to new string

                self.oldBtnValue = operatorStr + "*0.01"
                self.oldBtnValueForDisplay = ''.join(self.operatorDisplay) + "%" # for display. ex: sin30 becomes -sin30
            
                self.operator = [self.oldBtnValue]
                self.operatorDisplay = [self.oldBtnValueForDisplay]

            elif btnValue == 'x!':
                if operatorStr.isdigit() or str(eval(operatorStr)).isdigit(): # factorial only apply for integer
                    self.oldBtnValue = "math.factorial(" + operatorStr
                    self.oldBtnValueForDisplay = '!'
            
                self.operator = [self.oldBtnValue]
                self.operatorDisplay.append(self.oldBtnValueForDisplay)
            elif btnValue == '±':
                if "(" in operatorStr: 
                    num_parentheses = operatorStr.count('(')
                    self.operator.append(num_parentheses * ")")
                    # close all existing parentheses before doing minus, positive turns to negative, negative turns to positive
                    operatorStr = ''.join(self.operator) # join again to new string

                self.oldBtnValue = "-" + operatorStr
                self.oldBtnValueForDisplay = '-' + ''.join(self.operatorDisplay) # for display. ex: sin30 becomes -sin30
            
                self.operator = [self.oldBtnValue]
                self.operatorDisplay = [self.oldBtnValueForDisplay]
            elif btnValue == '=':
                try:
                    # closing all existing parentheses before doing equal
                    if "(" in operatorStr and ")" not in operatorStr:
                        num_parentheses = operatorStr.count('(')
                        self.operator.append(num_parentheses * ")")
                        operatorStr = ''.join(self.operator) # join again to new string
                    
                    # eval function: ex: eval("math.sqrt(9)") = 3 or eval("4*5") = 20
                    self.answer = str(eval(operatorStr))
                    self.operatorDisplay = [self.answer] # only 1 element answer
                    self.operator = [] # after taking equal, reset operation
                    self.oldBtnValue = "="
                except: # in case wrong syntax. ex: math.sqrt(), no parameter for sqrt func
                    self.operatorDisplay = ["Error"] # only 1 element answer
                    self.operator = []
                    self.oldBtnValue = "="
            elif btnValue == 'C':
                del self.operator[-1] # remove the last operator charater. for example 8*9 will be 8* or log(56) will be log(5)
                del self.operatorDisplay[-1]
                
                if self.operator: # if operator is not empty, set oldBtnValue to be the last element of operator after removing above
                    self.oldBtnValue = self.operator[-1]
                    self.oldBtnValueForDisplay = self.operatorDisplay[-1]
                else: # else, set it to ''
                    self.oldBtnValue = ''
                    self.oldBtnValueForDisplay = ''
            elif btnValue == 'CE': # remove all
                self.operator = []
                self.operatorDisplay = []
            
        textInput.set(''.join(self.operatorDisplay)) # show on the field screen

