from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    

    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

# Keep the game window open
screen.mainloop()
