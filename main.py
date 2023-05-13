import turtle
import time
from random import randint

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Catch The Turtle Game")
turtle_screen.setup(1000, 700)

turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.color("green")
turtle_instance.shapesize(3)
turtle_instance.penup()

turtle_instance2 = turtle.Turtle()
turtle_instance2.color("black")
turtle_instance2.penup()
turtle_instance2.hideturtle()
turtle_instance2.goto(-40, 230)

turtle_instance3 = turtle.Turtle()
turtle_instance3.color("red")
turtle_instance3.penup()
turtle_instance3.hideturtle()
turtle_instance3.goto(-480, 260)


class player():
    def __init__(self, x_cor=0, y_cor=0, score=0):
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.score = score

    def position_control(self, x, y):
        self.x_cor = x
        self.y_cor = y
        rand_x_cor, rand_y_cor = turtle_instance.position()
        if (rand_x_cor - 20) <= self.x_cor <= (rand_x_cor + 20) and (rand_y_cor - 20) <= self.y_cor <= (
                rand_y_cor + 20):
            self.score += 1


class printing(player):

    def __init__(self, pscore=0, ptime=1):
        self.pscore = pscore
        self.ptime = ptime

    def printing_menu(self):
        self.pscore = player1.score
        self.ptime = int(start_time - time.time()) + 20
        if self.ptime > 0:
            message = f"""
                    Score : {self.pscore}
                    Time : {self.ptime}
                    """
        if self.ptime <= 0:
            message = f"""
                    Score : {self.pscore}
                    GAME OVER!
                    """
        turtle_instance2.clear()
        turtle_instance2.write(message, align="center", font=("Arial", 16, "bold"))

    def default_menu(self):
        message = f"""
                Quit : 'Q'
                """
        turtle_instance3.clear()
        turtle_instance3.write(message, align="center", font=("Arial", 16, "bold"))

def closing_game():
    turtle_screen.bye()

player1 = player()
printing1 = printing()
printing1.default_menu()
start_time = time.time()
difficulty = 0.5

while printing1.ptime > 0:
    printing1.default_menu()
    printing1.printing_menu()
    rand_x_cor = randint(-200, 200)
    rand_y_cor = randint(-200, 200)
    turtle_instance.hideturtle()
    turtle_instance.goto(rand_x_cor, rand_y_cor)
    turtle_screen.listen()
    turtle_screen.onclick(player1.position_control)
    turtle_screen.onkey(fun=closing_game,key="q")
    turtle_instance.showturtle()
    time.sleep(difficulty)

turtle_instance.hideturtle()
turtle.mainloop()
