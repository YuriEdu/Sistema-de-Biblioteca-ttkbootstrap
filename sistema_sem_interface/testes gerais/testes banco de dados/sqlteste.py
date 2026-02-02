import sqlite3

def criar_banco_e_tabela():
    """Conecta ao banco de dados (ou cria se não existir) e cria uma tabela."""
    conn = sqlite3.connect('testes banco de dados/contas.db') # Cria/conecta a um arquivo de BD chamado contas.db
    cursor = conn.cursor()

    # Cria a tabela 'contas_a_pagar' se ela não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contas_a_pagar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL,
            data_vencimento TEXT NOT NULL
        )
    ''')
    
    # Salva (commita) as mudanças
    conn.commit()
    # Fecha a conexão
    conn.close()
    print("Banco de dados e tabela criados com sucesso.")

def inserir_conta(descricao, valor, data_vencimento):
    """Insere uma nova conta na tabela."""
    conn = sqlite3.connect('testes banco de dados/contas.db')
    cursor = conn.cursor()
    
    # Insere um novo registro na tabela
    cursor.execute("INSERT INTO contas_a_pagar (descricao, valor, data_vencimento) VALUES (?, ?, ?)", 
                   (descricao, valor, data_vencimento))
    
    # Salva (commita) as mudanças
    conn.commit()
    # Fecha a conexão
    conn.close()
    print(f"Conta '{descricao}' inserida com sucesso.")

def listar_contas():
    """Lista todas as contas salvas no banco de dados."""
    conn = sqlite3.connect('testes banco de dados/contas.db')
    cursor = conn.cursor()
    
    # Seleciona todos os registros da tabela
    cursor.execute("SELECT * FROM contas_a_pagar")
    registros = cursor.fetchall()
    
    print("\n--- Contas a Pagar ---")
    for registro in registros:
        print(f"ID: {registro[0]}, Descrição: {registro[1]}, Valor: R${registro[2]:.2f}, Vencimento: {registro[3]}")
    print("----------------------")
    
    # Fecha a conexão
    conn.close()

# --- Exemplo de uso ---

# 1. Cria o banco de dados e a tabela (execute apenas uma vez ou no início do programa)
criar_banco_e_tabela()

# 2. Insere algumas contas de exemplo
inserir_conta("Aluguel", 1500.00, "2025-11-10")
inserir_conta("Energia", 250.75, "2025-11-15")
inserir_conta("Internet", 99.90, "2025-11-20")

# 3. Lista as contas para verificar se foram salvas
listar_contas()
