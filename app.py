from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Lista para armazenar as interações (substitui um banco de dados para simplificação)
interactions = []

@app.route('/interaction', methods=['POST'])
def add_interaction():
    data = request.get_json()
    if data['book'] == "4":  # Aceita apenas interações do 4º livro
        interactions.append(data)  # Adiciona a interação à lista
        return jsonify({'message': 'Interaction added successfully'}), 201
    else:
        return abort(400, description="Only interactions from book 4 are accepted.")

# Helper function to find common friends
def find_common_friends(source, target):
    source_friends = set()
    target_friends = set()
    
    # Build sets of friends for source and target
    for interaction in interactions:
        if interaction['source'].lower() == source.lower():
            source_friends.add(interaction['target'].lower())
        elif interaction['target'].lower() == source.lower():
            source_friends.add(interaction['source'].lower())
        
        if interaction['source'].lower() == target.lower():
            target_friends.add(interaction['target'].lower())
        elif interaction['target'].lower() == target.lower():
            target_friends.add(interaction['source'].lower())

    # Find common friends
    common_friends = source_friends.intersection(target_friends)
    return [friend.title() for friend in common_friends]

@app.route('/common-friends', methods=['GET'])
def common_friends():
    source = request.args.get('source')
    target = request.args.get('target')

    if not source or not target:
        return abort(400, description="Both 'source' and 'target' parameters are required.")

    common_friends_list = find_common_friends(source, target)
    return jsonify({"common_friends": common_friends_list})

@app.route('/')
def home():
    return "Hello, Flask is running!"

if __name__ == '__main__':
    app.run(debug=True)
