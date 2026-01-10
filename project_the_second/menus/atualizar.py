from datetime import date
from utils.controle_dados import *
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from utils.controle_de_widgets import *

gêneros = []

with open(DADOSGÊNEROS, 'r') as arquivo:
    text = arquivo.read()
    gêneros = text.split(',')

subgêneros = []

with open(DADOSSUBGÊNEROS, 'r') as arquivo:
    text = arquivo.read()
    subgêneros = text.split(',')

class Atualizar(tk.Toplevel):
    def __init__(self, controller):
        tk.Toplevel.__init__(self)

        self.title('Atualizar')
        self.resizable(False, True)
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        x = (largura_tela - 700) // 2
        y = (altura_tela - (altura_tela // 1.2)) // 2
        self.geometry(f'{700}x{int(altura_tela // 1.2)}+{x}+{int(y)}')

        label_header = ttk.Label(self, text='Atualizar', font=LARGEFONT)
        label_header.pack(pady=20)

        frame = ttk.Frame(self)
        frame.pack()

        canvas = tk.Canvas(self)
        canvas.pack(side='left', fill='both', expand=True, pady=5, padx=16)

        scrollbar = ttk.Scrollbar(self, orient="vertical")
        scrollbar.pack(side="right", fill="y", padx=5, pady=5)

        canvas.config(yscrollcommand=scrollbar.set)

        scrollbar.config(command=canvas.yview)

        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        frame_interior = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame_interior, anchor='nw')
        
        self.listar_update_itens(catálogo, frame_interior)
    
    def criar_update_buttons(self, dict, janela, end):
        text = gerar_texto(dict, end=end, tipo='livro')
        btn = ttk.Button(janela, text=text, command=lambda : self.popup_atualizar(btn['text']))
        return btn
    
    def listar_update_itens(self, lista, janela, end='status'):
        pad_x = 13.6
        if len(lista) % 2 == 0:
            for a in range(0, len(lista)):
                if a % 2 == 0:
                    frame = ttk.Frame(janela)
                    frame.pack(fill='y', pady=5, padx=int(janela.master.cget('width')) // pad_x)

                    btn_1 = self.criar_update_buttons(lista[a], frame, end)
                    btn_1.pack(side='left', padx=5)

                    btn_2 = self.criar_update_buttons(lista[a + 1], frame, end)
                    btn_2.pack(side='right', padx=5)
        else:
            for a in range(0, len(lista)):
                if a % 2 == 0 and a < len(lista) - 1:
                    frame = ttk.Frame(janela)
                    frame.pack(fill='y', pady=5, padx=int(janela.master.cget('width')) // pad_x)

                    btn_1 = self.criar_update_buttons(lista[a], frame, end)
                    btn_1.pack(side='left', padx=5)

                    btn_2 = self.criar_update_buttons(lista[a + 1], frame, end)
                    btn_2.pack(side='right', padx=5)

            frame = ttk.Frame(janela)
            frame.pack(side='left', pady=5, padx=int(janela.master.cget('width')) // pad_x)

            btn_last = self.criar_update_buttons(lista[len(lista) - 1], frame, end)
            btn_last.pack(side='left', padx=5)

    def popup_atualizar(self, btn_text):

        btn_código = btn_text[8:20]

        popup = tk.Toplevel()
        popup.title('Atualizar Livro')

        label = ttk.Label(popup, text='Atualizar Livro', font=LARGEFONT)
        label.pack(padx=60, pady=20)

        frame = tk.Frame(popup)
        frame.pack()

        label_título = ttk.Label(frame, text='Título:')
        label_autor = ttk.Label(frame, text='Autor:')
        label_ano = ttk.Label(frame, text='Ano de Publicação:')
        label_gênero = ttk.Label(frame, text='Gênero:')
        label_subgênero = ttk.Label(frame, text='Subgênero:')

        entry_título = ttk.Entry(frame, width=25)
        entry_autor = ttk.Entry(frame, width=25)
        entry_ano = ttk.Entry(frame, width=25)

        gênero = tk.StringVar()
        subgênero = tk.StringVar()

        cb_genre = ttk.Combobox(frame, text='Selecione um Gênero', width=23, style='info.TCombobox', textvariable=gênero)
        cb_subgenre = ttk.Combobox(frame, text='Selecione um Subgênero', width=23, style='info.TCombobox', textvariable=subgênero)

        cb_genre['values'] = gêneros

        cb_subgenre['values'] = subgêneros

        for índice, livro in enumerate(catálogo):
            if livro['código'] == btn_código:
                entry_título.insert(0, livro['título'])
                entry_autor.insert(0, livro['autor'])
                entry_ano.insert(0, livro['ano de publicação'])
                cb_genre.insert(0, livro['gênero'])
                cb_subgenre.insert(0, livro['subgênero'])
                break

        lbl_erro = ttk.Label(popup, text='', foreground='red')
        lbl_sucesso = ttk.Label(popup, text='', foreground='blue')

        entry_list = [entry_título, entry_autor, entry_ano, gênero, subgênero]

        frame_buttons = ttk.Frame(popup)
        frame_buttons.pack(pady=20)

        btn_atualizar = ttk.Button(frame_buttons, text='Atualizar', command=lambda : self.atualizar_livro(entry_list, btn_código))

        label_título.grid(column=0, row=0, sticky='e')
        label_autor.grid(column=0, row=1, sticky='e')
        label_ano.grid(column=0, row=2, sticky='w')
        label_gênero.grid(column=0, row=3, sticky='e')
        label_subgênero.grid(column=0, row=4, sticky='e')
        entry_título.grid(column=1,row=0, padx=5, pady=5)
        entry_autor.grid(column=1,row=1, padx=5, pady=5)
        entry_ano.grid(column=1, row=2, padx=5, pady=5)
        cb_genre.grid(column=1, row=3, sticky='e', padx=5, pady=5)
        cb_subgenre.grid(column=1, row=4, sticky='e', padx=5, pady=5)

        lbl_erro.pack()
        lbl_sucesso.pack()
        btn_atualizar.pack(padx=5)

    def atualizar_livro(self, entry_list, código):
        for índice, livro in enumerate(catálogo):
            if livro['código'] == código:
                livro['título'] = entry_list[0].get()
                livro['autor'] = entry_list[1].get()
                livro['ano de publicação'] = entry_list[2].get()
                livro['gênero'] = entry_list[3].get()
                livro['subgênero'] = entry_list[4].get()
                break

        salvar_livros()