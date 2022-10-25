# libraries and make screen
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgpic("wallgif.gif")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

# call class
l_paddle = Paddle((-350,0))
r_paddle = Paddle ((350, 0))
ball = Ball()
score = Scoreboard()

# keyboard movement
screen.listen()
screen.onkey(key="Up" , fun=r_paddle.go_up)
screen.onkey(key="Down" , fun=r_paddle.go_down)
screen.onkey(key="s" , fun=l_paddle.go_up)
screen.onkey(key="x" , fun=l_paddle.go_down)



# update and tracer(0)
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.y_bounce()
    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()
    # Detect when r_paddle missed
    if ball.xcor() > 380:
        score.r_score()
        ball.reset_position()
    # Detect when l_paddle missed
    if ball.xcor() < -380:
        score.l_score()
        ball.reset_position()

screen.exitonclick()