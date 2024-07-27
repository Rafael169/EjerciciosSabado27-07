#print("**5**")
#from turtle import * 
#for n in range (5):

 #   forward(300)
  #  right(144)
    
import turtle
import math

# Configurar la pantalla
screen = turtle.Screen()
screen.title("Hola Mundo con Spring")
screen.bgcolor("white")

# Configurar la tortuga
t = turtle.Turtle()
t.speed(5)
t.pensize(2)
t.color("blue")

# Función para dibujar un resorte
def draw_spring(x, y, amplitude, wavelength, length):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(length):
        y_offset = amplitude * math.sin(i * 2 * math.pi / wavelength)
        t.goto(x + i, y + y_offset)

# Dibujar el texto "Hola Mundo" con resorte
def draw_text_with_spring(text, start_x, start_y, amplitude, wavelength):
    x = start_x
    y = start_y
    for char in text:
        draw_spring(x, y, amplitude, wavelength, 20)
        x += 20
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.write(char, font=("Arial", 16, "bold"))
        x += 20

# Configuración de las coordenadas y parámetros del resorte
start_x = -200
start_y = 0
amplitude = 10
wavelength = 20

# Dibujar "Hola Mundo" con resorte
draw_text_with_spring("Hola Mundo", start_x, start_y, amplitude, wavelength)

# Ocultar la tortuga y mostrar la pantalla
t.hideturtle()
turtle.done()
