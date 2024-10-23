from tkinter import *
import math


root=Tk()
root.title("Godfrey's 0.1")
root.config(bg='grey')
root.geometry('480x380+80+80')
screen=Entry(root, font=('arial', 20, 'bold'), bg='lightblue', fg='darkblue', bd=10, relief=SUNKEN, width=22)
screen.grid(row=0, column=0, columnspan=8, pady=1, padx=1)

button_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                    "4", "5", "6", "*", "∛", "x\u02b8", "x\u00B3", "x\u00B2",
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                    "0", ".", "%", "=", "log", "(", ")", "x!"]
firt_row=1
first_column=0
for i in button_list:
    button=Button(root, width=4, height=2, bd=2, relief=RAISED, text=i, bg='grey', fg='black',
                font=('arail', 14, 'bold'), activebackground='darkblue', padx=1, pady=1, command= lambda button=i: click(button))
    button.grid(row=firt_row, column=first_column)
    first_column+=1
    if first_column > 7:
        firt_row+=1
        first_column=0
        
def click(button):
    display=screen.get()
    answer=""
    try:
        if button=="CE":
            screen.delete(0, END)
        elif button=="C":
            show_me=display[0:len(display) - 1]
            screen.delete(0, END)
            screen.insert(0, show_me)
            return
        elif button== '√':
            answer=round(math.sqrt(eval(display)), 4)
        elif button=='π':
            answer=round(math.pi, 4)
        elif button=='cosθ':
            answer=round(math.cos(math.radians(eval(display))), 5)
        elif button=='tanθ':
            answer=round(math.tan(math.radians(eval(display))), 5)       
        elif button=='sinθ':     
            answer=round(math.sin(math.radians(eval(display))), 5)            
        elif button=='2π':
            answer=round(2*math.pi, 4)      
        elif button=='cosh':
            answer=round(math.cosh(eval(display)), 4)            
        elif button=='tanh':
            answer=round(math.tanh(eval(display)), 4)           
        elif button=='sinh':
            answer=round(math.sinh(eval(display)), 4)            
        elif button=='∛':
            answer=round(math.cbrt(eval(display)), 4)           
        elif button=='x\u02b8':  
            screen.insert(END, '**') 
            return
        elif button=='x\u00B3':
            answer=round(eval(display) ** 3, 4)           
        elif button=='x\u00B2':
            answer=round(eval(display) ** 2, 4)            
        elif button=='ln':
            answer=round(math.log2(eval(display)), 4)            
        elif button=='deg':
            answer=round(math.degrees(eval(display)), 4)            
        elif button=='rad':
            answer=round(math.radians(eval(display)), 4)           
        elif button=='e':
            answer=round(math.e, 4)            
        elif button=='log':
            answer=round(math.log10(eval(display)), 4)        
        elif button=='x!':
            answer=math.factorial(eval(display))           
        elif button==chr(247):
            screen.insert(END, "/")
            return              
        elif button=='=':
            answer=round(eval(display), 4)
        else:
            screen.insert(END, button)
            return
        screen.delete(0, END)
        screen.insert(0,    answer)
    except SyntaxError:
        pass
root.mainloop()