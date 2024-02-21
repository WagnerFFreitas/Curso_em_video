# Este código cria um desenho de um hexágono que vai sendo repetida e também mudando a sua cor das linhas em forma espiral com uma velocidade maior que o arquivo hexagono01.py.
# É importado a biblioteca Tartaruga(turtle)

import turtle

w = turtle.Screen()
w.title('Spiral Helix')
w.bgcolor('black')

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

t = turtle.Turtle()  # Corrija esta linha, substituindo 'pen' por 'Turtle'
t.speed(100)

for x in range(360):
    color = colors[x % len(colors)]
    t.pencolor(color)
    t.width(x / 100 + 1)
    t.forward(x)
    t.left(59)
turtle.done()