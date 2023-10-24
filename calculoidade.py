def calculo(ano):
    return 2023 - ano
executa = True
while(executa):
    try:
        print("Digite Seu Nome Completo :")
        nome = input()
        print("Digite Ano Nascimento de 1992 a 2022 :")
        ano = int(input())
        resultado = calculo(ano)
        print(f"Olá {nome} sua idade em 2023 completou ou completará {resultado}")
        executa = False
    except:
        print("Dados incorretos")