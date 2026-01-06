from utils.controle_dados import *
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from utils.controle_de_widgets import *

class Listar(tk.Toplevel):
    def __init__(self, controller):
        tk.Toplevel.__init__(self)

        self.title('Catálogo')
        self.resizable(False, True)
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        x = (largura_tela - 700) // 2
        y = (altura_tela - (altura_tela // 1.2)) // 2
        self.geometry(f'{700}x{int(altura_tela // 1.2)}+{x}+{int(y)}')

        label_header = ttk.Label(self, text='Catálogo', font=LARGEFONT)
        label_header.pack(pady=20)

        frame = ttk.Frame(self)
        frame.pack()

        buttons = []

        btn_emprestar = ttk.Checkbutton(frame, text='Emprestar', bootstyle='primary-outline-toolbutton', 
                                        command=lambda : [self.emprestar(catálogo, frame_interior, label_header, buttons), 
                                                          btn_emprestar.config(state=DISABLED),
                                                          btn_devolver.config(state=DISABLED)])

        btn_devolver = ttk.Checkbutton(frame, text='Devolver', bootstyle='primary-outline-toolbutton', 
                                       command=lambda : [self.devolver(catálogo, frame_interior, label_header, buttons), 
                                                          btn_emprestar.config(state=DISABLED),
                                                          btn_devolver.config(state=DISABLED)])
        
        buttons.append(btn_emprestar)
        buttons.append(btn_devolver)

        btn_emprestar.pack(side='left', padx=5)
        btn_devolver.pack(side='right', padx=5)

        canvas = tk.Canvas(self)
        canvas.pack(side='left', fill='both', expand=True, pady=5, padx=16)

        scrollbar = ttk.Scrollbar(self, orient="vertical")
        scrollbar.pack(side="right", fill="y", padx=5, pady=5)

        canvas.config(yscrollcommand=scrollbar.set)

        scrollbar.config(command=canvas.yview)

        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        frame_interior = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame_interior, anchor='nw')
        
        listar_itens(catálogo, frame_interior)

    def emprestar(self, lista, janela, label, button_list):
        destruir(janela)

        livros_disponíveis = []

        for i in lista:
            if not i['status'][0]:
                livros_disponíveis.append(i)
        listar_itens_com_checkbuttons(livros_disponíveis, janela)
        label.config(text='Empréstimo')

        frame_voltar = ttk.Frame(janela.master)
        frame_voltar.pack(side='bottom', fill='x')

        btn_voltar = ttk.Button(frame_voltar, text='Voltar', command=lambda : [destruir(janela), 
                                                                            listar_itens(lista, janela), 
                                                                            frame_voltar.destroy(),
                                                                            label.config(text='Catálogo'),
                                                                            ativar_botões_de_menu(button_list)])
        btn_voltar.pack(side='left', pady=5, padx=5)

        btn_finalizar = ttk.Button(frame_voltar, text='Finalizar')
        btn_finalizar.pack(side='right', pady=5, padx=5)

        '''
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
        '''

    def devolver(self, lista, janela, label, button_list):
        destruir(janela)
        
        livros_emprestados = []

        for i in lista:
            if i['status'][0]:
                livros_emprestados.append(i)
        listar_itens_com_checkbuttons(livros_emprestados, janela, end='multa')
        label.config(text='Devolução')

        frame_voltar = ttk.Frame(janela.master)
        frame_voltar.pack(side='bottom', fill='x')
        
        btn_voltar = ttk.Button(frame_voltar, text='Voltar', command=lambda : [destruir(janela), 
                                                                            listar_itens(lista, janela), 
                                                                            frame_voltar.destroy(),
                                                                            label.config(text='Catálogo'),
                                                                            ativar_botões_de_menu(button_list)])
        btn_voltar.pack(side='left', pady=5, padx=5)

        btn_finalizar = ttk.Button(frame_voltar, text='Finalizar')
        btn_finalizar.pack(side='right', pady=5, padx=5)