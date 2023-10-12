from turtle import Turtle
from helpers import Conway
import time

BOARD_SIZE = 20


def main():
    conway = Conway(BOARD_SIZE)
    turtle = Turtle()
    turtle.speed(0)
    turtle.hideturtle()
    turtle.screen.bgcolor("black")
    while True:
        render_board(conway, turtle)
        conway.update_board()
    turtle.screen.mainloop()


def render_board(conway, turtle: Turtle):
    turtle.screen.tracer(0)
    dimensions = turtle.screen.screensize()
    turtle.penup()
    turtle.goto(-dimensions[0], dimensions[1])
    step = dimensions[0] / BOARD_SIZE

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if conway.board[i][j] == 1:
                turtle.pendown()
                turtle.dot(step, "yellow")
                turtle.penup()
            turtle.forward(step)
        p = turtle.position()
        turtle.goto(p[0] - step * BOARD_SIZE, p[1] - step)

    turtle.screen.update()
    time.sleep(0.3)
    turtle.clear()


if __name__ == "__main__":
    main()
