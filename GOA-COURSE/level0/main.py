from turtle import *

speed(0)

penup()
goto(-1500, -200)
pendown()

pencolor("green")

pensize(500)

forward(3000)

pensize(1)

penup()
goto(-200, 0)
pendown()

fillcolor("lightblue")

begin_fill()
forward(400)
left(90)
forward(250)
left(90)
forward(400)
left(90)
forward(250)
left(90)
end_fill()

# karebis daxatva

penup()
goto(-25, 0)
pendown()


left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)


# saxuravis daxatva

penup()
goto(200, 250)
pendown()


fillcolor("red")


begin_fill()
right(125)
forward(265)
left(75)
forward(237)
left(140)
forward(400)
end_fill()

exitonclick()

