from tkinter import *
import time as t
from Scientific_calc import ScientificCalculator
import math as m

root = Tk()

GUI_width = 336
GUI_height = 450


def StandardCalc():
    pass


def ScientificCalc():
    SC = ScientificCalculator(root, 500, 600)
    SC.Structure(root)

# Geometry

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (GUI_width / 2)
y = (screen_height / 2) - (GUI_width / 2)

root.geometry(f"{GUI_width}x{GUI_height}+{int(x)}+{int(y)}")
root.title("Calculator - Made By Ritik with " + u"\u2764\ufe0f")


def welcome():
    tf.set("W")
    output.update()
    button[1]['bg'] = 'cyan'
    button[1].update()
    t.sleep(0.2)
    tf.set("We")
    button[1]['bg'] = 'white'
    button[1].update()
    button[2]['bg'] = 'cyan'
    button[2].update()
    output.update()
    t.sleep(0.2)
    tf.set("Wel")
    output.update()
    button[2]['bg'] = 'white'
    button[2].update()
    button[3]['bg'] = 'cyan'
    button[3].update()
    t.sleep(0.2)
    tf.set("Welc")
    output.update()
    button[3]['bg'] = 'white'
    button[3].update()
    button[4]['bg'] = 'cyan'
    button[4].update()
    t.sleep(0.2)
    tf.set("Welco")
    output.update()
    button[4]['bg'] = 'white'
    button[4].update()
    button[5]['bg'] = 'cyan'
    button[5].update()
    t.sleep(0.2)
    tf.set("Welcom")
    output.update()
    button[5]['bg'] = 'white'
    button[5].update()
    button[6]['bg'] = 'cyan'
    button[6].update()
    t.sleep(0.2)
    tf.set("Welcome")
    output.update()
    button[6]['bg'] = 'white'
    button[6].update()
    button[7]['bg'] = 'cyan'
    button[7].update()
    t.sleep(0.2)
    tf.set("Welcome.")
    output.update()
    button[7]['bg'] = 'white'
    button[7].update()
    button[8]['bg'] = 'cyan'
    button[8].update()
    t.sleep(0.2)
    tf.set("Welcome..")
    output.update()
    button[8]['bg'] = 'white'
    button[8].update()
    button[9]['bg'] = 'cyan'
    button[9].update()
    t.sleep(0.2)
    tf.set("Welcome...")
    output.update()
    button[9]['bg'] = 'white'
    button[9].update()
    t.sleep(0.2)
    tf.set("Welcome...")
    output.update()
    t.sleep(0.2)

    tf.set("")
    output.update()


def click(event):
    global tf
    text = event.widget.cget("text")
    if text == "X":
        text = "*"
    if text == "=":
        if tf.get().isdigit():
            result = int(tf.get())
        else:
            try:
                result = eval(output.get())
            except Exception as e:
                print(e)
                result = "Error"
                output.update()

        tf.set(result)
        output.update()

    elif text == "C":
        tf.set("")
        output.update()

    elif text == "OFF":
        butpower['text'] = "ON"
        button[0]['bg'] = 'white'
        tf.set("")
        output.config(state='disabled')
    elif text == "ON":
        output.config(state='normal')
        butpower['text'] = "OFF"
        welcome()

    elif butpower['text'] != 'ON':
        tf.set(tf.get() + text)
        output.update()

    else:
        tf.set("")


# Menu bar
mainMenu = Menu(root)
fileMenu = Menu(mainMenu, tearoff=0)
fileMenu.add_command(label="Standard Calculator", command=StandardCalc)
fileMenu.add_command(label="Scientific Calculator", command=ScientificCalc)
mainMenu.add_cascade(label="Options", menu=fileMenu)
root.config(menu=mainMenu)

tf = StringVar()
tf.set("")
button = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
output = Entry(root, textvariable=tf, bg="white", fg="black", font="Times 42 bold")
output.pack(fill=X, pady=10, padx=10, ipadx=15)

# Frames for Buttons
frame1 = Frame(root, bg="light grey", relief=SUNKEN, borderwidth=5)
frame1.pack(padx=20, pady=10, side=TOP, anchor=W)
frame2 = Frame(root, bg="light grey", relief=SUNKEN, borderwidth=5)
frame2.pack(padx=20, pady=5, side=TOP, anchor=W)
frame3 = Frame(root, bg="light grey", relief=SUNKEN, borderwidth=5)
frame3.pack(padx=20, pady=5, side=TOP, anchor=W)
frame4 = Frame(root, bg="light grey", relief=SUNKEN, borderwidth=5)
frame4.pack(padx=20, pady=5, side=TOP, anchor=W)
frameOperator = Frame(root, bg="grey", relief=SUNKEN, borderwidth=5)
frameOperator.pack(padx=20, pady=10, side=TOP, anchor=W)
# Numbers Buttons


for i in range(0, 10):
    if 0 < i < 4:
        button[i] = Button(frame2, text=f"{i}", relief=RIDGE, bg="white", activebackground = 'orange',activeforeground = 'white',width=4, height=1, font="Lucida 14 bold")
        button[i].pack(side=LEFT, padx=5)
        button[i].bind("<Button-1>", click)
    elif 4 <= i < 7:
        button[i] = Button(frame3, text=f"{i}", relief=RIDGE, bg="white",activebackground = 'orange',activeforeground = 'white', width=4, height=1, font="Lucida 14 bold")
        button[i].pack(side=LEFT, padx=5)
        button[i].bind("<Button-1>", click)
    elif 7 <= i < 10:
        button[i] = Button(frame4, text=f"{i}", relief=RIDGE, bg="white",activebackground = 'orange',activeforeground = 'white', width=4, height=1, font="Lucida 14 bold")
        button[i].pack(side=LEFT, padx=5)
        button[i].bind("<Button-1>", click)
    else:

        button[i] = Button(frameOperator, text=f"{i}", relief=RIDGE, bg="white",activebackground = 'orange',activeforeground = 'white', width=9, height=1,
                           font="Lucida 14 bold")
        button[i].pack(side=LEFT, padx=8)
        button[i].bind("<Button-1>", click)

# Operator Buttons


butsub = Button(frame2, text="-", relief=RIDGE, bg="orange", fg="white", width=4, height=1, font="Lucida 14 bold")
butsub.pack(side=TOP, padx=5)
butsub.bind("<Button-1>", click)

butmult = Button(frame3, text="X", relief=RIDGE, bg="orange", fg="white", width=4, height=1, font="Lucida 14 bold")
butmult.pack(side=TOP, padx=5)
butmult.bind("<Button-1>", click)

butdivide = Button(frame4, text="/", relief=RIDGE, bg="orange", fg="white", width=4, height=1, font="Lucida 14 bold")
butdivide.pack(side=TOP, padx=5)
butdivide.bind("<Button-1>", click)

butdecimle = Button(frameOperator, text=".", relief=RIDGE, bg="cyan", width=4, height=1, font="Lucida 14 bold")
butdecimle.pack(side=LEFT, padx=5)
butdecimle.bind("<Button-1>", click)

butequals = Button(frameOperator, text="=", relief=RIDGE, bg="orange", fg="white", width=4, height=1,
                   font="Lucida 14 bold")
butequals.pack(side=TOP, padx=5)
butequals.bind("<Button-1>", click)

butclear = Button(frame1, text="C", relief=RIDGE, bg="orange", fg="white", width=4, height=1, font="Lucida 14 bold")
butclear.pack(side=LEFT, padx=5)
butclear.bind("<Button-1>", click)

butremainder = Button(frame1, text="%", relief=RIDGE, bg="orange", fg="white", width=4, height=1, font="Lucida 14 bold")
butremainder.pack(side=LEFT, padx=5)
butremainder.bind("<Button-1>", click)

butpower = Button(frame1, text="OFF", relief=RIDGE, bg="red", fg="white", width=4, height=1, font="Lucida 14 bold")
butpower.pack(side=LEFT, padx=5)
butpower.bind("<Button-1>", click)

butAdd = Button(frame1, text="+", relief=RIDGE, bg="orange", fg="white", width=4, height=1, font="Lucida 14 bold")
butAdd.pack(side=LEFT, padx=5)
butAdd.bind("<Button-1>", click)

root.mainloop()
