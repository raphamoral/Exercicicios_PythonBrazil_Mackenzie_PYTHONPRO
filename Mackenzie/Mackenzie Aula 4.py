idade=int(input(""))

if idade <5:
    print('NÃO TEM IDADE PARA SER ATLETA')
elif 5<=idade<=7:
    print('INFANTIL A')
elif 8<=idade<=10:
    print('INFANTIL B')
elif 11 <= idade <= 13:
    print('JUVENIL A')
elif 14 <= idade <= 17:
    print(('JUVENIL B'))
elif idade >=18:
    print('SÊNIOR')
elif idade<0:
    print('Idade invalida')


