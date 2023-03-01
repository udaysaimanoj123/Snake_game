from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen=Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game 💀")
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()
screen.listen()

screen.onkey(snake.Up,"Up")
screen.onkey(snake.Down,"Down")
screen.onkey(snake.Right,"Right")
screen.onkey(snake.Left,"Left")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase()


    if snake.head.xcor()>285 or snake.head.ycor()>285 or snake.head.xcor()<-285 or snake.head.ycor()<-285:
        snake.restart()
        score.reset()

    for i in snake.segments[1:]:
        if snake.head.distance(i)<10:
            score.resett()
            snake.restart()

screen.exitonclick()