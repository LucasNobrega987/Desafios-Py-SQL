import csv
from collections import defaultdict

# Função para carregar dados do arquivo CSV e construir um dicionário de interações
def carregar_dados(filepath):
    # defaultdict para criar um dicionário onde cada chave é um personagem e cada valor é um conjunto de personagens com quem interage
    interacoes = defaultdict(set)
    # Abre o arquivo CSV no modo leitura com o encoding especificado
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)  # Pula o cabeçalho do arquivo
        for row in reader:
            p1, p2, _, _ = row  # Assume que as colunas são personagem1, personagem2, peso, livro
            # Adiciona cada personagem ao conjunto de interações do outro
            interacoes[p1].add(p2)
            interacoes[p2].add(p1)
    return interacoes

# Função para encontrar amigos em comum entre todos os pares de personagens
def encontrar_amigos_em_comum(interacoes):
    amigos_em_comum = []  # Lista para armazenar os resultados
    personagens = list(interacoes.keys())  # Lista de todos os personagens
    # Loop duplo para comparar cada par de personagens
    for i in range(len(personagens)):
        for j in range(i + 1, len(personagens)):
            p1, p2 = personagens[i], personagens[j]
            # Encontra a interseção dos conjuntos de amigos, i.e., amigos em comum
            comuns = interacoes[p1].intersection(interacoes[p2])
            # Se existirem amigos em comum, adiciona o par de personagens e os amigos à lista
            if comuns:
                amigos_em_comum.append(f"{p1}\t{p2}\t{','.join(comuns)}")
    return amigos_em_comum

# Bloco principal para execução do script
if __name__ == "__main__":
    # Caminhos dos arquivos de entrada e saída
    filepath = r'C:\Users\LucasNóbrega\Desktop\ESTUDOS\dataset.csv'
    output_path = r'C:\Users\LucasNóbrega\Desktop\ESTUDOS\PROJETO EM PYTHON\Desafio_2\amigos_comuns.csv'
    
    # Carrega os dados e encontra os amigos em comum
    interacoes = carregar_dados(filepath)
    resultados = encontrar_amigos_em_comum(interacoes)
    
    # Abre o arquivo de saída para escrita e grava os resultados
    with open(output_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Escreve o cabeçalho no arquivo CSV
        writer.writerow(['personagem1', 'personagem2', 'amigos_em_comum'])
        # Escreve cada linha de resultado no arquivo CSV
        for resultado in resultados:
            p1, p2, amigos = resultado.split('\t')
            writer.writerow([p1, p2, amigos])
