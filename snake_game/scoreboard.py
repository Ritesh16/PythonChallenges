from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.get_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score : {self.highscore}", align="center", font= ("Arial", 24, "normal"))
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game over", align="center", font = ("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score

        self.score = 0
        self.update_scoreboard()
        self.save_high_score()

    def get_high_score(self):
        contents = 0
        with open("data.txt") as data:
            contents = int(data.read())

        return contents

    def save_high_score(self):
        with open("data.txt", "w") as data:
            data.write(f"{self.highscore}")