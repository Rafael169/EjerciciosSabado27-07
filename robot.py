import turtle

# Configurar la pantalla
screen = turtle.Screen()
screen.title("Dibujo de un Robot")
screen.bgcolor("white")

# Crear la tortuga
t = turtle.Turtle()
t.speed(5)

# Función para dibujar un rectángulo
def draw_rectangle(width, height, color):
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Dibujar la cabeza del robot
def draw_head():
    t.penup()
    t.goto(-50, 100)
    t.pendown()
    draw_rectangle(100, 100, "grey")

# Dibujar los ojos del robot
def draw_eyes():
    t.penup()
    t.goto(-30, 150)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    
    t.penup()
    t.goto(30, 150)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    
    t.penup()
    t.goto(-30, 150)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    
    t.penup()
    t.goto(30, 150)
    t.pendown()
    t.begin_fill()
    t.circle(5)
    t.end_fill()

# Dibujar la boca del robot
def draw_mouth():
    t.penup()
    t.goto(-20, 120)
    t.pendown()
    t.color("black")
    t.forward(40)

# Dibujar el cuerpo del robot
def draw_body():
    t.penup()
    t.goto(-70, 0)
    t.pendown()
    draw_rectangle(140, 150, "grey")

# Dibujar los brazos del robot
def draw_arms():
    t.penup()
    t.goto(-90, 50)
    t.pendown()
    draw_rectangle(20, 100, "grey")
    
    t.penup()
    t.goto(70, 50)
    t.pendown()
    draw_rectangle(20, 100, "grey")

# Dibujar las piernas del robot
def draw_legs():
    t.penup()
    t.goto(-50, -150)
    t.pendown()
    draw_rectangle(40, 100, "grey")
    
    t.penup()
    t.goto(10, -150)
    t.pendown()
    draw_rectangle(40, 100, "grey")

# Dibujar el robot completo
def draw_robot():
    draw_head()
    draw_eyes()
    draw_mouth()
    draw_body()
    draw_arms()
    draw_legs()

# Dibujar el robot
draw_robot()

# Ocultar la tortuga y mostrar la pantalla
t.hideturtle()
turtle.done()
