from turtle import *
from random import randrange
from freegames import*
setup(600, 600)
bgcolor("black")
title("Snake Game")


snake = [vector(15, 0)]
goal = vector(0, -15)
food = vector(0, 0)


def Difference(x, y):
    goal.x = x  # X Axis
    goal.y = y  # Y Axis


listen()
onkey(lambda: Difference(15, 0), 'Right')
onkey(lambda: Difference(-15, 0), 'Left')
onkey(lambda: Difference(0, 15), 'Up')
onkey(lambda: Difference(0, -15), 'Down')


def Play():
    head = snake[-1].copy()
    head.move(goal)
    if not (-300 < head.x < 300 and -300 < head.y < 300) or head in snake:
        square(head.x, head.y, 10, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print(len(snake))
        food.x = randrange(-10, 10)*15
        food.y = randrange(-10, 10)*15

    else:
        snake.pop(0)

    clear()
    for b in snake:
        square(b.x, b.y, 10, 'white')
    square(food.x, food.y, 10, 'red')
    update()
    ontimer(Play, 120)


# Main
hideturtle()
tracer(False)
Play()
done()
