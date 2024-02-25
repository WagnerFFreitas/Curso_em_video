time=input('Qual é o seu time?')
nota1 = float(input('Dê uma nota para ele:'))
nota2 = float(input('Dê mais uma nota:'))
média = (nota1 + nota2) /2
print('Ele tirou {:.1f} e {:.1f}, e a média de seu time é {:.1f}'.format(nota1, nota2, média))
if média >=5 and média < 6:
    print('O seu time está em RECUPERAÇÃO.')
elif média < 5:
    print('Seu time e RUIM o suficiente que vai desce de divisão.')
elif média >= 6:
    print('Seu time e tão BOM que poderar ser eleito a CHAMPIONS LEAGUE.')