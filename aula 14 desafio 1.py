#criar um validador de Triangulo

#Apresentação

print('\n\t\t\t ---Validador de Triângulo')

#Entrada
a=int (input('Informe o lado a:'))
b=int (input('Informe o lado b:'))
c=int (input('Informe o lado c:'))

#Processamento e saída
if a < (b+c) and b < (a+c) and c < (a+b):
    print(f'\n\n{a}, {b} e {c} formam um triângulo!')

    #Tipo do Triangulo
    if ( a==b) and ( b==c):
        print('Equilátero')
    if (a==b) or (a==c) or (b==c):
        print('Isósceles')
    if (a != b) and (a != c) and (b != c):
        print('Escaleno')
else:
    print(f'\n\n{a}, {b} e {c} não formam um triângulo!')



