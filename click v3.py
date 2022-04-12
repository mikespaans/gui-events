# Als je op de + of het pijltje omhoog van je toetsenbord drukt word de zelfde functionaliet afgevuurd als op de up button.
# Als je op de – of het pijltje omlaag van je toetsenbord drukt word de zelfde functionaliet afgevuurd als op de down button.
# Als je op de spatie balk klikt word dezelfde functionaliteit afgevuurd als of je dubbel klikt op het label.

import tkinter as tk

window = tk.Tk()
window.title("Clicker")
window.geometry("600x300")
TextNumber = 0

Number = 0
def Omhoog():
    global Number
    global LaatstOmhoogOmlaag
    global TextNumber
    Number = TextNumber
    Number += 1
    TextNumber = tk.IntVar(value= Number) 
    TextNumber = TextNumber.get()
    box1.configure(text= TextNumber)
    Achtergrond(event = 0)
    LaatstOmhoogOmlaag = True
    return TextNumber

def Omlaag():
    global Number
    global LaatstOmhoogOmlaag
    global TextNumber
    Number = TextNumber
    Number -= 1
    TextNumber = tk.IntVar(value= Number) 
    TextNumber = TextNumber.get()
    box1.configure(text= TextNumber)
    Achtergrond(event = 0)
    LaatstOmhoogOmlaag = False
    return TextNumber

def Achtergrond(event):
    if Number == 0:
        box1.configure(background="grey")
        window.configure(background="grey")
    elif Number > 0:
        box1.configure(background="green")
        window.configure(background="green")
    else:
        box1.configure(background="red")
        window.configure(background="red")

def KleurVeranderen(event):
    window.configure(background="yellow")
    box1.configure(background="yellow")
    box1.bind('<Leave>', Achtergrond)

def DubbelKlik(event):
    global TextNumber
    if LaatstOmhoogOmlaag == True:
        TextNumber *= 3
        box1.configure(text= TextNumber)
    else:
        TextNumber /= 3
        box1.configure(text= TextNumber)


box1 = tk.Label(
    window,
    text= 0,
    background="grey"
)
window.configure(background="grey")
button = tk.Button(text="Up", command=Omhoog)
button.pack(padx=10, pady=10)
box1.bind('<Enter>', KleurVeranderen)

box1.pack(
    ipadx=50,
    ipady=30,
    fill="both"
)

Button2 = tk.Button(text="Down", command=Omlaag)
Button2.pack(padx=100, pady=30)

button.bind('<Double-Button>', DubbelKlik)
Button2.bind('<Double-Button>', DubbelKlik)


window.mainloop()