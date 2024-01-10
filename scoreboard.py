from turtle import Turtle

BOARD_ALIGNMENT = "center"
TEXT_FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(0, 250)
        self.write(f"Score: {self.score}", align=BOARD_ALIGNMENT, font=TEXT_FONT)

    def end_game(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=BOARD_ALIGNMENT, font=TEXT_FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=BOARD_ALIGNMENT, font=TEXT_FONT)
