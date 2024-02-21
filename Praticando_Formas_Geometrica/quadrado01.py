# Este código cria um desenho de um quadrado que vai sendo repetida e também mudando a cor de cada quadrado para vermelho, ciano, verde, laranja, azul, lima, azul claro.
# É importado a biblioteca Tartaruga(turtle)

import turtle

turtle.speed(0)
turtle.bgcolor("black")

for i in range(5):
	for color in ['red','cyan', 'green','orange','blue','lime','lightblue']:
		turtle.color(color)
		turtle.pensize(3)
		turtle.lt(12)
		for j in range(4):
			turtle.fd(200)
			turtle.lt(90)
turtle.done()
