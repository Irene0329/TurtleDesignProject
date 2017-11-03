import turtle
bob = turtle.Turtle()
turtle.colormode(255)
bob.speed(25)
turtle.bgcolor(0,0,0)

for times in range(255):
    bob.color(0,times,0)
    bob.right(150)
    bob.circle(20)
    bob.right(200)
    bob.width(5)
    bob.forward(100)
    bob.right(225)
    bob.color(times,0,times)
    bob.forward(50)
    bob.circle(20)
    bob.right(250+10)
    bob.forward(250)
    bob.color(0,times,times)
    bob.circle(20+10)
    bob.forward(100)

turtle.done()

