# Als je met je muis over het label gaat wordt de achtergrond van het scherm geel worden ongeacht wat hij was (groen, grijs of rood).
# Als je met je muis van het label af gaat moet de kleur weer als daarvoor worden (groen, grijs of rood).
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Clicker")
window.geometry("600x300")



Number = 0
def Omhoog():
    global Number
    Number += 1
    TextNumber = tk.IntVar(value= Number) 
    TextNumber = TextNumber.get()
    box1.configure(text= TextNumber)
    Achtergrond(event = 0)
    return TextNumber

def Omlaag():
    global Number
    Number -= 1
    TextNumber = tk.IntVar(value= Number) 
    TextNumber = TextNumber.get()
    box1.configure(text= TextNumber)
    Achtergrond(event = 0)
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







window.mainloop()