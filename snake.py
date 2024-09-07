#Snake
#The player needs to control the snake using the (W, A, S, D) key 
#to achieve high score the user also needs to control the snake and eat the food that is randomly
#appear in the screen
#Note: that the snake is not allowed to crash to own self it causes the game over

import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0
game_over = False

win = turtle.Screen()
win.title("Snake Game with WASD Controls and Score Above")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 275)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 16, "normal"))

game_over_pen = turtle.Turtle()
game_over_pen.speed(0)
game_over_pen.shape("square")
game_over_pen.color("red")
game_over_pen.penup()
game_over_pen.hideturtle()
game_over_pen.goto(0, 0)

def go_up():
    if head.direction != "down" and not game_over:
        head.direction = "up"

def go_down():
    if head.direction != "up" and not game_over:
        head.direction = "down"

def go_left():
    if head.direction != "right" and not game_over:
        head.direction = "left"

def go_right():
    if head.direction != "left" and not game_over:
        head.direction = "right"

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

def check_boundaries():
    if head.xcor() > 290:
        head.setx(-290)
    if head.xcor() < -290:
        head.setx(290)
    if head.ycor() > 290:
        head.sety(-290)
    if head.ycor() < -290:
        head.sety(290)

def display_game_over():
    game_over_pen.write("GAME OVER", align="center", font=("Courier", 36, "bold"))

def reset_game():
    global score, delay, game_over
    score = 0
    delay = 0.1
    game_over = False

    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()

    head.goto(0, 0)
    head.direction = "stop"

    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    food.goto(x, y)

    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 16, "normal"))

win.listen()
win.onkey(go_up, "w") 
win.onkey(go_down, "s")  
win.onkey(go_left, "a")  
win.onkey(go_right, "d")  

try:
    while True:
        win.update() 
        if not game_over:
            check_boundaries()
            if head.distance(food) < 20:
                x = random.randint(-290, 290)
                y = random.randint(-290, 290)
                food.goto(x, y)
                new_segment = turtle.Turtle()
                new_segment.shape("square")
                new_segment.color("grey")
                new_segment.penup()
                segments.append(new_segment)

                delay -= 0.001

                score += 10
                if score > high_score:
                    high_score = score

                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 16, "normal"))

            for index in range(len(segments) - 1, 0, -1):
                x = segments[index - 1].xcor()
                y = segments[index - 1].ycor()
                segments[index].goto(x, y)

            if len(segments) > 0:
                x = head.xcor()
                y = head.ycor()
                segments[0].goto(x, y)

            move() 

            for segment in segments:
                if segment.distance(head) < 20:
                    display_game_over()
                    game_over = True
                    time.sleep(1)
                    reset_game()
                    game_over_pen.clear()

        time.sleep(delay)

except turtle.Terminator:
    print("Turtle graphics window closed.")
finally:
    turtle.bye()
