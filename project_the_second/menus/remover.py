from datetime import date
from utils.controle_dados import *
from utils.controle_de_widgets import *
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Remover(tk.Toplevel):
    def __init__(self, controller):
        tk.Toplevel.__init__(self)

        def _on_mousewheel(event, canvas):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        self.title('Remover')
        self.resizable(False, True)
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        if sistema == 'Windows':
            x = (largura_tela - 900) // 2
            y = (altura_tela - (altura_tela // 1.2)) // 2
            self.geometry(f'{900}x{int(altura_tela // 1.2)}+{x}+{int(y)}')

        if sistema == 'Linux':
            x = (largura_tela - 800) // 2
            y = altura_tela
            self.geometry(f'{800}x{altura_tela - (altura_tela // 5)}+{x}+{int(y)}')

        label_header = ttk.Label(self, text='Remover', font=LARGEFONT)
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

        self.bind("<MouseWheel>", lambda event: _on_mousewheel(event, canvas))
        
        self.listar_remover_itens(catálogo, frame_interior)

    def criar_remover_buttons(self, dict, janela, end):
        text = gerar_texto(dict, end=end, tipo='livro')
        btn = ttk.Button(janela, text=text, command=lambda : self.garantir_certeza(btn['text'], janela.master))
        mensagem = tk.Message()
        return btn
    
    def listar_remover_itens(self, lista, janela, end='status'):
        if sistema == 'Windows':
            pad_x = 10.7
        if sistema == 'Linux':
            pad_x = 12
        if len(lista) % 2 == 0:
            for a in range(0, len(lista)):
                if a % 2 == 0:
                    frame = ttk.Frame(janela)
                    frame.pack(fill='y', pady=5, padx=int(janela.master.cget('width')) // pad_x)

                    btn_1 = self.criar_remover_buttons(lista[a], frame, end)
                    btn_1.pack(side='left', padx=5)

                    btn_2 = self.criar_remover_buttons(lista[a + 1], frame, end)
                    btn_2.pack(side='right', padx=5)
        else:
            for a in range(0, len(lista)):
                if a % 2 == 0 and a < len(lista) - 1:
                    frame = ttk.Frame(janela)
                    frame.pack(fill='y', pady=5, padx=int(janela.master.cget('width')) // pad_x)

                    btn_1 = self.criar_remover_buttons(lista[a], frame, end)
                    btn_1.pack(side='left', padx=5)

                    btn_2 = self.criar_remover_buttons(lista[a + 1], frame, end)
                    btn_2.pack(side='right', padx=5)

            frame = ttk.Frame(janela)
            frame.pack(side='left', pady=5, padx=int(janela.master.cget('width')) // pad_x)

            btn_last = self.criar_remover_buttons(lista[len(lista) - 1], frame, end)
            btn_last.pack(side='left', padx=5)

    def garantir_certeza(self, btn_text, janela):
        separador = 'Autor: '

        título = btn_text[36:].split(separador)[0].replace('Título: ', '').replace('\n', '').strip()

        for i in catálogo:
            if i['título'].lower() == título.lower():
                autor = i['autor']
                break
        mensagem = messagebox.askokcancel('Remover Livro', f'Tem certeza de que deseja remover {título}, de {autor}?', parent=self)
        if mensagem:
            for index, livro in enumerate(catálogo):
                if livro['título'].lower() == título:
                    del catálogo[index]

                    destruir(janela)
                    salvar_livros()
                    self.listar_remover_itens(catálogo, janela)
                    break
