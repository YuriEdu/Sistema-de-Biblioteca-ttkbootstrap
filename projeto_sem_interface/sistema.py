from datetime import date
import json
from funções import cadastrar, listar, emprestar, emprestados, devolver, salvar

livros = []
multa = 2

with open('dados_biblioteca.json', 'r', encoding='utf-8') as arquivo:
    livros = json.load(arquivo)

for i in livros:
    data_inteira = []
    if i['status'][0]:
        data = i['status'][1].split('-')
        for e in data:
            data_inteira.append(int(e))
        data_formatada = date(*data_inteira)
        i['status'][1] = data_formatada

        hoje = date.today()
        intervalo = hoje - i['status'][1]
        i['multa'] = multa * (intervalo.days - 14) if (intervalo.days - 14) > 0 else 0.0

while True:
    print('''
    ---------------------------------Menu---------------------------------
          
    1 - Cadastrar livro
    2 - Listar livros
    3 - Emprestar livro(s)
    4 - Devolver livro(s)
    5 - Livros emprestados
    6 - Salvar
    0 - Salvar e sair
          ''')
    
    opção = input('Digite a opção do menu que deseja: ')

    match opção:
        case '1':
            print('\n    ---------------------------Cadastrando Livro---------------------------')
            cadastrar(livros)
        case '2':
            print('\n    ----------------------------Listando Livros----------------------------')
            listar(livros)
        case '3':
            print('\n    ----------------------------Emprestar Livro----------------------------')
            emprestar(livros)
        case '4':
            print('\n    -----------------------------Devolver Livro-----------------------------')
            devolver(livros)
        case '5':
            print('\n    ----------------------Listando Livros Emprestados----------------------')
            emprestados(livros)
        case '6':
            salvar(livros)
        case '0':
            break

salvar(livros)
print('Saindo do Sistema.')