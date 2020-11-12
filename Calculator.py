import tkinter as Tk
from tkinter import *
import math

root = Tk()
root.title("OOP Calculator")

class App:
    def __init__(self,master):
        self.master = master
        calc = Calculator(self.master,0,0)
    
class Calculator:
    def __init__(self,parent, x, y):
        self.parent = parent
        self.container = Frame(self.parent)
        self.container.grid(row=x,column=y)
        
        self.font = ("Arial",15)
        self.b_height = 2
        self.b_width = 4
        
        self.res = ""  # saves expression
        self.last_ans = ""  # saves last solution
        self.ans_on_disp = False   # checks whether solution already being displayed
      
    # ---- Buttons ---- #
    
        self.entry(0,0)
        self.btn_ac("AC",1,0,"lightgrey")
        self.btn_undo("Undo",1,1,"lightgrey")
        self.btn_eq("=",5,2)
        self.btn_ans("Ans",1,2,"lightgrey")
        
        self.btn("1",2,0)
        self.btn("2",2,1)
        self.btn("3",2,2)
        self.btn("√",2,3,"lightgrey")
        self.btn("^",2,4,"lightgrey")
        
        self.btn("4",3,0)
        self.btn("5",3,1)
        self.btn("6",3,2)
        self.btn("(",3,3,"lightgrey")
        self.btn(")",3,4,"lightgrey")
        
        self.btn("7",4,0)
        self.btn("8",4,1)
        self.btn("9",4,2)
        self.btn("+",4,3,"lightgrey")
        self.btn("-",4,4,"lightgrey")
        
        self.btn(".",5,0)
        self.btn("0",5,1)
        self.btn("×",5,3,"lightgrey")
        self.btn("÷",5,4,"lightgrey")
        
    def entry(self, x_co, y_co):
        self.entry = Text(self.container,font=self.font, state = DISABLED,
                     height = self.b_height//2, width = self.b_width*5)
        self.entry.grid(row=x_co, column=y_co, columnspan=5, sticky='we')
        
    def btn(self, op, x_co, y_co, back_col="white"):
        self.b = Button(self.container, text=op, bg = back_col,
                        height=self.b_height, width=self.b_width, font = self.font,
                       command=lambda:self.btn_click(op))
        self.b.grid(row=x_co, column=y_co,sticky="WE")
        
    def btn_eq(self, op, x_co, y_co, back_col="white"):
        self.b = Button(self.container, text=op, bg = back_col,
                        height=self.b_height, width=self.b_width, font = self.font,
                       command=lambda:self.btn_eq_click())
        self.b.grid(row=x_co, column=y_co,sticky="WE")
        
    def btn_undo(self, op, x_co, y_co, back_col="white"):
        self.b = Button(self.container, text=op, bg = back_col,
                        height=self.b_height, width=self.b_width, font = self.font,
                       command=lambda:self.btn_undo_click())
        self.b.grid(row=x_co, column=y_co,sticky="WE")
        
    def btn_ac(self, op, x_co, y_co, back_col="white"):
        self.b = Button(self.container, text=op, bg = back_col,
                        height=self.b_height, width=self.b_width, font = self.font,
                       command=lambda:self.btn_ac_click())
        self.b.grid(row=x_co, column=y_co,sticky="WE")
        
    def btn_ans(self, op, x_co, y_co, back_col="white"):
        self.b = Button(self.container, text=op, bg = back_col,
                        height=self.b_height, width=self.b_width, font = self.font,
                       command=lambda:self.btn_ans_click())
        self.b.grid(row=x_co, column=y_co,sticky="WE")
        
    def display_stuff(self,txt):
        self.entry.config(state=NORMAL)
        self.entry.delete("1.0",END)
        self.entry.insert("1.0",txt)
        self.entry.config(state=DISABLED)
    
    
    # ---- Button Commands ---- #
    
    def btn_click(self,txt):
        if not self.ans_on_disp:
            self.res = self.res + txt
            self.display_stuff(self.res)
        else:
            find_eq = self.res.index("=")
            self.res = self.res[find_eq:] + txt
            self.ans_on_disp = False
            self.display_stuff(self.res)
        
    def btn_eq_click(self):
        if self.ans_on_disp == False:
            backend_sol = self.res
            rep_list = {"×":"*",
                        "÷":"/" , 
                        "^":"**",
                        "√":"math.sqrt"}
            
            if self.res != "":
                for op in rep_list:
                    if op in backend_sol:
                        backend_sol = backend_sol.replace(op,rep_list[op])

                try:
                    fin_ans = self.last_ans = round(eval(backend_sol),5)
                    self.res = self.res + "=" + str(fin_ans)
                    
                except Exception:
                    self.res = self.res + "=" + "Error"

                self.display_stuff(self.res)
                self.ans_on_disp = True
    
    def btn_undo_click(self):  
        if self.ans_on_disp == True:
            eq_sign = self.res.index("=")
            self.res = self.res[:eq_sign-1] + txt
            self.ans_on_disp = False
        else:
            self.res = self.res[:-1]
            
        self.display_stuff(self.res)
              
    def btn_ac_click(self):
        self.res = ""
        self.display_stuff(self.res)
        self.ans_on_disp = False
        
    def btn_ans_click(self):
        if self.ans_on_disp == False:
            self.res = self.res + str(self.last_ans)
        else:
            self.res = str(self.last_ans)
            self.ans_on_disp = False
        self.display_stuff(self.res)
        
app = App(root)
root.mainloop()