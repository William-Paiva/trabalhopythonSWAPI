import sqlite3

# Função para conectar ao banco
def create_connection():
    connection = sqlite3.connect('swapi.db')
    return connection

# Executar queries (inserção, exclusão, etc.)
def execute_query(query):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

# Ler dados do banco
def execute_read_query(query):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()
    return result

# Criar as tabelas do banco
def create_tables():
    connection = create_connection()
    cursor = connection.cursor()

    # Criação de tabela para personagens
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS personagens (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        altura TEXT,
        massa TEXT,
        ano_nascimento TEXT
    );
    ''')

    # Tabela de filmes
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS filmes (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        numero_episodio INTEGER NOT NULL
    );
    ''')

    # Tabela de favoritos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS favoritos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        personagem TEXT,
        filme TEXT,
        nave TEXT,
        veiculo TEXT,
        especie TEXT,
        planeta TEXT
    );
    ''')

    connection.commit()
    connection.close()
