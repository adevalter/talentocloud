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
        

print("=============================================================")        
print("====================== CALCULADORA ==========================")
print("Para realizar os calculos escolha umas das operações abaixo")
print(" 1. Soma \n 2. Subtração \n 3. Multiplicação \n 4. Divisão")
operacao = int(input("Qual operação deseja realizar ? .: "))
valor1 = int(input("Informe primeiro valor            .: "))
valor2 = int(input("Informe segundo valor             .: "))

resultado = calculadora(valor1,valor2,operacao)

if resultado == 0:
    print(f"Escolha da Operação inválida seu resultado é: {resultado}")
else:
    print(f'Resultado da Sua Operação é : {resultado}')
    
print("=============================================================")   