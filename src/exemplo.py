import random
import matplotlib.pyplot as plt

# Função para calcular a média
def calcular_media(notas):
    if not all(isinstance(nota, (int, float)) for nota in notas):
        raise TypeError("Todas as notas devem ser números.")
    if len(notas) == 0:
        raise ValueError("A lista de notas não pode estar vazia.")
    return sum(notas) / len(notas)

# Gerar dados de estudantes
estudantes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]
notas = {estudante: [random.uniform(5, 10) for _ in range(4)] for estudante in estudantes}

# Exibir as notas
for estudante, notas_estudante in notas.items():
    print(f'{estudante}: {notas_estudante}')

try:
    # Calcular a média de cada estudante
    medias = {estudante: calcular_media(notas_estudante) for estudante, notas_estudante in notas.items()}

    # Plotar as notas dos estudantes
    plt.figure(figsize=(10, 5))

    for estudante, notas_estudante in notas.items():
        plt.plot(range(1, len(notas_estudante) + 1), notas_estudante, marker='o', label=estudante)

    plt.title("Desempenho Acadêmico dos Estudantes")
    plt.xlabel("Trimestres")
    plt.ylabel("Notas")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Selecionar um estudante aleatoriamente e exibir suas notas
    estudante_selecionado = random.choice(estudantes)
    print(f'Estudante selecionado aleatoriamente: {estudante_selecionado}')
    print(f'Notas: {notas[estudante_selecionado]}')
    print(f'Média: {medias[estudante_selecionado]:.2f}')
except KeyError as e:
    print(f"Erro: Estudante não encontrado - {e}")
except TypeError as e:
    print(f"Erro: Tipo de dado inválido - {e}")
except ValueError as e:
    print(f"Erro: Valor inválido - {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado - {e}")
finally:
    print("Execução do script finalizada.")
