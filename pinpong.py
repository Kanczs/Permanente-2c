import turtle

ventana=turtle.Screen()
ventana.title("Ping Pong")
ventana.bgcolor("black")
ventana.setup(width = 800, height=600)
ventana.tracer(0)

marcador1=0
marcador2=0

Jugador1 = turtle.Turtle()
Jugador1.speed(0)
Jugador1.shape("square")
Jugador1.color("white")
Jugador1.penup()
Jugador1.goto(-350,0)
Jugador1.shapesize(stretch_wid=5, stretch_len = 1)

Jugador2= turtle.Turtle()
Jugador2.speed(0)
Jugador2.shape("square")
Jugador2.color("white")
Jugador2.penup()
Jugador2.goto(350,0)
Jugador2.shapesize(stretch_wid=5, stretch_len=1)


pelota= turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)

pelota.dx = 0.2
pelota.dy = 0.2




#Division
division = turtle.Turtle()
division.color("white")
division.goto(0,400)
division.goto(0,-400)

#pen
pen = turtle.Turtle()
pen.speed(9)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Jugador1: 0      Jugador2:0", align= "center", font=(30))



#funciones
def jugador1_up():
    y= Jugador1.ycor()
    y += 20
    Jugador1.sety(y)

def jugador1_down():
    y= Jugador1.ycor()
    y -= 20
    Jugador1.sety(y)

def Jugador2_up():
    y= Jugador2.ycor()
    y += 20
    Jugador2.sety(y)

def Jugador2_down():
    y= Jugador2.ycor()
    y -= 20
    Jugador2.sety(y)    




ventana.listen()
ventana.onkeypress(jugador1_up, "w") 
ventana.onkeypress(jugador1_down, "s")   
ventana.onkeypress(Jugador2_up, "Up") 
ventana.onkeypress(Jugador2_down, "Down")   



while True:
    ventana.update()
    
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

     #Colisiones con los bordes

    if pelota.ycor() > 290:
        pelota.dy *= -1
    if pelota.ycor() < -290:
        pelota.dy *= -1

      #Regresa al centro

    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcador1+=1
        pen.clear()
        pen.write("Jugador1:{}      Jugador2: {}".format(marcador1,marcador2), align= "center", font=(24))        

    if pelota.xcor() < -390: 
        pelota.goto(0,0)
        pelota.dx *= -1 
        marcador2 +=1 
        pen.clear()
        pen.write("Jugador1: {}     Jugador2:{}".format(marcador1,marcador2), align= "center", font=(24))       

    if  ((pelota.xcor() >340 and pelota.xcor() < 350)
            and (pelota.ycor()< Jugador2.ycor() +50
            and pelota.ycor() > Jugador2.ycor() -50 )): 
            pelota.dx *= -1
            pelota.dy *= -1

    if  ((pelota.xcor() <-340 and pelota.xcor() >-350)
            and (pelota.ycor()< Jugador1.ycor() +50
            and pelota.ycor()> Jugador1.ycor() -50 )):
            pelota.dx *= -1  
            pelota.dy *= -1           
