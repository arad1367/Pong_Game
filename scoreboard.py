from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_user_score = 0
        self.l_user_score = 0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.goto(100, 180)
        self.write(self.r_user_score, align='center', font=('Courier', 80, 'bold'))
        self.goto(-100, 180)
        self.write(self.l_user_score, align='center', font=('Courier', 80, 'bold'))
        self.goto(0, -270)
        self.write("Created by Pejman", align='center', font=('Courier', 15, 'bold'))
    def l_score(self):
        self.l_user_score += 1
        self.update_scoreboard()
    def r_score(self):
        self.r_user_score += 1
        self.update_scoreboard()