import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from utils.controle_dados import *
from utils.controle_de_widgets import *

class PáginaUsuário(tk.Toplevel):
    def __init__(self, controller, username, senha):
        tk.Toplevel.__init__(self)

        self.title('Catálogo')
        self.resizable(False, True)
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        x = (largura_tela - 700) // 2
        y = (altura_tela - (altura_tela // 1.2)) // 2
        self.geometry(f'{700}x{int(altura_tela // 1.2)}+{x}+{int(y)}')

        label_header = ttk.Label(self, text='Livros Pendentes', font=LARGEFONT)
        label_header.pack(pady=20)

        label_instructions = ttk.Label(self, text='Devolver ou renovar livros em 14 dias ou menos\nCaso o contrário, haverá multa', justify='center', font=SMALLFONT)
        label_instructions.pack(pady=10)

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

        códigos_livros_pendentes = []
        for i in usuários:
            if i['usuário'] == username:
                códigos_livros_pendentes = i['livros'].split('; ')
                break
        
        códigos_livros_pendentes.pop()
        print(códigos_livros_pendentes)

        livros_pendentes = []
        for código in códigos_livros_pendentes:
            for livro in catálogo:
                if livro['código'] == código:
                    livros_pendentes.append(livro)

        listar_itens(livros_pendentes, frame_interior, end='multa', tipo='livros_pendentes')