from datetime import date, timedelta
import json
import tkinter as tk
import platform
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

sistema = platform.system()

if sistema == 'Windows':
    DADOSLIVROS = 'data/dados_livros.json'
    DADOSUSUÁRIOS = 'data/dados_usuários.json'
    DADOSGÊNEROS = 'data/gêneros.txt'
    DADOSSUBGÊNEROS = 'data/subgêneros.txt'

    LARGEFONT = ('Bookman Old Style', 35, 'bold')
    MEDIUMFONT = ('Verdana', 15)
    SMALLFONT = ('Verdana', 10)
    BUTTONFONT = '-size 9'

if sistema == 'Linux':
    DADOSLIVROS = 'projeto_com_interface/data/dados_livros.json'
    DADOSUSUÁRIOS = 'projeto_com_interface/data/dados_usuários.json'
    DADOSGÊNEROS = 'projeto_com_interface/data/gêneros.txt'
    DADOSSUBGÊNEROS = 'projeto_com_interface/data/subgêneros.txt'

    LARGEFONT = ('URW Bookman', 35, 'bold')
    MEDIUMFONT = ('Veranda', 15)
    SMALLFONT = ('Veranda', 10)
    BUTTONFONT = '-size 10'

btn_variables = []

import string

alfabeto = ''.join(string.ascii_lowercase) + ''.join(string.ascii_uppercase)

def validar_cpf(P):
    len_máxima = 14

    if len(P) <= len_máxima:
        return True
    else:
        return False
    
def validar_tel(P):
    len_máxima = 15

    if len(P) <= len_máxima:
        return True
    else:
        return False

def validar_ano(P):
    len_máxima = 4

    if len(P) <= len_máxima:
        return True
    else:
        return False

def formatar_cpf(event):
    if event.keysym.lower() == "backspace": return

    entry = event.widget.get()
    event.widget.delete(0, tk.END)
    for i in entry:
        if i in alfabeto:
            entry = entry.replace(i, '')
    if len(entry) == 3 or len(entry) == 7:
        entry += '.'
    elif len(entry) == 11:
        entry += '-'
    event.widget.insert(0, entry)

def formatar_telefone(event):
    if event.keysym.lower() == "backspace": return

    telefone = event.widget.get()
    event.widget.delete(0, tk.END)
    for i in telefone:
        if i in alfabeto:
            telefone = telefone.replace(i, '')
    if len(telefone) == 2:
        telefone = '(' + telefone+ ') '
    if len(telefone) == 10:
        telefone += '-'
    event.widget.insert(0, telefone)

def formatar_ano(event):
    if event.keysym.lower() == "backspace": return
    números = '0123456789'

    ano = event.widget.get()
    event.widget.delete(0, tk.END)
    for i in ano:
        if i not in números:
            ano = ano.replace(i, '')
    event.widget.insert(0, ano
                        )
def limpar(entry_list, erro, sucesso, tipo=0):
    for i in entry_list:
        i.delete(0, tk.END)

    tipo = -1
    erro.config(text='', bootstyle='danger')
    sucesso.config(text='', bootstyle='success')

def salvar_livros(mostrar_mensagem=False):
    livros_filtrados = []

    for i in catálogo:
        livro_filtro = i
        if livro_filtro['status'][0]:
            data_inteira = []
            data = str(i['status'][1]).split('-')
            for e in data:
                data_inteira.append(int(e))
            data_formatada = date(*data_inteira)
            hoje = date.today()
            intervalo = hoje - data_formatada
            if intervalo.days > 14:
                livro_filtro['multa'] = (intervalo.days - 14) * 2
        livro_filtro['status'][1] = str(livro_filtro['status'][1])
        livros_filtrados.append(livro_filtro)

    with open(DADOSLIVROS, 'w', encoding='utf-8') as arquivo:
        json.dump(livros_filtrados, arquivo, ensure_ascii=False, indent=4)

    if mostrar_mensagem:
        mensagem = messagebox.showinfo('Salvando', 'Dados salvos com SUCESSO!')

def salvar_usuários():
    with open(DADOSUSUÁRIOS, 'w', encoding='utf-8') as arquivo:
        json.dump(usuários, arquivo, ensure_ascii=False, indent=4)

def destruir(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def importar_livros():
    livros = []
    multa = 2

    with open(DADOSLIVROS, 'r', encoding='utf-8') as arquivo:
        try:
            livros = json.load(arquivo)
        except Exception:
            pass

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

def importar_usuários():
    usuários = []

    with open(DADOSUSUÁRIOS, 'r', encoding='utf-8') as arquivo:
        try:
            usuários = json.load(arquivo)
        except Exception:
            pass

    return usuários

def deletar():
    pass

def atualizar():
    pass

def cadastrar_usuário(entry_list, radio, erro, sucesso):
    sucesso.config(text='')
    cadastro = {}
    tipo = radio.get()
    usuário = entry_list[0]
    cpf = entry_list[1]
    senha = entry_list[2]
    confirmar_senha = entry_list[3]
    telefone = entry_list[4]

    nomes_valores = ['Nome', 'CPF', 'Senha', 'Telefone']

    if tipo == 0:
        erro.config(text='Um tipo(Admin ou Usuário) precisa ser selecionado', bootstyle='inverse-danger')
        return
    
    for i in usuários:
        if i['cpf'].strip() == cpf.get().strip():
            erro.config(text=f'CPF não disponível', bootstyle='inverse-danger')
            return

    if senha.get() != confirmar_senha.get():
        erro.config(text='As senhas estão diferentes', bootstyle='inverse-danger')
        return
    
    for índice, valor in enumerate(entry_list):
        if not valor.get():
            erro.config(text=f'{nomes_valores[índice]} precisa ser preenchido(a)', bootstyle='inverse-danger')
            return
    

    erro.config(bootstyle='danger')
    if tipo == 2:
        cadastro['tipo'] = True
    elif tipo == 1:
        cadastro['tipo'] = False
    cadastro['usuário'] = usuário.get().strip()
    cadastro['cpf'] = cpf.get()
    cadastro['senha'] = senha.get()
    cadastro['telefone'] = telefone.get()
    if not cadastro['tipo']:
        cadastro['livros'] = ''

    usuários.append(cadastro)

    with open(DADOSUSUÁRIOS, 'w', encoding='utf-8') as arquivo:
        json.dump(usuários, arquivo, ensure_ascii=False, indent=4)

    limpar(entry_list, erro, sucesso, tipo=tipo)

    erro.config(text='')
    sucesso.config(text='Cadastro Realizado com SUCESSO!', bootstyle='inverse-success')

def emprestar_livros(livros_para_emprestar, cpf_usuário):
    for i in livros_para_emprestar:
        for index, livro in enumerate(catálogo):
            if i == livro['código'] and not livro['status'][0]:
                catálogo[index]['status'][0] = True
                catálogo[index]['status'][1] = str(date.today())
    
    for índice, user in enumerate(usuários):
        if user['cpf'].strip() == cpf_usuário.strip():
            for i in livros_para_emprestar:
                usuários[índice]['livros'] += f"{i}; "
            break

    devolução = date.today() + timedelta(days=14)
    
    message = messagebox.showinfo('Aviso', f"Devolver ou renovar até {devolução}")

    salvar_usuários()
    salvar_livros()

def check_selection(btn, lista):
    if btn.instate(['selected']):
        lista.append(btn.cget('text')[8:20])

def print_all_selected(frame, emprestar):
    selecionados = []

    for widget in frame.winfo_children():
        if isinstance(widget, ttk.Frame):
            for button in widget.winfo_children():
                if isinstance(button, ttk.Checkbutton):
                    check_selection(button, selecionados)
    if emprestar:
        return selecionados

    else:
        for i in selecionados:
            for index, livro in enumerate(catálogo):
                if i == livro['código'] and livro['status'][0]:
                    catálogo[index]['status'][0] = False
                    catálogo[index]['status'][1] = '0'
                    catálogo[index]['multa'] = 0.0
            for index, usuário in enumerate(usuários):
                try:
                    if i in usuário['livros']:
                        usuários[index]['livros'] = usuários[index]['livros'].replace(f"{i}; ", '')
                except Exception:
                    continue

    salvar_livros()
    salvar_usuários()

def renovar_livros(frame):
    selecionados = []

    for widget in frame.winfo_children():
        if isinstance(widget, ttk.Frame):
            for button in widget.winfo_children():
                if isinstance(button, ttk.Checkbutton):
                    check_selection(button, selecionados)

    for i in selecionados:
        for index, livro in enumerate(catálogo):
            if i == livro['código']:
                catálogo[index]['status'][1] = str(date.today())
                catálogo[index]['multa'] = 0.0
                catálogo[index]['renovações'] += 1

    salvar_livros()
    salvar_usuários()

catálogo = importar_livros()
usuários = importar_usuários()