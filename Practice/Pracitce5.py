import turtle
t=turtle.Screen()
t.setup(600,600)
spiral=turtle.Turtle()
spiral=turtle.Turtle()
t.bgcolor("black")
col=("Yellow","white","sky blue","red")
c=0
for i in range(50):
    spiral.forward(i*10)
    spiral.right(144)
    spiral.color(col[c])
    if c==3:
        c=0
    else:
        c+=1
        