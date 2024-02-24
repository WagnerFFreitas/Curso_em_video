# Este código cria um desenho de um hexágono que vai sendo repetida e também mudando a cor de cada linha para verde, azul, amarelo, vermelho e branco em forma espiral.
# É importado a biblioteca Tartaruga(turtle)

import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
colors = ['green', 'blue', 'yellow', 'red', 'white']

for i in range(102):
    t.color(colors[i % 5])
    t.left(150)
    t.forward(i * 2)
    t.right(72)

turtle.done()