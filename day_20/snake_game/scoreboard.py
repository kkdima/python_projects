import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.load_high_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        # Position at the top-right corner (adjust based on screen size)
        self.goto(0, 260)
        self.update_scoreboard()

    def load_high_score(self):
        try:
            with open("day_20/snake_game/data.txt", "r") as file:
                return int(file.read())
        except (FileNotFoundError, ValueError):
            return 0

    def save_high_score(self):
        with open("day_20/snake_game/data.txt", "w") as file:
            file.write(str(self.highscore))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, Highscore: {
                   self.highscore}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_high_score()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
