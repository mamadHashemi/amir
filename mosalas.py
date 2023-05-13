import turtle
c=180-(((3-2)*180)/3)
k=200
s=turtle.Screen()
l=turtle.Turtle()
l.pensize(1)
for b in range(10) :
    for i in range(3) :
        l.forward(k)
        l.left(c)
    k=k-20
    l.left(30)
    l.penup()
    l.forward(10)
    l.pendown()
    l.right(30)

l.penup()
l.forward(1000)

s.exitonclick()