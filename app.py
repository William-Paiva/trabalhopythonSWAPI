from flask import Flask, jsonify, request
import requests
from database import create_connection, execute_query, execute_read_query, create_tables

app = Flask(__name__)
BASE_SWAPI_URL = "https://swapi.dev/api"


@app.route('/')
def status():
    return jsonify({"status": "API está funcionando!"}), 200


def fetch_data_from_swapi(endpoint):
    response = requests.get(f"{BASE_SWAPI_URL}/{endpoint}")
    if response.status_code == 200:
        return response.json(), 200
    else:
        return {"error": "Erro ao buscar dados da SWAPI"}, response.status_code


# ----------------- ROTAS DE PERSONAGENS ----------------- #
@app.route('/personagens', methods=['GET'])
def get_personagens():
    data, status = fetch_data_from_swapi('people/')
    return jsonify(data), status


@app.route('/personagens/<int:id>', methods=['GET'])
def get_personagem(id):
    data, status = fetch_data_from_swapi(f'people/{id}/')
    return jsonify(data), status


@app.route('/personagens/<int:id>/save', methods=['POST'])
def save_personagem(id):
    personagem_data, status = fetch_data_from_swapi(f'people/{id}/')
    if status == 200:
        query = f"""
        INSERT INTO personagens (id, nome, altura, massa, ano_nascimento) 
        VALUES ({id}, '{personagem_data["name"]}', '{personagem_data["height"]}', 
        '{personagem_data["mass"]}', '{personagem_data["birth_year"]}');
        """
        execute_query(query)
        return jsonify({"message": "Personagem salvo no banco de dados!"}), 201
    return jsonify({"error": "Erro ao salvar personagem"}), status


@app.route('/personagens/<int:id>/delete', methods=['DELETE'])
def delete_personagem(id):
    query = f"DELETE FROM personagens WHERE id={id};"
    execute_query(query)
    return jsonify({"message": "Personagem removido do banco de dados!"}), 200


# ----------------- ROTAS DE FILMES ----------------- #
@app.route('/filmes', methods=['GET'])
def get_filmes():
    data, status = fetch_data_from_swapi('films/')
    return jsonify(data), status


@app.route('/filmes/<int:id>', methods=['GET'])
def get_filme(id):
    data, status = fetch_data_from_swapi(f'films/{id}/')
    return jsonify(data), status


@app.route('/filmes/<int:id>/save', methods=['POST'])
def save_filme(id):
    filme_data, status = fetch_data_from_swapi(f'films/{id}/')
    if status == 200:
        query = f"""
        INSERT INTO filmes (id, nome, numero_episodio) 
        VALUES ({id}, '{filme_data["title"]}', {filme_data["episode_id"]});
        """
        execute_query(query)
        return jsonify({"message": "Filme salvo no banco de dados!"}), 201
    return jsonify({"error": "Erro ao salvar filme"}), status


@app.route('/filmes/<int:id>/delete', methods=['DELETE'])
def delete_filme(id):
    query = f"DELETE FROM filmes WHERE id={id};"
    execute_query(query)
    return jsonify({"message": "Filme removido do banco de dados!"}), 200


# ----------------- ROTAS DE FAVORITOS ----------------- #
@app.route('/favorito/save', methods=['POST'])
def save_favorito():
    data = request.json
    query = f"""
    INSERT INTO favoritos (personagem, filme, nave, veiculo, especie, planeta) 
    VALUES ('{data["personagem"]}', '{data["filme"]}', '{data["nave"]}', 
    '{data["veiculo"]}', '{data["especie"]}', '{data["planeta"]}');
    """
    execute_query(query)
    return jsonify({"message": "Favorito salvo com sucesso!"}), 201


@app.route('/getFavorito', methods=['GET'])
def get_favorito():
    query = "SELECT * FROM favoritos;"
    favorito = execute_read_query(query)
    return jsonify(favorito), 200


if __name__ == '__main__':
    create_tables()  
    app.run(debug=True)
