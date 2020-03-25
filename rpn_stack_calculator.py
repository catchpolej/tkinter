#
# Reverse polish notation stack calculator
#
# uses: deque class
# https://docs.python.org/2/library/collections.html#collections.deque
#
from tkinter import *
from collections import deque
import tkinter.font as font

  
stack = deque() 
  
# first a bit of sample stack code
# append() function is push()
stack.append('test stack item') 
try:
    print(stack.pop())
except IndexError:
    print("stack empty")
try:
    print(stack.pop())
except IndexError:
    print("stack empty")

    
# define the gui
class rpn_calc_gui:
    def __init__(self, master):
        self.w = Label(master, text="RPN Calculator")
        self.w.pack()
        self.expression_list = []
        self.i = 0
        self.processing = False

        control_frame = Frame(master, bg='lavender')
        control_frame.pack()                                           #fill=BOTH, expand=True
        self.label1 = Label (control_frame, text =("rpn expression"))
        self.label1.pack(side="left")
        self.expression = StringVar()
        self.expression.set("Enter rpn expression")
        self.e_expression = Entry (control_frame, textvariable=self.expression)
        self.e_expression.pack(side="left")
        self.e_expression.bind('<Return>', self.start)
        self.b_step = Button(control_frame, text = "step", command=lambda:self.step())
        self.b_step.config(state="disabled")
        self.b_step.pack(side="left")
        
        data_frame = Frame(master, bg='grey')
        data_frame.pack()
        # message box
        msg_frame = Frame(data_frame)
        msg_frame.grid(column=0, row=0)
        self.t = Text(msg_frame, height="5")
        self.t.pack()
        self.t.delete(1.0,END)
        self.t.insert(END, "Enter the rpn expression into the top box\n")
        self.t.insert(END, "For example:\n4 5 + 1 3 - / 3 * =")

        # next item widgets
        nxt_frame = Frame(data_frame)
        nxt_frame.grid(column=0, row=1)        
        self.label2 = Label (nxt_frame, text =("next item"))
        self.label2.pack(side="left")
        self.next = StringVar()
        self.next.set("NIL")
        self.e_next = Entry (nxt_frame, textvariable=self.next)
        self.e_next.pack(side="left")
        # top of stack widgets
        st_frame = Frame(data_frame)
        st_frame.grid(column=0, row=2)
        self.label3 = Label (st_frame, text =("top of stack"))
        self.label3.pack(side="left")
        self.stack_top = StringVar()
        self.stack_top.set("NIL")
        self.e_st = Entry (st_frame, textvariable=self.stack_top)
        self.e_st.pack(side="left")

    
    def calc(self,op):
        if op == '^':
            op = '**'
        arg2 = stack.pop()
        arg1 = stack.pop()
        return eval(arg1 + op + arg2)
   
    def step(self):
        # clear message box
        self.t.delete(1.0,END)
        # Look at the next item to see what to do
        if self.next.get() in ['+','-','*','/','=','^','**']:
            if self.next.get() == '=':
                mem = stack.pop()
                self.processing = False
            else:
                mem = self.calc(self.next.get())
            stack.append(str(mem))
            self.stack_top.set(str(mem))
        else:
            stack.append(self.expression_list[self.i])
            self.stack_top.set(self.expression_list[self.i])
            
        if self.processing:
            self.t.insert(END, "STEP " + str(self.i) + " completed.")
            self.i += 1
            self.next.set(self.expression_list[self.i])
        else:
            self.t.insert(END, "Final result is " + str(mem))
            self.b_step.config(state="disabled")

    def start(self, event):
        self.t.delete(1.0,END)
        self.b_step.config(state="normal")
        self.expression_list = self.expression.get().split(" ")
        self.t.insert(END, "INITIALISED:\n")
        self.t.insert(END, str(self.expression_list))
        self.i = 0
        self.next.set(self.expression_list[self.i])
        self.processing = True

        
        
# window setup
window1 = Tk()
font.nametofont('TkDefaultFont').configure(size=14)
window1.geometry("500x600")
window1.title("Window for GUI")
# launch the gui
app1 = rpn_calc_gui(window1)
window1.mainloop()
# wit for user input to close
input("Press enter to close")
