import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from utils.controle_dados import *
from utils.controle_de_widgets import *

class PáginaUsuário(tk.Toplevel):
    def __init__(self, controller, username, senha):
        tk.Toplevel.__init__(self)

        self.title('Livros Pendentes')
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

        label_header = ttk.Label(self, text='Livros Pendentes', font=LARGEFONT)
        label_header.pack(pady=20)

        label_instructions = ttk.Label(self, text='Devolver ou renovar livros em 14 dias ou menos\nCaso o contrário, haverá multa', justify='center', font=SMALLFONT)
        label_instructions.pack(pady=10)

        frame = ttk.Frame(self)
        frame.pack(fill='x')

        buttons = []

        btn_renovar = ttk.Checkbutton(frame, text='Renovar', bootstyle='primary-outline-toolbutton', 
                                        command=lambda : [self.renovar(livros_pendentes, frame_interior, label_header, buttons), 
                                                          btn_renovar.config(state=DISABLED)])
        
        buttons.append(btn_renovar)

        btn_renovar.pack(side='bottom')

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

    def criar_checkbuttons(self, dict, janela, end):
        text = gerar_texto(dict, tipo='livro', end=end)
        btn = ttk.Checkbutton(janela, text=text, bootstyle='info-outline-toolbutton')
        return btn

    def listar_itens_com_checkbuttons(self, lista, janela, end='status'):
        if sistema == 'Windows':
            pad_x = 10
        if sistema == 'Linux':
            pad_x = 11.3
        if len(lista) % 2 == 0:
            for a in range(0, len(lista)):
                if a % 2 == 0:
                    frame = ttk.Frame(janela)
                    frame.pack(fill='y', pady=5, padx=int(janela.master.cget('width')) // pad_x)

                    btn_1 = self.criar_checkbuttons(lista[a], frame, end)
                    btn_1.pack(side='left', padx=5)

                    btn_2 = self.criar_checkbuttons(lista[a + 1], frame, end)
                    btn_2.pack(side='right', padx=5)
        else:
            for a in range(0, len(lista)):
                if a % 2 == 0 and a < len(lista) - 1:
                    frame = ttk.Frame(janela)
                    frame.pack(fill='y', pady=5, padx=int(janela.master.cget('width')) // pad_x)

                    btn_1 = self.criar_checkbuttons(lista[a], frame, end)
                    btn_1.pack(side='left', padx=5)

                    btn_2 = self.criar_checkbuttons(lista[a + 1], frame, end)
                    btn_2.pack(side='right', padx=5)

            frame = ttk.Frame(janela)
            frame.pack(side='left', pady=5, padx=int(janela.master.cget('width')) // pad_x)

            btn_last = self.criar_checkbuttons(lista[len(lista) - 1], frame, end)
            btn_last.pack(side='left', padx=5)

    def renovar(self, lista, janela, label, button_list):
        destruir(janela)

        livros_renováveis = []

        for i in lista:
            if float(i['multa']) == 0.0:
                livros_renováveis.append(i)
        self.listar_itens_com_checkbuttons(livros_renováveis, janela, end='multa')
        label.config(text='Renovar')

        frame_voltar = ttk.Frame(janela.master)
        frame_voltar.pack(side='bottom', fill='x')

        btn_voltar = ttk.Button(frame_voltar, text='Voltar', command=lambda : [destruir(janela), 
                                                                            listar_itens(lista, janela, end='multa', tipo='livros_pendentes'),
                                                                            frame_voltar.destroy(),
                                                                            label.config(text='Livros Pendentes'),
                                                                            ativar_botões_de_menu(button_list)])
        btn_voltar.pack(side='left', pady=5, padx=5)

#        btn_finalizar = ttk.Button(frame_voltar, text='Finalizar',
#                                   command=lambda : [self.print_all_selected(janela, True), self.emprestar(catálogo, janela, label, button_list), frame_voltar.destroy()])
        
        btn_finalizar = ttk.Button(frame_voltar, text='Finalizar',
                                   command=lambda : [renovar_livros(janela), 
                                                     destruir(janela), 
                                                     listar_itens(lista, janela, end='multa', tipo='livros_pendentes'),
                                                     frame_voltar.destroy(),
                                                     label.config(text='Livros Pendentes'),
                                                     ativar_botões_de_menu(button_list)])

        btn_finalizar.pack(side='right', pady=5, padx=5)
    
    def renovar_livro(self, janela, lista, label, button_list):
        pass