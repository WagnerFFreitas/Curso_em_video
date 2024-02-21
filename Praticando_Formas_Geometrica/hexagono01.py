# Este código cria um desenho de um hexágono que vai sendo repetida e também mudando a cor de cada linha para vermelho, roxo,azul, verde, laranja e amarelo em forma espiral.
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
