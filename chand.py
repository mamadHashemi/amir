import turtle
A = int(input('Please enter your number'))
H=A
c=180-(((H-2)*180)/H)
s=turtle.Screen()
l=turtle.Turtle()
l.pensize(3)
for b in range(A) :
    for i in range(H) :
        l.forward(100)
        l.left(c)
    H=H-1
    c=180-(((H-2)*180)/H)
    
s.exitonclick()        