import turtle
import random #it gives random  to the content
import time
delay=0.1
score_card=0
highest_score=0
bodies=[]


#creating a screen
s=turtle.Screen()
s.title("Snake Game")
s.bgcolor("light blue");
s.setup(width=600,height=600)   #size of a screen


#creating a head

head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("blue")
head.fillcolor("red")
head.penup()
head.goto(0,0)
head.direction="stop"


#creating a food for snake



food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.fillcolor("blue")
food.penup()
food.ht()       #it means hide turtle
food.goto(150,200)
food.st()         #it means show turtle

#creating a score board
score_board=turtle.Turtle()
score_board.penup()
score_board.ht()
score_board.goto(-250,250)
score_board.write("Score:0  |  highest Score:0")   #to print a message for first time


#creating a function for moving in all direction

def moveUp():
    if head.direction!="down":
        head.direction="up"

def moveDown():
    if head.direction!="up":
        head.direction="down"

def moveLeft():
    if head.direction!="right":
        head.direction="left"

def moveRight():
    if head.direction!="left":
        head.direction="right"

def moveStop():
    head.direction="stop"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)


#event handling

s.listen()
s.onkey(moveUp,"Up")
s.onkey(moveDown,"Down")
s.onkey(moveLeft,"Left")
s.onkey(moveRight,"Right")
s.onkey(moveStop,"space")


#main loop

while True:
    s.update()  #to update the screen
    #check collision with border
    if head.xcor()>290:
        head.setx(-290)


    if head.xcor()<-290:
        head.setx(290)


    if head.ycor()>290:
        head.sety(-290)

    if head.ycor()<-290:
        head.sety(290)
#check collision with food
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        #increase the body of snake
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        bodies.append(body)  #append new body in list
        score_card=score_card+100   #increase the score
        delay=delay-0.001   #increase the speed
        if score_card>highest_score:
            highest_score=score_card   #update highest score
            score_board.clear()
            score_board.write("Score:{}  |  Highest Score:{}".format(score_card,highest_score))

    #move snake bodies

    for i in range(len(bodies)-1,0,-1):
        x=bodies[i-1].xcor()
        y=bodies[i-1].ycor()
        bodies[i].goto(x,y)

        if len(bodies)>0:
             x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
       
    move()

#check collision with snake body itself

    for body in bodies:
            if body.distance(head)<20:
                time.sleep(1)
                head.goto(0,0)
                head.direction="stop"
                #hide bodies
                for body in bodies:
                    body.ht()
                bodies.clear()

                score_card=0
                delay=0.1
                score_board.clear()
                score_board.write("Score:{}  |  highest Score:{}".format(score_card,highest_score))

    time.sleep(delay)


s.mainloop()


      


    

            
        
   
