from collections import deque

# Cria uma fila com capacidade máxima de 100 elementos
fila_de_espera = deque(maxlen=100)

# Solicita a quantidade de pessoas para adicionar na fila
quantidade = int(input("Quantas pessoas deseja adicionar à fila de espera? (Máximo 100): "))

# Limita a quantidade a 100, se necessário
if quantidade > 100:
    quantidade = 100
    print("A quantidade foi ajustada para 100.")

# Adiciona nomes à fila com base na quantidade informada
for i in range(quantidade):
    nome = input(f"Digite o nome da pessoa {i + 1}: ")
    fila_de_espera.append(nome)

# Exibe a fila de espera completa
print("\nFila de Espera:")
for pessoa in fila_de_espera:
    print(pessoa)
