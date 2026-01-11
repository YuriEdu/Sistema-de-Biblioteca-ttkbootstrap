from datetime import date
from utils.controle_dados import *
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

LARGEFONT = ('URW Bookman', 35)
MEDIUMFONT = ('Veranda', 15)
SMALLFONT = ('Veranda', 10)

gêneros = []

with open(DADOSGÊNEROS, 'r') as arquivo:
    text = arquivo.read()
    gêneros = text.split(',')

subgêneros = []

with open(DADOSSUBGÊNEROS, 'r') as arquivo:
    text = arquivo.read()
    subgêneros = text.split(',')

class Cadastro(tk.Frame):
    id = '0000'

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text='Cadastrando Livro', font=LARGEFONT)
        label.pack(pady=20, padx=5)

        frame_other = tk.Frame(master=self)
        frame_other.pack(pady=40)

        label_title = ttk.Label(frame_other, text='Título:')
        label_author = ttk.Label(frame_other, text='Autor:')
        label_ano = ttk.Label(frame_other, text='Ano de Publicação:')
        label_genre = ttk.Label(frame_other, text='Gênero:')
        label_subgenre = ttk.Label(frame_other, text='Subgênero:')
        entry_title = ttk.Entry(frame_other, width=25)
        entry_author = ttk.Entry(frame_other, width=25)
        entry_ano = ttk.Entry(frame_other, width=25)

        gênero = tk.StringVar()
        subgênero = tk.StringVar()

        cb_genre = ttk.Combobox(frame_other, text='Selecione um Gênero', width=23, style='info.TCombobox', textvariable=gênero)
        cb_subgenre = ttk.Combobox(frame_other, text='Selecione um Subgênero', width=23, style='info.TCombobox', textvariable=subgênero)

        cb_genre['values'] = gêneros

        cb_subgenre['values'] = subgêneros
            
        btn_submit = ttk.Button(frame_other, text='Cadastrar', command= lambda : self.cadastrar(entry_title, entry_author, gênero, subgênero, entry_ano, label_resultado))
        label_resultado = ttk.Label(self)
        btn_voltar = ttk.Button(self, text='Voltar', command= lambda : [controller.página_inicial(), 
                                                                        label_resultado.config(text='')])

        label_title.grid(column=0, row=2, sticky='e')
        label_author.grid(column=0, row=3, sticky='e')
        label_ano.grid(column=0, row=4, sticky='w')
        label_genre.grid(column=0, row=5, sticky='e')
        label_subgenre.grid(column=0, row=6, sticky='e')
        entry_title.grid(column=1, row=2, sticky='e', padx=5, pady=5)
        entry_author.grid(column=1, row=3, sticky='e', padx=5, pady=5)
        entry_ano.grid(column=1, row=4, sticky='e', padx=5, pady=5)
        cb_genre.grid(column=1, row=5, sticky='e', padx=5, pady=5)
        cb_subgenre.grid(column=1, row=6, sticky='e', padx=5, pady=5)
        btn_submit.grid(column=0, row=7, sticky='s', columnspan=5, pady=10)
        label_resultado.pack()
        btn_voltar.pack(side='left', padx=5, pady=5)

    def cadastrar(self, título, autor, gênero, subgênero, publicação, label):
        if not título.get():
            label['text'] = 'O TÍTULO precisa ser preenchido'
            return
        else:
            for i in catálogo:
                if título.get().lower() == i['título'].lower():
                    label['text'] = 'Este livro já foi registrado'
                    return
        if not autor.get():
            label['text'] = 'O AUTOR precisa ser preenchido'
            return
        if not publicação.get():
            label['text'] = 'O ANO DE PUBLICAÇÃO precisa ser preenchido'
            return
        if not gênero.get():
            label['text'] = 'O GÊNERO precisa ser preenchido'
            return
        if not subgênero.get():
            label['text'] = 'O SUBGÊNERO precisa ser preenchido'
            return
        cadastro = {}
        código = str(date.today()).replace('-', '')
        if len(catálogo) > 0:
            if catálogo[len(catálogo) - 1]['data de catálogo'] == f'{date.today()}':
                Cadastro.id = f'{int(catálogo[len(catálogo) - 1]['código'][9:]) + 1:04}'
                código += Cadastro.id
                Cadastro.id = f'{int(Cadastro.id) + 1:04}'
            else:
                código += Cadastro.id
                Cadastro.id = f'{int(Cadastro.id) + 1:04}'
        else:
            código += Cadastro.id

        cadastro['código'] = código
        cadastro['título'] = título.get()
        cadastro['autor'] = autor.get()
        cadastro['gênero'] = gênero.get()
        cadastro['subgênero'] = subgênero.get()
        cadastro['status'] = [False, 0]
        cadastro['multa'] = 0.0
        cadastro['ano de publicação'] = publicação.get()
        cadastro['data de catálogo'] = str(date.today())
        catálogo.append(cadastro)

        if subgênero.get() not in subgêneros:
            subgêneros.append(subgênero.get())

        if gênero.get() not in gêneros:
            gêneros.append(gênero.get())

        título.delete(0, END)
        autor.delete(0, END)
        publicação.delete(0, END)
        gênero.set('')
        subgênero.set('')

        label.config(text=f'{cadastro['título']} de {cadastro["autor"]} cadastrado com SUCESSO!')

        salvar_livros()
        print(catálogo)