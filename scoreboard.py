from turtle import Turtle

BOARD_ALIGNMENT = "center"
TEXT_FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(0, 250)
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=BOARD_ALIGNMENT, font=TEXT_FONT)

    # def end_game(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over", align=BOARD_ALIGNMENT, font=TEXT_FONT)

    def increase_score(self):
        self.score += 1

    def set_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=BOARD_ALIGNMENT, font=TEXT_FONT)


