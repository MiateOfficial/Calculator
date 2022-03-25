import os
import tkinter
from functools import partial
from sys import setrecursionlimit
from tkinter import *

Window = Tk()
Window.geometry("329x420")
Window.configure(bg="#203239")
Window.title("Calculator")
new_result = ""
label = Label(Window,text="Developed by Miate",font=("Roboto",10),bg="#203239",fg="white")
label.place(x=98,y=396)
dir = str(os.getcwd()) + "\\icon.ico"
Window.iconbitmap(dir)

#Result
#This function made for convert x to *
def PressTimes():
    if not result.get().__contains__("/") and not result.get().__contains__("x") and not result.get().__contains__("+") and not result.get().__contains__("-"):
        RemoveValidation()
        result.insert(result.index(INSERT), "x")
        AddValidation()
def getResult():
    global result
    global new_result
    new_results = result.get()
    if (new_results.__contains__("x")):
        f = new_results.replace("x", "*")
        new_result = eval(f)
    else:
        new_result = eval(new_results)
    RemoveValidation()
    result.delete(0,tkinter.END)
    result.insert(0,new_result)
    AddValidation()
# SCREEN
def only_numbers(char):
    return char.isdigit()
validation = Window.register(only_numbers)
result = tkinter.Entry(Window, width=400, font=("Roboto", 24), bg="#141E27", bd="10", fg="white", validate="key",validatecommand=(validation, '%S'))
def RemoveValidation():
    result.configure(width=400, font=("Roboto", 24), bg="#141E27", bd="10", fg="white", validate="all",validatecommand=(validation, "%i"))
def AddValidation():
    result.configure(width=400, font=("Roboto", 24), bg="#141E27", bd="10", fg="white", validate="all",validatecommand=(validation, "%S"))
def Clears():
    RemoveValidation()
    result.delete(0,tkinter.END)
    AddValidation()
# ButtonEvents
def ButtonPress(str):
    global CurrentCalculating
    if str == "Button1":
        result.insert(result.index(INSERT), "1")
    elif str == "Button2":
        result.insert(result.index(INSERT), "2")
    elif str == "Button3":
        result.insert(result.index(INSERT), "3")
    elif str == "Button4":
        result.insert(result.index(INSERT), "4")
    elif str == "Button5":
        result.insert(result.index(INSERT), "5")
    elif str == "Button6":
        result.insert(result.index(INSERT), "6")
    elif str == "Button7":
        result.insert(result.index(INSERT), "7")
    elif str == "Button8":
        result.insert(result.index(INSERT), "8")
    elif str == "Button9":
        result.insert(result.index(INSERT), "9")
    elif str == "Button0":
        result.insert(result.index(INSERT), "0")
    elif str == "ButtonDot":
        RemoveValidation()
        result.insert(result.index(INSERT), ".")
        AddValidation()
    elif str == "ButtonPlus":
        if not result.get().__contains__("/") and not result.get().__contains__("x") and not result.get().__contains__("+") and not result.get().__contains__("-"):
            RemoveValidation()
            result.insert(result.index(INSERT), "+")
            AddValidation()
        else:
            result.insert(result.index(INSERT), "+")
    elif str == "ButtonMinus":
        RemoveValidation()
        result.insert(result.index(INSERT), "-")
        AddValidation()
    elif str == "ButtonSubstract":
        if not result.get().__contains__("/") and not result.get().__contains__("x") and not result.get().__contains__("+") and not result.get().__contains__("-"):
            RemoveValidation()
            result.insert(result.index(INSERT), "/")
            AddValidation()
        else:
            result.insert(result.index(INSERT), "/")
# Buttons
calculate_area = tkinter.Canvas(Window)
calculate_area.configure(width=200, height=320, bg="#203239", bd=0, highlightthickness=0)
calculate_area.place(x=0, y=65)
DEFAULT_COORDINATES = 0, 0, 85, 85
Zero = PhotoImage(file = f"button0.png")
One = PhotoImage(file=f"button1.png")
Two = PhotoImage(file=f"button2.png")
Three = PhotoImage(file=f"button3.png")
Four = PhotoImage(file=f"button4.png")
Five = PhotoImage(file=f"button5.png")
Six = PhotoImage(file=f"button6.png")
Seven = PhotoImage(file=f"button7.png")
Eight = PhotoImage(file=f"button8.png")
Nine = PhotoImage(file=f"button9.png")
Minus = PhotoImage(file=f"button-small.png")
Plus = PhotoImage(file=f"button+small.png")
Times = PhotoImage(file=f"buttonx.png")
Substract = PhotoImage(file=f"ButtonSubstract.png")
Equals = PhotoImage(file=f"button=.png")
Clear = PhotoImage(file=f"ButtonClear.png")
Dot = PhotoImage(file=f"ButtonDot.png")
Button1 = tkinter.Button(calculate_area, image=One, bd=0, command=partial(ButtonPress,"Button1")).pack(side=LEFT)
Button2 = tkinter.Button(calculate_area, image=Two, bd=0,command=partial(ButtonPress,"Button2")).pack(side=LEFT)
Button3 = tkinter.Button(calculate_area, image=Three, bd=0,command=partial(ButtonPress,"Button3")).pack(side=RIGHT)
Button4 = tkinter.Button(Window, image=Four, bd=0,command=partial(ButtonPress,"Button4")).place(x=0, y=147)
Button5 = tkinter.Button(Window, image=Five, bd=0,command=partial(ButtonPress,"Button5")).place(x=82, y=147)
Button6 = tkinter.Button(Window, image=Six, bd=0,command=partial(ButtonPress,"Button6")).place(x=164, y=147)
Button7 = tkinter.Button(Window, image=Seven, bd=0,command=partial(ButtonPress,"Button7")).place(x=0, y=229)
Button8 = tkinter.Button(Window, image=Eight, bd=0,command=partial(ButtonPress,"Button8")).place(x=82, y=229)
Button9 = tkinter.Button(Window, image=Nine, bd=0,command=partial(ButtonPress,"Button9")).place(x=164, y=229)
Button0 = tkinter.Button(Window, image=Zero, bd=0,command=partial(ButtonPress,"Button0")).place(x=82, y=311)
ButtonMinus = tkinter.Button(Window, image=Minus, bd=0,command=partial(ButtonPress,"ButtonMinus")).place(x=246, y=65)
ButtonPlus = tkinter.Button(Window, image=Plus, bd=0,command=partial(ButtonPress,"ButtonPlus")).place(x=246, y=147)
ButtonTimes = tkinter.Button(Window, image=Times, bd=0,command=PressTimes).place(x=246, y=229)
ButtonSubstract = tkinter.Button(Window, image=Substract, bd=0,command=partial(ButtonPress,"ButtonSubstract")).place(x=246, y=311)
ButtonEquals = tkinter.Button(Window, image=Equals, bd=0,borderwidth=0,command=getResult,highlightthickness=0,relief="ridge",activeforeground="#141E27").place(x=270, y=10)
ButtonClear = tkinter.Button(Window, image=Clear, bd=0,command=Clears).place(x=0, y=311)
ButtonDot = tkinter.Button(Window, image=Dot, bd=0,command=partial(ButtonPress,"ButtonDot")).place(x=164, y=311)

result.pack()
Window.resizable(False, False)
Window.mainloop()
#
