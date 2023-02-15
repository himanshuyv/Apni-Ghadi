import turtle
import time


def date1():
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.speed(0)
    t.color("black")
    t.goto(-180, 5)
    t.write("Date-:", font=("calibari", 15, "normal"))
    t.goto(-180, -15)
    t.write(f"\n{date} {month} {year}", font=("calibari", 15, "normal"))
    if int(hour) == 23:
        t.reset()

def hour1():
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.speed(0)
    t.color("black")
    t.goto(-180, 5)
    t.write("Date-:", font=("calibari", 15, "normal"))
    t.goto(-180, -15)

    t.goto(-25, -30)
    t.write(f"{hour}:", font=("calibari", 40, "normal"))
    if int(minute)== 59:
        t.reset()

def minute1():
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.speed(0)
    t.color("black")
    t.goto(-180, 5)
    t.write("Date-:", font=("calibari", 15, "normal"))
    t.goto(-180, -15)

    t.goto(45, -30)
    t.write(f"{minute}:", font=("calibari", 40, "normal"))

    if int(second)== 59:
        t.reset()

def second1():
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.speed(0)
    t.color("black")
    t.goto(-180, 5)
    t.write("Date-:", font=("calibari", 15, "normal"))
    t.goto(-180, -15)

    t.goto(115, -30)
    t.write(f"{second}", font=("calibari", 40, "normal"))

    time.sleep(0.98)
    t.reset()


while True:

    localtime = time.asctime(time.localtime(time.time()))

    day = localtime[0:3]
    month = localtime[4:7]
    date = localtime[8:10]
    hour = localtime[11:13]
    minute = localtime[14:16]
    second = localtime[17:19]
    year = localtime[20:25]
    s = turtle.Screen()
    s.title("APNI GHADI")
    s.setup(width=400, height=100)
    s.bgcolor("sky blue")
    date1()
    hour1()
    minute1()
    second1()