from datetime import date
import json

def importar():
    livros = []
    multa = 2

    with open('project_the_second/dados_biblioteca_2.json', 'r', encoding='utf-8') as arquivo:
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
    return livros

def cadastrar(lista):   
    while True:
        print()
        cadastro = {}
        cadastro['código'] = input('Código do Livro: ')
        cadastro['título'] = input('Título do Livro: ')
        cadastro['autor'] = input('Autor do Livro(Sobrenome, Nome): ')
        cadastro['status'] = [False, 0]
        cadastro['multa'] = 0.0
        lista.append(cadastro)
        cadastrar_outro = input('Deseja cadastrar mais um livro(s ou n): ').lower()
        if cadastrar_outro == 's':
            continue
        else:
            print('Cadastro finalizado com sucesso.')
            break

def listar(lista):
    if len(lista) % 2 == 0:
        for a in range(len(lista)):
            if a % 2 != 0:
                print(f'\nCódigo: {lista[a - 1]['código']:<40}Código: {lista[a]['código']}')
                print(f'Título: {lista[a - 1]['título']:<40}Título: {lista[a]['título']}')
                print(f'Autor: {lista[a - 1]['autor']:<41}Autor: {lista[a]['autor']}')
                print(f'Status: {'Emprestado' if lista[a - 1]['status'][0] else 'Disponível':<40}Status: {'Emprestado' if lista[a]['status'][0] else 'Disponível':<40}')
    else:
        for a in range(len(lista) - 1):
            if a % 2 != 0:
                print(f'\nCódigo: {lista[a - 1]['código']:<40}Código: {lista[a]['código']}')
                print(f'Título: {lista[a - 1]['título']:<40}Título: {lista[a]['título']}')
                print(f'Autor: {lista[a - 1]['autor']:<41}Autor: {lista[a]['autor']}')
                print(f'Status: {'Emprestado' if lista[a - 1]['status'][0] else 'Disponível':<40}Status: {'Emprestado' if lista[a]['status'][0] else 'Disponível':<40}')

        print()
        print(f'Código: {lista[len(lista) - 1]['código']}')
        print(f'Título: {lista[len(lista) - 1]['título']}')
        print(f'Autor: {lista[len(lista) - 1]['autor']}')
        print(f'Status: {'Emprestado' if lista[len(lista) - 1]['status'][0] else 'Disponível'}')

def emprestar(lista):
    livros_emprestados = []
    while True:
        empréstimo = input('\nInsira o código do livro a ser emprestado(Digite 0 para finalizar): ')
        finalizado = False
        for i in lista:
            if empréstimo == '0':
                finalizado = True
                break
            if empréstimo == i['código']:
                if not i['status'][0]:
                    print(f'{i['título']}, de {i['autor']}, emprestado com sucesso!')
                    i['status'][0] = True
                    i['status'][1] = date.today()
                    livros_emprestados.append(i)
                    break
                elif i['status'][0]:
                    print(f'{i['título']}, de {i['autor']}, não está disponível no momento.')
                    break
        else:
            print('Não há nenhum livro disponível com esse código.')
        if finalizado:
            print('Empréstimo finalizado com sucesso!')
            if len(livros_emprestados) > 0:
                print('\n ----------Livros Emprestados----------\n')
                for a in livros_emprestados:
                    print(f'Código: {a['código']}')
                    print(f'Título: {a['título']}')
                    print(f'Autor: {a['autor']}')
                    print()
            break

def emprestados(lista, valor_multa=2):
    livros_emprestados = []
    for i in lista:
        if i['status'][0]:
            livros_emprestados.append(i)
    for i in livros_emprestados:
        hoje = date.today()
        intervalo = hoje - i['status'][1]
        print(f'\nCódigo: {i['código']}')
        print(f'Título: {i['título']}')
        print(f'Autor: {i['autor']}')
        if intervalo.days > 14:
            print(f'Emprestado em {i['status'][1]}. Atrasado a {intervalo.days - 14} dias.')
            print(f'Multa = R${i['multa']:5.2f}')
        else:
            print(f'Emprestado em {i['status'][1]}. {14 - intervalo.days} dias para devolução sem multa.')

def devolver(lista):
    emprestados(lista)
    while True:
        livro = input('\nTítulo do livro a ser devolvido(0 para sair): ')
        if livro == '0':
            break 
        else:
            for i in lista:
                if livro == i['título'] and i['multa'] == 0:
                    print(f'{i['título']} devolvido com sucesso!')
                    i['status'] = [False, 0]
                    break
                elif livro == i['título'] and i['multa'] > 0:
                    pagar = input(f'O cliente deve pagar uma multa de R${i['multa']:5.2f}. Este o fez(s ou n)? ').lower()
                    if pagar == 's':
                        print(f'{i['título']} devolvido com sucesso!')
                        i['status'] = [False, 0]

            else:
                print('A multa deste livro não foi paga, este livro não foi emprestado ou ele não está no catálogo.')
                continue

def salvar(lista):
    livros_filtrados = []

    for i in lista:
        livro_filtro = i
        livro_filtro['status'][1] = str(livro_filtro['status'][1])
        livros_filtrados.append(livro_filtro)

    with open('dados_biblioteca.json', 'w', encoding='utf-8') as arquivo:
        json.dump(livros_filtrados, arquivo, ensure_ascii=False, indent=4)
    print('Dados salvos com sucesso!')