import turtle
import _tkinter
import time
import random

delay = 0.1

#Score
score = 0
high_score = 0

#set up the window

wn = turtle.Screen()
wn.title("Snake game by Mayur")
wn.bgcolor("green") #background color of screen
wn.setup(width=1000 , height=1000) #setup screen_size
wn.tracer(0) #turn of Animation // screen updates

#Snake Head
head = turtle.Turtle()
head.speed(0) #animation speed of turtle module
head.shape("square")
head.color("black")
head.penup() #does not draw anthing
head.goto(0,0) #tobe in center when starts
head.direction = "stop"

#Snake_Food
food = turtle.Turtle()
food.speed(0) 
food.shape("circle")
food.color("red")
food.penup() 
food.goto(0,100) 

segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 460)
pen.write("Score: 0     High Score: 0",align="center", font=("Courier", 24 ,"normal"))

#Function
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

#Function
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#keyboard binding
wn.listen() #listen when you press any keys
wn.onkeypress(go_up , "w")
wn.onkeypress(go_down , "s")
wn.onkeypress(go_left , "a")
wn.onkeypress(go_right , "d")

#Main game loop
while True:
    wn.update()

    #check for collision with the border
    if head.xcor() > 490 or head.xcor() < -490 or head.ycor() > 490 or head.ycor() < -490:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        #hide the segments
        for segment in segments:
            segment.goto(1200,1200)
        
        #clear the segment list
        segments.clear()

        #reset the score
        score = 0

        #Reset the Delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}     High Score: {}".format(score, high_score), align="center", font=("Courier", 24 ,"normal"))


    #Check for the collition for the food
    if head.distance(food) < 20:
        #move food to random spot on screen
        x = random.randint(-490, 490)
        y = random.randint(-490, 490)
        food.goto(x, y)

        #Add a Segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #Shorten the delay
        delay -= 0.001

        #Increase Score
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}     High Score: {}".format(score, high_score), align="center", font=("Courier", 24 ,"normal"))
    
    #Move the end segment first
    for index in range(len(segments)-1 , 0 , -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #Move segment 0 to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    #Check for head collsion with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            #hide the segments
            for segment in segments:
                segment.goto(1200,1200)
            
            #clear the segment list
            segments.clear()

            score = 0
            
            #Reset the Delay
            delay = 0.1

            pen.clear()
            pen.write("Score: {}     High Score: {}".format(score, high_score), align="center", font=("Courier", 24 ,"normal"))

         
    time.sleep(delay)

wn.mainloop() #keep window open for us 