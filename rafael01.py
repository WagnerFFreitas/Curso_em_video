nome=input('qual é o seu nome?')
idade=input('qual sua idade?')
data=input('quando você nasceu?')
peso=input('qual é o seu peso?')
time=input('qual seu time?')
opção = 0
while opção != 7:
    print('''    [ 1 ] seu nome
    [ 2 ] seu idade
    [ 3 ] sua data
    [ 4 ] seu peso
    [ 5 ] tudo junto
    [ 6 ] qual time você torce
    [ 7 ] quer acabar o registro''')
    opção = int(input('Qual é a sua opção?'))
    if opção == 1:
        print('Olá', nome, 'como você estar.')
        nome=input('bem ou mal?')
        print('que bom.')
    elif opção == 2:
        print('sua idade é de', idade,'anos !' )
    elif opção == 3:
         print('você nasceu no dia de', data, '.')
    elif opção == 4:
        print('seu peso é de', peso, '.')
    elif opção == 5:
        print('seu nome é', nome, 'e você nasceu no dia ', data, 'por isso você fez ou vai fazer', idade, 'e mais uma informação você pesa', peso, 'kilos', 'e seu time é o', time, '.')
    elif opção == 6:
        print('Seu time de coração é o', time, '.')
    elif opção == 7:
        print('Registro finalizado com sucesso.')
    else:
        print('Opção inválida. Tente novamente')
print('até a próxima, jovem aprendiz.')