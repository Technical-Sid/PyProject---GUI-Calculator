#A Simple Calculator Using Tkinter GUI.

from tkinter import *
from tkinter import messagebox
import math
class Window(Frame):

    def __init__(self, master=None):
        
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        

    def init_window(self):
        self.focus_set()
        self.master.geometry("315x457")
        self.master.resizable(0,0)
        self.master.title("Calci")
        self.pack(fill=BOTH, expand=1)
        operation = ""
        self.operation = operation
        operation2 = ""
        self.operation2 = operation2
        memory = - 0
        self.memory = memory
        num1 = 0
        self.num1 = num1
        num3 = 0
        self.num3 = num3
        

        message = lambda : messagebox.showinfo(title="About", message="A GUI Calculator coded in Python v3.9 by Siddhesh Surve")
        message2 = lambda : messagebox.showinfo(title="Help", message="Contact for more info: mr.siddhesh07@gmail.com")

        menubar = Menu(self)
        menubar.add_command(label="About", command=message)
        menubar.add_command(label="Help", command=message2)

        root.config(menu=menubar)
        
        display = Entry(self, font=("Helvetica",36,"normal"), width=11)
        display.configure(bg="white",fg="grey", relief="flat", state="readonly")
        self.display = display

        button_1 = Button(self, text="7", width=4, height=1,
                          command=self.button_1_handler, bg="lightgrey",
                          font=("Helvetica",20,"bold"))
        button_1.configure(fg="white", relief="flat")
        self.button_1 = button_1

        button_2 = Button(self, text="8", width=4, height=1,
                          command=self.button_2_handler, bg="lightgrey",
                          font=("Helvetica",20,"bold"))
        
        button_2.configure(fg="white", relief="flat")
        self.button_2 = button_2

        button_3 = Button(self, text="9", width=4, height=1,
                          command=self.button_3_handler, bg="lightgrey",
                          font=("Helvetica",20,"bold"))
        button_3.configure(fg="white", relief="flat")
        self.button_3 = button_3

        button_ADD = Button(self, text="+", width=4, height=1,
                          command=self.button_ADD_handler, bg="grey",
                          font=("Helvetica",20,"bold"))
        button_ADD.configure(fg="white", relief="flat")
        self.button_ADD = button_ADD

        button_PERC = Button(self, text="%", width=4, height=1,             
                          command=self.button_PERC_handler, bg="grey",
                          font=("Helvetica",20,"bold"))
        button_PERC.configure(fg="white", relief="flat")
        self.button_PERC = button_PERC


        button_SQUARE = Button(self, text="x²", width=4, height=1,             
                          command=self.button_SQUARE_handler, bg="darkgrey",
                          font=("Helvetica",20,"bold"))
        button_SQUARE.configure(fg="white", relief="flat")
        self.button_SQUARE = button_SQUARE


        button_ROOT = Button(self, text="√", width=4, height=1,
                          command=self.button_ROOT_handler, bg="darkgrey",
                          font=("Helvetica",20,"bold"))
        button_ROOT.configure(fg="white", relief="flat")
        self.button_ROOT = button_ROOT


        button_pi = Button(self, text="π", width=4, height=1,
                          command=self.button_pi_handler, bg="darkgrey",
                          font=("Helvetica",20,"bold"))
        button_pi.configure(fg="white", relief="flat")
        self.button_pi = button_pi


        button_4 = Button(self, text="4", width=4, height=1,
                          command=self.button_4_handler, bg="lightgrey",
                          font=("Helvetica",20,"bold"))
        button_4.configure(fg="white", relief="flat")
        self.button_4 = button_4

        button_5 = Button(self, text="5", width=4, height=1,
                          command=self.button_5_handler, bg="lightgrey",
                          font=("Helvetica",20,"bold"))
        button_5.configure(fg="white", relief="flat")
        self.button_5 = button_5

        button_6 = Button(self, text="6", width=4, height=1,
                          command=self.button_6_handler, bg="lightgrey",
                          font=("Helvetica",20,"bold"))
        button_6.configure(fg="white", relief="flat")
        self.button_6 = button_6

        button_SUB = Button(self, text="-", width=4, height=1,
                          command=self.button_SUB_handler, bg="grey",
                          font=("Helvetica",20,"bold"))
        button_SUB.configure(fg="white", relief="flat")
        self.button_SUB = button_SUB

        button_7 = Button(self, text="1", width=4, height=1,
                          command=self.button_7_handler, bg="lightgrey",
                          font=("Helvetica",20,"bold"))
        button_7.configure(fg="white", relief="flat")
        self.button_7 = button_7

        button_8 = Button(self, text="2", width=4, height=1,
                          command=self.button_8_handler, bg="lightgrey",
                          font=("Helvetica",20,"bold"))
        button_8.configure(fg="white", relief="flat")
        self.button_8 = button_8


        button_9 = Button(self, text="3", width=4, height=1,
                          command=self.button_9_handler, bg="lightgrey",
                          font=("Helvetica",20,"bold"))
        button_9.configure(fg="white", relief="flat")
        self.button_9 = button_9


        button_MUL = Button(self, text="x", width=4, height=1,
                          command=self.button_MUL_handler, bg="grey",
                          font=("Helvetica",20,"bold"))
        button_MUL.configure(fg="white", relief="flat")
        self.button_MUL = button_MUL


        button_10 = Button(self, text="0", width=4, height=1,
                          command=self.button_10_handler, bg="lightgrey",
                          font=("Helvetica",20,"bold"))
        button_10.configure(fg="white", relief="flat")
        self.button_10 = button_10 

   
        button_11 = Button(self, text=".", width=4, height=1,
                          command=self.button_11_handler, bg="darkgrey",
                          font=("Helvetica",20,"bold"))
        button_11.configure(fg="white", relief="flat")
        self.button_11 = button_11

  
        button_12 = Button(self, text="CE", width=4, height=1,
                          command=self.button_12_handler, bg="grey",
                          font=("Helvetica",20,"bold"))
        button_12.configure(fg="white", relief="flat")
        self.button_12 = button_12

   
        button_DIV = Button(self, text="÷", width=4, height=1,
                          command=self.button_DIV_handler, bg="grey",
                          font=("Helvetica",20,"bold"))
        button_DIV.configure(fg="white", relief="flat")
        self.button_DIV = button_DIV

  
        button_EQUALS = Button(self, text="=", width=18, height=1,
                          command=self.button_EQUALS_handler, bg="grey",
                          font=("Helvetica",20,"bold"))
        button_EQUALS.configure(fg="white", relief="flat")
        self.button_EQUALS = button_EQUALS

        button_MPLUS = Button(self, text="M+", width=4, height=1,
                          command=self.button_MPLUS_handler, bg="darkorange",
                          font=("Helvetica",20,"bold"))
        button_MPLUS.configure(fg="white", relief="flat")
        self.button_MPLUS = button_MPLUS

     
        button_MREAD = Button(self, text="MR", width=4, height=1,
                          command=self.button_MREAD_handler, bg="darkorange",
                          font=("Helvetica",20,"bold"))
        button_MREAD.configure(fg="white", relief="flat")
        self.button_MREAD = button_MREAD

       
        button_MSUB = Button(self, text="M-", width=4, height=1,
                          command=self.button_MSUB_handler, bg="darkorange",
                          font=("Helvetica",20,"bold"))
        button_MSUB.configure(fg="white", relief="flat")
        self.button_MSUB = button_MSUB

       
        button_MCLEAR = Button(self, text="MC", width=4, height=1,
                          command=self.button_MCLEAR_handler, bg="darkorange",
                          font=("Helvetica",20,"bold"))
        button_MCLEAR.configure(fg="white", relief="flat")
        self.button_MREAD = button_MCLEAR




        display.place(x=0, y=0)
        button_1.place(x=0, y=173)
        button_2.place(x=79, y=173) 
        button_3.place(x=158, y=173) 
        button_ADD.place(x=237, y=287)
        button_4.place(x=0, y=230)
        button_5.place(x=79, y=230)
        button_6.place(x=158, y=230)
        button_SUB.place(x=237, y=230)
        button_7.place(x=0, y=287)
        button_8.place(x=79, y=287)
        button_9.place(x=158, y=287)
        button_MUL.place(x=237, y=173)
        button_10.place(x=79, y=344)
        button_11.place(x=0, y=344)
        button_12.place(x=0, y=116)
        button_DIV.place(x=237, y=116)
        button_EQUALS.place(x=0, y=401)
        button_PERC.place(x=237, y=344)
        button_SQUARE.place(x=79, y=116)
        button_ROOT.place(x=158, y=116)
        button_pi.place(x=158, y=344)
        button_MPLUS.place(x=158 , y=59)
        button_MREAD.place(x=79 , y=59)
        button_MSUB.place(x=237 , y=59)
        button_MCLEAR.place(x=0 , y=59)



    def button_1_handler(self):
        self.display.configure(state="normal")
        self.display.insert("end", "7")
        self.display.configure(state="readonly")
    def button_2_handler(self):
        self.display.configure(state="normal")
        self.display.insert("end", "8")
        self.display.configure(state="readonly")
    def button_3_handler(self):
        self.display.configure(state="normal")
        self.display.insert("end", "9")
        self.display.configure(state="readonly")
    def button_4_handler(self):
        self.display.configure(state="normal")
        self.display.insert("end", "4")
        self.display.configure(state="readonly")
    def button_5_handler(self):
        self.display.configure(state="normal")
        self.display.insert("end", "5")
        self.display.configure(state="readonly")
    def button_6_handler(self):
        self.display.configure(state="normal")
        self.display.insert("end", "6")
        self.display.configure(state="readonly")
    def button_7_handler(self):
        self.display.configure(state="normal")
        self.display.insert("end", "1")
        self.display.configure(state="readonly")
    def button_8_handler(self):
        self.display.configure(state="normal")
        self.display.insert("end", "2")
        self.display.configure(state="readonly")
    def button_9_handler(self):
        self.display.configure(state="normal")
        self.display.insert("end", "3")
        self.display.configure(state="readonly")
    def button_10_handler(self):
        self.display.configure(state="normal")
        self.display.insert("end", "0")
        self.display.configure(state="readonly")
    def button_11_handler(self):
        self.display.configure(state="normal")
        self.display.insert("end", ".")
        self.display.configure(state="readonly")
    def button_12_handler(self):
        self.focus_set()
        self.display.configure(state="normal")
        self.display.delete(0,"end")
        self.num1 = 0
        self.num2 = 0
        self.operation = ""
        self.operation2 = ""
        self.display.configure(state="readonly")
    def button_pi_handler(self):
        self.display.configure(state="normal")
        self.display.insert("end", "3.141592653")
        self.display.configure(state="readonly")


    def button_MPLUS_handler(self):
        self.display.configure(state="normal")
        value = self.display.get()
        value = float(value)
        self.memory = value + self.memory
        self.display.configure(state="readonly")

    def button_MSUB_handler(self):
        self.display.configure(state="normal")
        value = self.display.get()
        value = float(value)
        self.memory = self.memory - value
        self.display.configure(state="readonly")


    def button_MREAD_handler(self):
        self.display.configure(state="normal")
        self.display.insert("end", self.memory)
        self.display.configure(state="readonly")

    def button_MCLEAR_handler(self):
        self.display.configure(state="normal")
        self.memory = 0
        self.display.insert("end", self.memory)
        self.display.configure(state="readonly")
        



    def button_ADD_handler(self):
        self.display.configure(state="normal")
       
        self.operation = "+"
        self.num1 = self.display.get()

        self.display.delete(0, "end")

        print(self.num1)
        self.display.configure(state="readonly")


    def button_SUB_handler(self): 
        self.display.configure(state="normal")
        self.operation = "-"
        self.num1 = self.display.get()
        self.display.delete(0, "end")
        print(self.num1)
        self.display.configure(state="readonly")

    def button_PERC_handler(self): 
        self.display.configure(state="normal")
        self.operation2 = "%"
        self.num3 = self.display.get()
        print("percentage")
        self.display.configure(state="readonly")
        self.button_EQUALS_handler()

    def button_SQUARE_handler(self): 
        self.display.configure(state="normal")
        self.operation = "square"
        self.num1 = self.display.get()
        self.display.delete(0, "end")
        print("square")
        self.display.configure(state="readonly")
        self.button_EQUALS_handler()

    def button_ROOT_handler(self):
        self.display.configure(state="normal")
        self.operation = "root"
        self.num1 = self.display.get()
        self.display.delete(0, "end")
        print("root")
        self.display.configure(state="readonly")
        self.button_EQUALS_handler()

    def button_MUL_handler(self):
        self.display.configure(state="normal")
        self.operation = "*"
        self.num1 = self.display.get()
        self.display.delete(0, "end")
        print(self.num1)
        self.display.configure(state="readonly")

    def button_DIV_handler(self):
        self.display.configure(state="normal")
        self.operation = "/"
        self.num1 = self.display.get()
        self.display.delete(0, "end")
        print(self.num1)
        self.display.configure(state="readonly")

    def button_EQUALS_handler(self):
        try:
            carry_on = 0
            self.display.configure(state="normal")
            num1 = float(self.num1)
            print(self.num1)
          
            num2 = self.display.get()
            num2 = float(num2)
            print(num2)
           
        except ValueError:
            print("Needs a second Value")
            

        result = 0
        result = float(result)
        self.num3 = float(self.num3)
        self.num1 = float(self.num1)

        if self.operation2 == "%" and self.operation == "-":
            num3 = self.num3/100
            num4 = self.num1*num3
            result = self.num1-num4
            carry_on = 1
            
        elif self.operation2 == "%" and self.operation == "+":
            num3 = self.num3/100
            num4 = self.num1*num3
            result = self.num1+num4
            carry_on = 1

        elif self.operation2 == "%" and self.operation == "*":
            num3 = self.num3/100
            num4 = self.num1*num3
            result = self.num1*num4
            carry_on = 1

        elif self.operation2 == "%" and self.operation == "/":
            num3 = self.num3/100
            num4 = self.num1*num3
            result = self.num1/num4
            carry_on = 1
        
        elif self.operation == "root":
            num2 = math.sqrt(num1)
            result = num2

        elif self.operation == "square":
            result = num1*num1

            
        elif self.operation == "+":
            if carry_on == 0:
                print("add")
                result = num1 + num2 
                print(result)
            else:
                print("carry on")

        elif self.operation == "-":
            if carry_on == 0:
                print("subtract")
                result = num1 - num2
                print(result)
            else:
                print("carry on...")

        elif self.operation == "*":
            if carry_on == 0:
                print("multiply")
                result = num1 * num2
                print(result)
            else:
                print("carry on...")

        elif self.operation == "/":
            if carry_on == 0:
          
                try:
                    print("divide")
                    result = num1 / num2
                    print(result)
                except ZeroDivisionError:
                    print("You cannot divide by zero!")
                    result = "Error!"
            else:
                print("carry on...")
                
        
        carry_on = 0
        self.display.delete(0, "end")       
        self.display.insert("end", result) 

        num1 = 0
        num2 = 0
        num3 = 0
        num4 = 0
        self.num1 = 0
        self.num2 = 0 
        self.operation = ""
        self.operation2 = ""
        self.display.configure(state="readonly")


root = Tk() 



app = Window(root)
app.pack()

def key(event):
    print("pressed", repr(event.char))
    press = event.char
    if press == "7":
        app.button_1.configure(state=ACTIVE)
        app.button_1_handler()
        app.after(50, lambda: app.button_1.config(state=NORMAL))

    elif press == "8":
        app.button_2.configure(state=ACTIVE)
        app.button_2_handler()
        app.after(50, lambda: app.button_2.config(state=NORMAL))

    elif press == "9":
        app.button_3.configure(state=ACTIVE)
        app.button_3_handler()
        app.after(50, lambda: app.button_3.config(state=NORMAL))
        
    elif press == "4":
        app.button_4.configure(state=ACTIVE)
        app.button_4_handler()
        app.after(50, lambda: app.button_4.config(state=NORMAL))
        
    elif press == "5":
        app.button_5.configure(state=ACTIVE)
        app.button_5_handler()
        app.after(50, lambda: app.button_5.config(state=NORMAL))
        
    elif press == "6":
        app.button_6.configure(state=ACTIVE)
        app.button_6_handler()
        app.after(50, lambda: app.button_6.config(state=NORMAL))
        
    elif press == "1":
        app.button_7.configure(state=ACTIVE)
        app.button_7_handler()
        app.after(50, lambda: app.button_7.config(state=NORMAL))
        
    elif press == "2":
        app.button_8.configure(state=ACTIVE)
        app.button_8_handler()
        app.after(50, lambda: app.button_8.config(state=NORMAL))
        
    elif press == "3":
        app.button_9.configure(state=ACTIVE)
        app.button_9_handler()
        app.after(50, lambda: app.button_9.config(state=NORMAL))
        
    elif press == "0":
        app.button_10.configure(state=ACTIVE)
        app.button_10_handler()
        app.after(50, lambda: app.button_10.config(state=NORMAL))
    elif press == ".":
        app.button_11.configure(state=ACTIVE)
        app.button_11_handler()
        app.after(50, lambda: app.button_11.config(state=NORMAL))
        
    elif press == "c":
        app.button_12.configure(state=ACTIVE)
        app.button_12_handler()
        app.after(50, lambda: app.button_12.config(state=NORMAL))
        
    elif press == "+":
        app.button_ADD.configure(state=ACTIVE)
        app.button_ADD_handler()
        app.after(50, lambda: app.button_ADD.config(state=NORMAL))
        
    elif press == "-":
        app.button_SUB.configure(state=ACTIVE)
        app.button_SUB_handler()
        app.after(50, lambda: app.button_SUB.config(state=NORMAL))
        
    elif press == "*":
        app.button_MUL.configure(state=ACTIVE)
        app.button_MUL_handler()
        app.after(50, lambda: app.button_MUL.config(state=NORMAL))
        
    elif press == "/":
        app.button_DIV.configure(state=ACTIVE)
        app.button_DIV_handler()
        app.after(50, lambda: app.button_DIV.config(state=NORMAL))
    elif press == "=":
        app.button_EQUALS.configure(state=ACTIVE)
        app.button_EQUALS_handler()
        app.after(50, lambda: app.button_EQUALS.config(state=NORMAL))
    elif press == "%":
        app.button_PERC.configure(state=ACTIVE)
        app.button_PERC_handler()
        app.after(50, lambda: app.button_PERC.config(state=NORMAL))
        
def returnButton(event):
     app.button_EQUALS.configure(state=ACTIVE)
     app.button_EQUALS_handler()
     app.after(50, lambda: app.button_EQUALS.config(state=NORMAL))
    

def clear(event):
    app.button_12.configure(state=ACTIVE)
    app.button_12_handler()
    app.after(50, lambda: app.button_12.config(state=NORMAL))
        

    
app.focus_set()
app.bind("<Key>", key)
app.bind("<Return>", returnButton)
app.bind("<BackSpace>", clear)

while app.operation == "+":
    print("hello!")

root.mainloop()

print("Wait for a While!")

#Coding & GUI - PYTHON v3.9
#Created By - Siddhesh Surve

