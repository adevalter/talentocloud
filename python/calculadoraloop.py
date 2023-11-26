def calculadora(valor1, valor2, operacao):
    if(operacao == 1):
        return (valor1 + valor2)
    elif (operacao == 2):
        return (valor1 - valor2)
    elif (operacao == 3):
        return (valor1 * valor2)
    elif (operacao == 4):
        return (valor1 / valor2)
    else:
        return 0
        
while(True):
    print("=============================================================")        
    print("====================== CALCULADORA ==========================")
    print("Para realizar os calculos escolha umas das operações abaixo")
    print(" 1. Soma \n 2. Subtração \n 3. Multiplicação \n 4. Divisão \n 0: Sair")
    operacao = int(input("Qual operação deseja realizar ? .: "))
   
    if operacao == 0:
        print("Sistema Encerrado")
        break
    elif operacao > 4:
        print("Essa opção não existe")
    else:
        valor1 = int(input("Informe primeiro valor            .: "))
        valor2 = int(input("Informe segundo valor             .: "))
        print("")
        resultado = calculadora(valor1,valor2,operacao)
        print(f'Resultado da Sua Operação é : {resultado}')