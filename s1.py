import turtle
import random
import time
sc=turtle.Screen()
sc.title("SNAKE GAME BY MOUNIKA")
sc.setup(width=700,height=700)
sc.tracer(0)
turtle.bgcolor("black")
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color("white")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()
score=0
delay=0.1
#snake creating
snake=turtle.Turtle()
snake.speed(0)
snake.shape("circle")
snake.color("red")
snake.penup()
snake.goto(0,0)
snake.direction="stop"
#food creating
fruit=turtle.Turtle()
fruit.speed(3)
fruit.shape("circle")
fruit.color("green")
fruit.penup()
fruit.goto(50,50)
old_food=[]
#scoring creating
scoring=turtle.Turtle()
scoring.speed(0)
scoring.color("skyblue")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,450)
scoring.write("score: ",align="center",font=("Courier",24,"bold"))
def go_up():
    if snake.direction !="down":
        snake.direction="up"
def go_down():
    if snake.direction !="up":
        snake.direction="down"
def go_left():
    if snake.direction !="right":
        snake.direction="left"
def go_right():
    if snake.direction !="left":
        snake.direction="right"
def move():
    if snake.direction=="up":
        y=snake.ycor()
        snake.sety(y+20)
    elif snake.direction=="down":
        y=snake.ycor()
        snake.sety(y-20)
    elif snake.direction=="right":
        x=snake.xcor()
        snake.setx(x+20)
    elif snake.direction=="left":
        x=snake.xcor()
        snake.setx(x-20)
# keyboard bindings with turtle
sc.listen()
sc.onkeypress(go_up,"Up")
sc.onkeypress(go_down,"Down")
sc.onkeypress(go_right,"Right")
sc.onkeypress(go_left,"Left")
while True:
    sc.update()
    #snake and food collisions
    if snake.distance(fruit)<20:
        x=random.randint(-290,270)
        y=random.randint(-240,240)
        fruit.goto(x,y)
        scoring.clear()
        score+=1
        scoring.write(f"score:{score} ",align="center",font=("Courier",24,"bold"))
        delay -=0.001
        #new food
        new_fruit=turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("circle")
        new_fruit.color("green")
        new_fruit.penup()
        old_food.append(new_fruit)
    #snake size increasing
    for i in range(len(old_food)-1,0,-1):
        a=old_food[i-1].xcor()
        b=old_food[i-1].ycor()
        old_food[i].goto(a,b)
    if len(old_food)>0:
        a=snake.xcor()
        b=snake.ycor()
        old_food[0].goto(a,b)
    move()
    #snake and border collision
    if snake.xcor()>270 or snake.xcor()<-290 or snake.ycor()>240 or snake.ycor()<-240:
        time.sleep(1)
        sc.clear()
        sc.bgcolor("black")
        scoring.goto(0,0)
        scoring.write(f"  GAME OVER \n Your score is:  {score}",align="center",font=("Courier",30,"bold"))
    # snake collide itself
    for f in old_food:
        if f.distance(snake)<20:
           time.sleep(1)
           sc.clear()
           sc.bgcolor("black")
           scoring.goto(0,0)
           scoring.write(f"  GAME OVER \n Your score is: {score}",align="center",font=("Courier",30,"bold")) 
    time.sleep(delay)
turtle.Terminator()
