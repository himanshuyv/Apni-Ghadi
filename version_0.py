import turtle
import time

def main():
    t = turtle.Turtle()
    t.pensize(width=0)
    t.hideturtle()
    t.penup()
    t.speed(0)
    t.color("black")
    t.goto(-180, 5)
    t.write("Date-:", font=("calibari", 15, "normal"))
    t.goto(-180, -15)
    t.write(f"\n{date} {month} {year}", font=("calibari", 15, "normal"))
    t.color("black")

    t.goto(-25, -30)
    t.write(f"{hour}:", font=("calibari", 40, "normal"))

    t.goto(45, -30)
    t.write(f"{minute}:", font=("calibari", 40, "normal"))

    t.goto(115, -30)
    t.write(f"{second}", font=("calibari", 40, "normal"))
    time.sleep(0.98)
    t.reset()
    t.hideturtle()

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
    main()
