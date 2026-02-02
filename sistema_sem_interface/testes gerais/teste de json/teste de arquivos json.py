import json

'''
# 1. Crie um objeto Python (por exemplo, um dicionário)
dados = {
    "nome": "Alice",
    "idade": 30,
    "cidade": "São Paulo"
}

# 2. Use 'with' para abrir o arquivo no modo de escrita ('w')
# A extensão .json é usada para identificar o arquivo como JSON

with open('projeto Linguagem de Programação/dados.json', 'w', encoding='utf-8') as arquivo:
    # 3. Use json.dump() para escrever os dados no arquivo
    # O primeiro argumento é o objeto Python, o segundo é o objeto de arquivo
    json.dump(dados, arquivo, ensure_ascii=False)

print("Dados salvos com sucesso em dados.json!")
'''

data = {
    "name": "Jane Smith",
    "age": 25,
    "city": "New York"
}

file_path = "formatted_data.json"

with open('dados.json', "w") as json_file:
    json.dump(data, json_file, indent=4)

print(f"Data saved to {file_path} with formatting.")