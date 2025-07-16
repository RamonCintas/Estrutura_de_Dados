# Lista para armazenar números válidos
numeros_validos = []

# Loop até que 5 números válidos sejam inseridos
while len(numeros_validos) < 5:
    try:
        # Solicita um número inteiro
        numero = int(input("Digite um número inteiro positivo: "))
        
        # Verifica se o número é positivo
        if numero > 0:
            numeros_validos.append(numero)  # Adiciona à lista
        else:
            print("Número inválido! Por favor, insira um número positivo.")
    except ValueError:
        # Trata entrada que não seja número inteiro
        print("Entrada inválida! Por favor, insira um número inteiro.")

# Exibe os números válidos inseridos
print("Números válidos:", ' '.join(map(str, numeros_validos)))
