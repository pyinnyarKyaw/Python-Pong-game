import turtle
import winsound

#main menu
print ('')
print ('  WELCOME TO PING PONG')
print ('')
print ('  MOVEMENT KEYS:')
print ("  Yellow: 'w' and 's'")
print ("  Green: 'Up' and 'Down'")
print ('')
input('  Press Enter to start:') 

#screen
window = turtle.Screen()
window.title('Ping Pong')
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(1) #on/off toggle + delay

#score
score_a = 0
score_b = 0

#left paddle
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("yellow")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#right paddle
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('lightgreen')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = 5

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('yellow')
pen.penup()
pen.hideturtle()
pen.goto(-150, 260)
pen.write('player 1: 0', align='center', font=('Courier', 24, 'normal'))

pen_2 = turtle.Turtle()
pen_2.speed(0)
pen_2.color('lightgreen')
pen_2.penup()
pen_2.hideturtle()
pen_2.goto(150, 260)
pen_2.write('player 2: 0', align='center', font=('Courier', 24, 'normal'))

#paddle movement functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#key bindings
window.listen()
window.onkeypress(paddle_a_up, 'w')
window.onkeypress(paddle_a_down, 's')
window.onkeypress(paddle_b_up, 'Up')
window.onkeypress(paddle_b_down, 'Down')

#main game loop
while True:
    window.update()

    #ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #creating borders

    #top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    #left and right
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write('player 1: {}'.format(score_a), align='center', font=('Courier', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen_2.clear()
        pen_2.write('player 2: {}'.format(score_b), align='center', font=('Courier', 24, 'normal'))

    #paddle and ball collisions
    if (ball.xcor() > 330 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(330)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if (ball.xcor() < -330 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-330)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)


    if score_a == 10:
        
        turtle.resetscreen()
        
        pen_3 = turtle.Turtle()
        pen_3.speed(0)
        pen_3.color('yellow')
        pen_3.write('player 1 wins', align='center', font=('Courier', 24, 'normal'))
        pen_3.hideturtle()
        turtle.exitonclick()

    if score_b == 10:
        
        turtle.resetscreen()
        
        pen_3 = turtle.Turtle()
        pen_3.speed(0)
        pen_3.color('lightgreen')
        pen_3.write('player 2 wins', align='center', font=('Courier', 24, 'normal'))
        pen_3.hideturtle()
        turtle.exitonclick()
