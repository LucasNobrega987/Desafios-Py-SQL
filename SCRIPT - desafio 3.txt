# Importa módulos necessários do Flask
from flask import Flask, request, jsonify, abort

# Cria uma instância da aplicação Flask
app = Flask(__name__)

# Lista para armazenar as interações (substitui um banco de dados para simplificação)
interactions = []

# Define uma rota para adicionar interações entre personagens via método POST
@app.route('/interaction', methods=['POST'])
def add_interaction():
    # Obtém os dados JSON enviados na requisição
    data = request.get_json()
    # Verifica se a interação é do 4º livro
    if data['book'] == "4":  
        # Adiciona a interação à lista de interações
        interactions.append(data)
        # Retorna uma resposta JSON indicando sucesso e o código de status HTTP 201 (Created)
        return jsonify({'message': 'Interaction added successfully'}), 201
    else:
        # Retorna um erro HTTP 400 (Bad Request) se a interação não for do livro 4
        return abort(400, description="Only interactions from book 4 are accepted.")

# Função auxiliar para encontrar amigos em comum entre dois personagens
def find_common_friends(source, target):
    # Conjuntos para armazenar amigos do source e do target
    source_friends = set()
    target_friends = set()
    
    # Constroi os conjuntos de amigos para source e target
    for interaction in interactions:
        # Adiciona amigos ao conjunto de source
        if interaction['source'].lower() == source.lower():
            source_friends.add(interaction['target'].lower())
        elif interaction['target'].lower() == source.lower():
            source_friends.add(interaction['source'].lower())
        
        # Adiciona amigos ao conjunto de target
        if interaction['source'].lower() == target.lower():
            target_friends.add(interaction['target'].lower())
        elif interaction['target'].lower() == target.lower():
            target_friends.add(interaction['source'].lower())

    # Encontra a interseção dos conjuntos de amigos (amigos em comum)
    common_friends = source_friends.intersection(target_friends)
    # Retorna a lista de amigos em comum, formatados com a primeira letra maiúscula
    return [friend.title() for friend in common_friends]

# Define uma rota para consultar amigos em comum entre dois personagens via método GET
@app.route('/common-friends', methods=['GET'])
def common_friends():
    # Obtém os parâmetros source e target da URL
    source = request.args.get('source')
    target = request.args.get('target')

    # Verifica se ambos os parâmetros foram fornecidos
    if not source or not target:
        # Retorna um erro HTTP 400 (Bad Request) se algum parâmetro estiver ausente
        return abort(400, description="Both 'source' and 'target' parameters are required.")

    # Encontra a lista de amigos em comum usando a função auxiliar
    common_friends_list = find_common_friends(source, target)
    # Retorna a lista de amigos em comum em formato JSON
    return jsonify({"common_friends": common_friends_list})

# Define uma rota na raiz que retorna uma mensagem simples
@app.route('/')
def home():
    return "Hello, Flask is running!"

# Bloco condicional para executar a aplicação somente se este script for o ponto de entrada principal
if __name__ == '__main__':
    # Inicia a aplicação Flask com o modo de depuração ativado
    app.run(debug=True)
