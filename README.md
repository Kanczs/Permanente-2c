# Permanente-2c

Este programa es un minijuego hecho en python que nos permite jugar al pinpong con alguien mas, ya que cuenta con 2 marcadores para que estos pueden ver la puntuacion de cada uno, tambien pueden aumentar la velocidad de la pelota para que esta vay mas rapida segun sus preferencias.



Primero ponemos import turtle para poder hacer este minijuego en python, esto nos abrira una ventana. 

           import turtle
           ventana=turtle.Screen()
           ventana.title("Ping Pong")

Aqui ponemos el color del fondo y el ancho y altura de este mismo. 

           ventana.bgcolor("white")
           ventana.setup(width = 800, height=600)

Esta función se utiliza para activar o desactivar la animación de turtle y establecer un retraso en la actualización de los dibujos.

           ventana.tracer(0)


Creamos las variables de los marcadores.

           marcador1=0
           marcador2=0
           
Creamos la variable de jugador, agregadonle la velocidad, forma, color y posicion que tendra asi como tambien el ancho de la forma.           

    Jugador_1 = turtle.Turtle()
    Jugador_1.speed(0)
    Jugador_1.shape("square")
    Jugador_1.color("black")
    Jugador_1.penup()
    Jugador_1.goto(-350,0)
    Jugador_1.shapesize(stretch_wid=5, stretch_len = 1)
    
Lo mismo con el jugador 2.

    Jugador2= turtle.Turtle()
    Jugador2.speed(0)
    Jugador2.shape("square")
    Jugador2.color("black")
    Jugador2.penup()
    Jugador2.goto(350,0)
    Jugador2.shapesize(stretch_wid=5, stretch_len=1)
    
Aqui creamos la variable de la pelota agregando 

    pelota= turtle.Turtle()
    pelota.speed(0)
    pelota.shape("circle")
    pelota.color("black")
    pelota.penup()
    pelota.goto(0,0)

Aca podemos cambiar la velocidad de la pelota 

    pelota.dx = 1
    pelota.dy = 1
    
Creamos la division en el centro de la ventana 

    division = turtle.Turtle()
    division.color("black")
    division.goto(0,400)
    division.goto(0,-400)    
    
    
    
    
    pen = turtle.Turtle()
    pen.speed(9)
    pen.color("black")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,260)
    pen.write("Jugador_1: 0      Jugador2:0", align= "center", font=(30))

           
           
           
 Funciones
 
    def jugador1_up():
       y= Jugador_1.ycor()
       y += 20
       Jugador_1.sety(y)

    def jugador1_down():
      y= Jugador_1.ycor()
      y -= 20
       Jugador_1.sety(y)

    def Jugador2_up():
      y= Jugador2.ycor()
      y += 20
      Jugador2.sety(y)
  
    def Jugador2_down():
      y= Jugador2.ycor()
      y -= 20
      Jugador2.sety(y)    

Para porder mover los rectangulos hacia arriba y abajo con diferentes teclas.

    ventana.listen()
    ventana.onkeypress(jugador1_up, "w") 
    ventana.onkeypress(jugador1_down, "s")   
    ventana.onkeypress(Jugador2_up, "Up") 
    ventana.onkeypress(Jugador2_down, "Down") 


Para que la pelota rebote contra los bordes y no se pierda la pelota.

    if pelota.ycor() > 290:
        pelota.dy *= -1
    if pelota.ycor() < -290:
        pelota.dy *= -1
        
Para que la pelota vuelva al centro y al hacerlo esto aumente el marcador con la puntuacion respectiva.
        
    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcador1+=1
        pen.clear()
        pen.write("Jugador_1:{}      Jugador2: {}".format(marcador1,marcador2), align= "center", font=(24))        

    if pelota.xcor() < -390: 
        pelota.goto(0,0)
        pelota.dx *= -1 
        marcador2 +=1 
        pen.clear()
        pen.write("Jugador_1: {}     Jugador2:{}".format(marcador1,marcador2), align= "center", font=(24))         
        
        if  ((pelota.xcor() >340 and pelota.xcor() < 350)
            and (pelota.ycor()< Jugador2.ycor() +50
            and pelota.ycor() > Jugador2.ycor() -50 )): 
            pelota.dx *= -1
            pelota.dy *= -1

    if  ((pelota.xcor() <-340 and pelota.xcor() >-350)
            and (pelota.ycor()< Jugador_1.ycor() +50
            and pelota.ycor()> Jugador_1.ycor() -50 )):
            pelota.dx *= -1  
            pelota.dy *= -1       
        
        
        
        
        
        

