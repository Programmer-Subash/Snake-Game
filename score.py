from turtle import Turtle


class Score(Turtle):
    def __init__(self, width: int, height: int):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(-80, height // 2 - 50)
        with open("highest_score.txt") as highest_score_file:
            self.highest_score = int(highest_score_file.read())

    def show_score(self):
        self.clear()
        if self.score > self.highest_score:
            self.setx(-180)
            self.write(f"Score: {self.score} High Score: {self.score}", font=("Arial", 30, "bold"))
        else:
            self.write(f"Score: {self.score}", font=("Arial", 30, "bold"))

    def update_score(self, point: int):
        self.score += point

    def game_over_message(self):
        self.goto(-100, -15)
        self.write(f"Game Over", font=("Arial", 30, "bold"))
        self.score = 0

    def update_highest_score(self):
        if self.score > self.highest_score:
            with open("highest_score.txt", mode='w') as highest_score_file:
                highest_score_file.write(str(self.score))
