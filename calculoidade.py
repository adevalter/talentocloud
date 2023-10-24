def calculo(ano):
    return 2022 - ano
executa = True
while(executa):
    try:
        print("Digite Seu Nome:")
        nome = input()
        print("digite Ano Nascicomento de 1922 a 2022:")
        ano = int(input())
        if (ano >= 1922 and ano <= 2022):
            resultado = calculo(ano)
            print(f"Olá {nome} sua idade em 2022 é {resultado}")
            executa = False
        else:
           print("Dados Invalidos Digite Ano Nascimento entre 1002 a 2022") 
    except:
        print("Dados incorretos")