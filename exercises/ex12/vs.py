
import turtle
def square_draw(t,sz):
    for i in ['red', 'blue','purple', 'yellow']:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.title('Hey Turtle!')

max = turtle.Turtle()
max.pensize(2)

size = 20

for i in range(15):
    square_draw(max, size)
    size = size + 10
    max.forward(10)
    max.left(18)
wn.mainloop()    
