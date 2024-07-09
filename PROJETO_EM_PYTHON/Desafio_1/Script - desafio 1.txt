import csv
from collections import defaultdict

# Função para calcular as interações entre personagens e exportar os resultados para um arquivo CSV
def computar_interacoes(filepath, output_path):
    # Dicionário para armazenar as interações. Usa defaultdict para inicializar valores default como uma lista de zeros
    interacoes = defaultdict(lambda: [0, 0, 0, 0])

    # Abre o arquivo CSV de entrada para leitura
    with open(filepath, newline='', encoding='latin1') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)  # Ignora o cabeçalho do arquivo CSV
        for row in reader:
            personagem1, personagem2, peso, livro = row
            livro = int(livro)  # Converte o número do livro para inteiro
            peso = int(peso)   # Converte o peso (número de interações) para inteiro
            interacoes[personagem1][livro - 1] += peso
            interacoes[personagem2][livro - 1] += peso

    resultado = []
    # Processa as interações armazenadas para preparar a lista de resultados
    for personagem, valores in interacoes.items():
        total_interacoes = sum(valores)  # Calcula o total de interações para o personagem
        resultado.append([personagem] + valores + [total_interacoes])

    # Ordena a lista de resultados com base no total de interações, de forma decrescente
    resultado.sort(key=lambda x: x[4], reverse=True)

    # Escreve os resultados em um arquivo CSV de saída
    with open(output_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['personagem', 'interacoes_livro1', 'interacoes_livro2', 'interacoes_livro3', 'total_interacoes'])
        writer.writerows(resultado)

if __name__ == "__main__":
    filepath = r'C:\Users\LucasNóbrega\Desktop\ESTUDOS\dataset.csv'  # Caminho do arquivo de entrada
    output_path = r'C:\Users\LucasNóbrega\Desktop\ESTUDOS\interacoes_resultados.csv'  # Caminho do arquivo de saída
    computar_interacoes(filepath, output_path)  # Executa a função
