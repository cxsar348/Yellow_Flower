#                                                                       Edited by @cxsar348

#           ----- Importing and config libraries ---
from turtle import*
from turtle import Screen 
import turtle as tour
import tkinter as tk

tur = tour.Turtle()

#           --- Assinging the font --- 
FONT = ('Comic Sans MS', 12, 'normal')

#           --- Drawing ---
tur.penup ()
tur.left (90)
tur.fd (200)
tur.pendown ()
tur.right (90)

tur.fillcolor ("yellow")
tur.begin_fill ()
tur.circle (10,180)
tur.circle (25,110)
tur.left (50)
tur.circle (60,45)
tur.circle (20,170)
tur.right (24)
tur.fd (30)
tur.left (10)
tur.circle (30,110)
tur.fd (20)
tur.left (40)
tur.circle (90,70)
tur.circle (30,150)
tur.right (30)
tur.fd (15)
tur.circle (80,90)
tur.left (15)
tur.fd (45)
tur.right (165)
tur.fd (20)
tur.left (155)
tur.circle (150,80)
tur.left (50)
tur.circle (150,90)
tur.end_fill ()


tur.left (150)
tur.circle (-90,70)
tur.left (20)
tur.circle (75,105)
tur.setheading (60)
tur.circle (80,98)
tur.circle (-90,40)

tur.left (180)
tur.circle (90,40)
tur.circle (-80,98)
tur.setheading (-83)

tur.fd (30)
tur.left (90)
tur.fd (25)
tur.left (45)
tur.fillcolor ("dark green")
tur.begin_fill ()
tur.circle (-80,90)
tur.right (90)
tur.circle (-80,90)
tur.end_fill ()
tur.right (135)
tur.fd (60)
tur.left (180)
tur.fd (85)
tur.left (90)
tur.fd (80)

tur.right (90)
tur.right (45)
tur.fillcolor ("dark green")
tur.begin_fill ()
tur.circle (80,90)
tur.left (90)
tur.circle (80,90)
tur.end_fill ()
tur.left (135)
tur.fd (60)
tur.left (180)
tur.fd (60)
tur.right (90)
tur.circle (200,60)

#           --- Assing a function to display the Text
def i_love_you():
    label = tk.Label(canvas.master, text="text 1", font=(FONT))
    canvas.create_window(0, -5000, window=label)

#           --- Creating the Text ---
    canvas.create_text(-230, -200, text="Sé que no es mucho,", fill="gold3", font=(FONT))
    canvas.create_text(-230, -180, text="pero es lo mejor que puedo", fill="gold3", font=(FONT))
    canvas.create_text(-230, -160, text="hacer por ti ahora mismo", fill="gold3", font=(FONT))
    canvas.create_text(-230, -140, text="Te amo <3", fill="gold2", font=(FONT))
    canvas.create_text(-230, -120, text="~César L Paredes", fill="gold2", font=('Comic Sans MS', 12, 'bold'))

#           --- Displaying the button and the screen ---
screen = tour.Screen()
screen.setup(678,574)
canvas = screen.getcanvas()

button = tk.Button(canvas.master, text="Click me", command=i_love_you)
canvas.create_window(0, 0, window=button)

#           --- Loop ---
screen.mainloop()
