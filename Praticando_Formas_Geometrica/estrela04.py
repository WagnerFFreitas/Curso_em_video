# Este código cria um desenho de uma estrela de cinco pontas que vai sendo repetida formando um aspiral de cor vermelha
# É importado a biblioteca Tartaruga(turtle)

import turtle
import colorsys

t=turtle.Turtle( )
s=turtle.Screen( )

s.bgcolor('black')
t.speed (0)
n=50
h=0
for i in range (360):
	c=colorsys.hsv_to_rgb(n, 1, 0.8)
	h+=1/n
	t.color(c)
	t. forward(i*2)
	t.left(145)