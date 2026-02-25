import turtle

screen=turtle.Screen()
screen.bgcolor("black")

t1=turtle.Turtle()
t1.speed(0)
t1.pensize(5)
colors=["green","red","pink","grey","white"]

for i in range(360):
    t1.pencolor(colors[i%5])
    t1.circle(i*0.5)
    t1.left(180)

turtle.done()