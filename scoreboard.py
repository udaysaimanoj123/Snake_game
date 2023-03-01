from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,265)
        self.update()

    def increase(self):
        self.score+=1
        self.update()

    def update(self):
        self.clear()
        with open("highscore.txt") as uday:
            score=uday.read()
        self.write(f"Score: {self.score} High Score: {score}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        with open("highscore.txt") as uday:
            score=uday.read()
            score=int(score)
        if self.score>score:
            score=self.score
            with open("highscore.txt", mode="w") as uday:
                uday.write(str(score))
        self.score=0
        self.update()

    def dash(self):
        self.clear()
        self.score=0
        self.update()



