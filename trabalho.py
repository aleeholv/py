def soma_numeros():
    # Solicita ao usuário que insira dois números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    # Calcula a soma dos números
    soma = num1 + num2
    
    # Exibe o resultado da soma
    print("A soma de", num1, "e de", num2, "é", soma)

# Chama a função para executar o programa
soma_numeros()