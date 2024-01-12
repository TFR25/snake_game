import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Hungry Python")

# Turn animation off, hide snake parts
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

start_game = True
while start_game:
    # Re-draw screen with snake parts in position
    screen.update()
    time.sleep(0.3)

    snake.move()

    # Detect collision with food, create new food in random location
    if snake.head.distance(food) < 15:
        food.create_food()
        scoreboard.increase_score()
        snake.extend()
        scoreboard.update_scoreboard()

    # Detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.set_high_score()
        scoreboard.update_scoreboard()
        snake.reset_snake()
        # start_game = False
        # scoreboard.end_game()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.set_high_score()
            scoreboard.update_scoreboard()
            snake.reset_snake()
            # start_game = False
            # scoreboard.end_game()


screen.exitonclick()
