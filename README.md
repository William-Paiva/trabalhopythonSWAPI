Star Wars API Integration System
Este projeto é uma API desenvolvida em Python que utiliza dados da SWAPI (Star Wars API) para interagir com personagens, filmes, naves, veículos, espécies e planetas da franquia Star Wars. Além de consumir os dados da SWAPI, o sistema permite salvar e gerenciar essas informações em um banco de dados local SQLite.

Tecnologias Utilizadas
1. Flask
Framework de desenvolvimento web para Python. Ele permite criar APIs de forma simples e eficiente.
A API construída utiliza rotas para interagir com os dados da SWAPI e fazer a comunicação com o banco de dados SQLite.
2. SQLite
Um banco de dados leve e autônomo, ideal para pequenos projetos.
Todas as informações que o usuário salva, como personagens, filmes, naves e favoritos, são armazenadas em um banco de dados local SQLite.
3. Requests
Biblioteca Python utilizada para fazer as requisições HTTP. Através dela, a aplicação faz as chamadas à SWAPI para buscar os dados sobre o universo Star Wars.
4. SWAPI (Star Wars API)
A Star Wars API fornece dados completos e detalhados sobre os filmes, personagens, naves e outros elementos da franquia. A aplicação interage com a SWAPI para buscar essas informações e exibi-las ou salvá-las localmente.
5. SQLite3
O módulo nativo do Python utilizado para conectar e executar comandos no banco de dados SQLite.
Funcionalidades da API
A API oferece várias rotas para interagir com os dados da SWAPI, realizar operações de salvar e deletar informações no banco de dados, além de gerenciar favoritos:


Como Funciona o Sistema
Consumindo Dados da SWAPI:

Ao acessar as rotas de personagens, filmes, naves, etc., a aplicação faz requisições à SWAPI para obter as informações e retorná-las ao usuário em formato JSON.
Salvando Dados no Banco de Dados:

Os usuários podem salvar dados específicos (como personagens e filmes) no banco de dados local (SQLite) ao acessar as rotas correspondentes de save.
Gerenciando Favoritos:

O sistema permite que o usuário salve um conjunto de favoritos (personagem, filme, nave, veículo, espécie e planeta) e visualize essas informações em outra rota.


Como Rodar o Projeto
Clone o repositório:

bash
Copiar código
git clone <URL_DO_REPOSITÓRIO>
cd star-wars-api
Crie e ative um ambiente virtual (opcional, mas recomendado):

bash
Copiar código
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Inicie a aplicação:

bash
Copiar código
python app.py
A API estará disponível em http://localhost:5000.
