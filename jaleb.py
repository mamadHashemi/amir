import turtle
A = int(input('Please enter your number'))
c=180-(((A-2)*180)/A)
s=turtle.Screen()
l=turtle.Turtle()
l.pensize(3)
for b in range(300) :
    for i in range(A) :
        l.forward(100)
        l.left(c)
    l.left(5)    