# Este código cria um desenho de um hexágono que vai sendo repetida e também mudando a sua cor das linhas em forma espiral.
# É importado a biblioteca Tartaruga(turtle)

import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
	t.pencolor(colors[x%6])
	t.width(x//100 + 1)
	t.forward(x)
	t.left(59)
