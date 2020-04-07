from tkinter import *
from tkinter import messagebox


# Initialize parameters
paramBackground = '#ECECEC'
paramFrom = -100
paramTo = 100
paramWidth = 3
paramJustify = CENTER
paramRowLine1 = 0
paramRowLine2 = 3
paramRowLine3 = 6
paramRowLine4 = 9
paramRowLine5 = 13
paramRowLine6 = 18


def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


def verify_spinbox(widget, num):
    if check_int(num) is True:
        return
    messagebox.showerror('Error', 'Values must be integers between ' + str(paramFrom) + ' and ' + str(paramTo) + '!')


# Create tkinter window with properties
window = Tk()
window.title("Python TP6")
window.geometry('1080x500')
window.minsize(500, 400)
window.configure(bg=paramBackground)


# Make window responsive
for i in range(0, 20):
    window.rowconfigure(index=i, weight=1)
    window.columnconfigure(index=i, weight=1)


# Set default values
defaultValue = 0
defaultValueTeta1 = IntVar(); defaultValueTeta1.set(defaultValue)
defaultValueTeta2 = IntVar(); defaultValueTeta2.set(defaultValue)
defaultValueTeta3 = IntVar(); defaultValueTeta3.set(defaultValue)
defaultValueTeta4 = IntVar(); defaultValueTeta4.set(defaultValue)
defaultValueL = IntVar(); defaultValueL.set(defaultValue)
defaultValueX = IntVar(); defaultValueX.set(defaultValue)
defaultValueY = IntVar(); defaultValueY.set(defaultValue)
defaultValueZ = IntVar(); defaultValueZ.set(defaultValue)


# Initialize Label
lblTeta1 = Label(window, text='θ1', bg=paramBackground, highlightbackground=paramBackground)
lblTeta2 = Label(window, text='θ2', bg=paramBackground, highlightbackground=paramBackground)
lblTeta3 = Label(window, text='θ3', bg=paramBackground, highlightbackground=paramBackground)
lblTeta4 = Label(window, text='θ4', bg=paramBackground, highlightbackground=paramBackground)
lblL = Label(window, text='L', bg=paramBackground, highlightbackground=paramBackground)
lblX = Label(window, text='X', bg=paramBackground, highlightbackground=paramBackground)
lblY = Label(window, text='Y', bg=paramBackground, highlightbackground=paramBackground)
lblZ = Label(window, text='Z', bg=paramBackground, highlightbackground=paramBackground)
lblResultText = Label(window, text='The result is :', bg=paramBackground, highlightbackground=paramBackground)
lblResultValue = Label(window, text='result', bg=paramBackground, highlightbackground=paramBackground)


# Initialize Button
btnCalculate = Button(window, text='Calculate', justify=paramJustify, bg=paramBackground,
                      highlightbackground=paramBackground)
btnQuit = Button(window, text='Quit', justify=paramJustify, command=window.destroy, bg=paramBackground,
                 highlightbackground=paramBackground)


# Initialize Spinbox
teta1 = Spinbox(window, from_=paramFrom, to=paramTo, width=paramWidth, justify=paramJustify,
                textvariable=defaultValueTeta1, bg=paramBackground, highlightbackground=paramBackground)
teta2 = Spinbox(window, from_=paramFrom, to=paramTo, width=paramWidth, justify=paramJustify,
                textvariable=defaultValueTeta2, bg=paramBackground, highlightbackground=paramBackground)
teta3 = Spinbox(window, from_=paramFrom, to=paramTo, width=paramWidth, justify=paramJustify,
                textvariable=defaultValueTeta3, bg=paramBackground, highlightbackground=paramBackground)
teta4 = Spinbox(window, from_=paramFrom, to=paramTo, width=paramWidth, justify=paramJustify,
                textvariable=defaultValueTeta4, bg=paramBackground, highlightbackground=paramBackground)
l = Spinbox(window, from_=paramFrom, to=paramTo, width=paramWidth, justify=paramJustify,
            textvariable=defaultValueL, bg=paramBackground, highlightbackground=paramBackground)
x = Spinbox(window, from_=paramFrom, to=paramTo, width=paramWidth, justify=paramJustify,
            textvariable=defaultValueX, bg=paramBackground, highlightbackground=paramBackground)
y = Spinbox(window, from_=paramFrom, to=paramTo, width=paramWidth, justify=paramJustify,
            textvariable=defaultValueY, bg=paramBackground, highlightbackground=paramBackground)
z = Spinbox(window, from_=paramFrom, to=paramTo, width=paramWidth, justify=paramJustify,
            textvariable=defaultValueZ, bg=paramBackground, highlightbackground=paramBackground)


# Place all widgets in the window
lblTeta1.grid(column=4, row=paramRowLine1, sticky="e"); teta1.grid(column=5, row=paramRowLine1, sticky="w")
lblTeta2.grid(column=6, row=paramRowLine1, sticky="e"); teta2.grid(column=7, row=paramRowLine1, sticky="w")
lblTeta3.grid(column=8, row=paramRowLine1, sticky="e"); teta3.grid(column=9, row=paramRowLine1, sticky="w")
lblTeta4.grid(column=10, row=paramRowLine1, sticky="e"); teta4.grid(column=11, row=paramRowLine1, sticky="w")

lblL.grid(column=7, row=paramRowLine2, sticky="e"); l.grid(column=8, row=paramRowLine2, sticky="w")

lblX.grid(column=5, row=paramRowLine3, sticky="e"); x.grid(column=6, row=paramRowLine3, sticky="w")
lblY.grid(column=7, row=paramRowLine3, sticky="e"); y.grid(column=8, row=paramRowLine3, sticky="w")
lblZ.grid(column=9, row=paramRowLine3, sticky="e"); z.grid(column=10, row=paramRowLine3, sticky="w")

btnCalculate.grid(column=8, row=paramRowLine4, sticky="ew")

lblResultText.grid(column=6, row=paramRowLine5, sticky="e") # move to calculate method
lblResultValue.grid(column=7, row=paramRowLine5, sticky="w") # move to calculate method

btnQuit.grid(column=18, row=paramRowLine6, sticky="ew")


window.mainloop()
