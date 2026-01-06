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

    def criar_checkbuttons(self, dict, janela, end):
        text = gerar_texto(dict, end)
        btn = ttk.Checkbutton(janela, text=text, bootstyle='info-outline-toolbutton')
        return btn
    
    def check_selection(self, btn, lista):
        if btn.instate(['selected']):
            print(btn.cget('text'))
            print(btn.cget('text')[8:20])
            lista.append(btn.cget('text')[8:20])

    def listar_itens_com_checkbuttons(self, lista, janela, end='status'):
        pad_x = 13
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

    def emprestar(self, lista, janela, label, button_list):
        destruir(janela)

        livros_disponíveis = []

        for i in lista:
            if not i['status'][0]:
                livros_disponíveis.append(i)
        self.listar_itens_com_checkbuttons(livros_disponíveis, janela)
        label.config(text='Empréstimo')

        frame_voltar = ttk.Frame(janela.master)
        frame_voltar.pack(side='bottom', fill='x')

        btn_voltar = ttk.Button(frame_voltar, text='Voltar', command=lambda : [destruir(janela), 
                                                                            listar_itens(lista, janela), 
                                                                            frame_voltar.destroy(),
                                                                            label.config(text='Catálogo'),
                                                                            ativar_botões_de_menu(button_list)])
        btn_voltar.pack(side='left', pady=5, padx=5)

        btn_finalizar = ttk.Button(frame_voltar, text='Finalizar',
                                   command=lambda : [self.print_all_selected(janela, True), self.emprestar(catálogo, janela, label, button_list), frame_voltar.destroy()])
        
        btn_finalizar.pack(side='right', pady=5, padx=5)

    def devolver(self, lista, janela, label, button_list):
        destruir(janela)
        
        livros_emprestados = []

        for i in lista:
            if i['status'][0]:
                livros_emprestados.append(i)
        self.listar_itens_com_checkbuttons(livros_emprestados, janela, end='multa')
        label.config(text='Devolução')

        frame_voltar = ttk.Frame(janela.master)
        frame_voltar.pack(side='bottom', fill='x')
        
        btn_voltar = ttk.Button(frame_voltar, text='Voltar', command=lambda : [destruir(janela), 
                                                                            listar_itens(lista, janela), 
                                                                            frame_voltar.destroy(),
                                                                            label.config(text='Catálogo'),
                                                                            ativar_botões_de_menu(button_list)])
        btn_voltar.pack(side='left', pady=5, padx=5)

        btn_finalizar = ttk.Button(frame_voltar, text='Finalizar',
                                   command=lambda : [self.print_all_selected(janela, False), self.devolver(catálogo, janela, label, button_list), frame_voltar.destroy()])
        
        btn_finalizar.pack(side='right', pady=5, padx=5)

    def print_all_selected(self, frame, tipo):
        selecionados = []

        for widget in frame.winfo_children():
            if isinstance(widget, ttk.Frame):
                for button in widget.winfo_children():
                    if isinstance(button, ttk.Checkbutton):
                        self.check_selection(button, selecionados)
        if tipo:
            for i in selecionados:
                for index, livro in enumerate(catálogo):
                    if i == livro['código'] and not livro['status'][0]:
                        catálogo[index]['status'][0] = True
                        catálogo[index]['status'][1] = str(date.today())
                        print(catálogo[index]['status'][1])

        else:
            for i in selecionados:
                for index, livro in enumerate(catálogo):
                    if i == livro['código'] and livro['status'][0]:
                        catálogo[index]['status'][0] = False
                        catálogo[index]['status'][1] = '0'
                        catálogo[index]['multa'] = 0.0
                        print(catálogo[index]['status'][1])

        print(catálogo)
        salvar(catálogo)