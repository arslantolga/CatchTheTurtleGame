import turtle
import time
from random import randint

baslangic_zamani = time.time()

#Turtle Screen Definitions
turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Catch The Turtle Game")
turtle_screen.setup(1000,700)

#Turtle Object 1 Definitions
turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.color("green")
turtle_instance.shapesize(3)
turtle_instance.penup()

#Turtle Object 2 Definitions
turtle_instance2 = turtle.Turtle()
turtle_instance2.color("black")
turtle_instance2.penup()
turtle_instance2.hideturtle()
turtle_instance2.goto(-40,230)

#Turtle Object 3 Definitions
turtle_instance3 = turtle.Turtle()
turtle_instance3.color("red")
turtle_instance3.penup()
turtle_instance3.hideturtle()
turtle_instance3.goto(-480,260)

#Position Control Function
def position_control(x,y):
    x_cor, y_cor = turtle_instance.position()
    # Compare mause position and object position
    if (x_cor-20) <= int(x) <= (x_cor+20) and (y_cor-20) <= int(y) <= (y_cor+20):
        global score
        score = score + 1

#Game Starting Function
def start_game():
    global score
    score = 0
    while time.time() - baslangic_zamani < 20:
        x_cor = randint(-200, 200)
        y_cor = randint(-200, 200)
        turtle_instance.hideturtle()
        turtle_instance.goto(x_cor, y_cor)
        turtle_screen.listen()
        turtle_screen.onclick(fun=score, btn=1, add=None)
        turtle_screen.onscreenclick(position_control)
        turtle_instance.showturtle()
        printing_timer()
        printing_menu()
        time.sleep(1)
    printing_timer("Game Over!")

#Game Closing Function
def closing_game():
    turtle_screen.bye()

#Game Printing Function
def printing_timer():
    message = f"""
            Score : {score}
            Time : {int(baslangic_zamani-time.time())+20}
            """
    turtle_instance2.clear()
    turtle_instance2.write(message, align="center", font=("Arial", 24, "bold"))

def printing_menu():
    message = f"""
            Start : 'S'
            Quit : 'Q'
            """
    turtle_instance3.clear()
    turtle_instance3.write(message, align="center", font=("Arial", 16, "bold"))

printing_menu()

turtle_screen.listen()
turtle_screen.onkey(fun=start_game,key="s")
turtle_screen.onkey(fun=closing_game,key="q")


turtle_screen.mainloop()
