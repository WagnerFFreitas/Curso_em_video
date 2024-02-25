# Este código cria um desenho de duas estrelas com varias pontas que vai sendo repetida formando um espiral com varias pontas e também ao crescer vai mudando a sua cor
# É importado a biblioteca Tartaruga(turtle)

import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
n = 80
h = 0

for i in range(302):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1 / n
    t.color(c)
    t.left(104)
    t.forward(i * 3)
    
    for j in range(3):
        t.left(5)
        t.forward(i * 2)
        t.left(52)
