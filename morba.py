import turtle
c=180-(((4-2)*180)/4)
k=200
s=turtle.Screen()
l=turtle.Turtle()
l.pensize(1)
for b in range(10) :
    for i in range(4) :
        l.forward(k)
        l.left(c)
    k=k-20
    l.forward(10)
    l.left(90)
    l.penup()
    l.forward(10)
    l.pendown()
    l.right(90)

l.penup()
l.forward(1000)

s.exitonclick()