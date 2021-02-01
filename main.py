import turtle

print("Hello World.")

t = turtle.Turtle()

t.color('white')
t.left(90)
t.forward(100)
t.left(270)
t.color('blue')
i = 10
while i < 200:
  t.forward(i)
  t.left(90)
  i += 10

t2 = turtle.Turtle()

t2.color('white')
t2.left(270)
t2.forward(100)
t2.left(90)
t2.color('red')
i = 10
while i < 200:
  t2.forward(i)
  t2.left(90)
  i *= 1.1
