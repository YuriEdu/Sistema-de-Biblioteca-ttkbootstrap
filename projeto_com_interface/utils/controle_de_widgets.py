import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from utils.controle_dados import *

def ativar_botões_de_menu(button_list):
    for i in button_list:
        i.config(state=NORMAL)
        i.state(('!selected',))

def gerar_texto(dict, tipo, end='status'):
    text = ''
    
    if tipo == 'livro':
        for key, value in dict.items():
            if key == 'multa':
                text += f'\n{key.capitalize()}: R${value:5.2f}'
            elif key == 'status':
                text += f"{key.capitalize()}: {'EMPRESTADO' if value[0] else 'DISPONÍVEL'}"
            elif key == 'código':
                text += f'{key.capitalize()}: {value:<55}\n'
            elif key == 'gênero':
                continue
            elif key == 'subgênero':
                continue
            else:
                text += f'{key.capitalize()}: {value}\n'
            if key == end:
                break
    
    if tipo == 'usuário':
        for key, value in dict.items():
            if key == 'tipo' or key == 'senha':
                continue
            elif key == 'cpf':
                text += f'{key.upper()}: {value:<60}\n'
            elif key == 'telefone':
                text += f'{key.capitalize()}: {value}'
                break
            else:
                text += f'{key.capitalize()}: {value}\n'
    
    if tipo == 'livros_pendentes':
        for key, value in dict.items():
            if key == 'multa':
                text += f'\n{key.capitalize()}: R${value:5.2f}'
            elif key == 'status':
                text += f'Empréstimo: {str(value[1])}'
            elif key == 'código':
                text += f'{key.capitalize()}: {value:<55}\n'
            elif key == 'gênero':
                continue
            elif key == 'subgênero':
                continue
            else:
                text += f'{key.capitalize()}: {value}\n'
            if key == end:
                break
    return text

def criar_buttons(dict, janela, end, tipo):
    text = gerar_texto(dict, tipo, end)
    btn = ttk.Button(janela, text=text)
    return btn

def listar_itens(lista, janela, end='status', tipo='livro'):
    if sistema == 'Windows':
        pad_x = 10.7
    if sistema == 'Linux':
        pad_x = 12
    if len(lista) % 2 == 0:
        for a in range(0, len(lista)):
            if a % 2 == 0:
                frame = ttk.Frame(janela)
                frame.pack(fill='y', pady=5, padx=int(janela.master.cget('width')) // pad_x)

                btn_1 = criar_buttons(lista[a], frame, end, tipo)
                btn_1.pack(side='left', padx=5)

                btn_2 = criar_buttons(lista[a + 1], frame, end, tipo)
                btn_2.pack(side='right', padx=5)
    else:
        for a in range(0, len(lista)):
            if a % 2 == 0 and a < len(lista) - 1:
                frame = ttk.Frame(janela)
                frame.pack(fill='y', pady=5, padx=int(janela.master.cget('width')) // pad_x)

                btn_1 = criar_buttons(lista[a], frame, end, tipo)
                btn_1.pack(side='left', padx=5)

                btn_2 = criar_buttons(lista[a + 1], frame, end, tipo)
                btn_2.pack(side='right', padx=5)

        frame = ttk.Frame(janela)
        frame.pack(side='left', pady=5, padx=int(janela.master.cget('width')) // pad_x)

        btn_last = criar_buttons(lista[len(lista) - 1], frame, end, tipo)
        btn_last.pack(side='left', padx=5)
