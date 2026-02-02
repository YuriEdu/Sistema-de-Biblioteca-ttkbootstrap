from utils.controle_dados import *
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from menus.página_usuário import PáginaUsuário
from menus.cadastro import Cadastro
from menus.listar import Listar
from menus.atualizar import Atualizar
from menus.remover import Remover

class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        def enter_pressionado(event):
            self.validar_login(parent, entry_username, entry_senha, controller, lbl_erro)

        label = ttk.Label(self, text='Login', font=LARGEFONT)
        label.pack(pady=60, padx=150)

        lbl_erro = ttk.Label(self, text='', bootstyle='danger')
        lbl_erro.pack()

        frame_other = ttk.Frame(self)
        frame_other.pack(pady=10)

        label_username = ttk.Label(frame_other, text='Usuário:')
        label_senha = ttk.Label(frame_other, text='Senha:')
        entry_username = ttk.Entry(frame_other, width=25, font=SMALLFONT)
        entry_senha = ttk.Entry(frame_other, width=25, show='*', font=SMALLFONT)

        frame_buttons = ttk.Frame(self)
        frame_buttons.pack(pady=20)

        btn_login = ttk.Button(frame_buttons, text='Login', width=10,
                               command=lambda : self.validar_login(parent, entry_username, entry_senha, controller, lbl_erro))
        btn_sair = ttk.Button(frame_buttons, text='Sair', width=10,
                               command=lambda : self.master.master.destroy())
        
        self.master.master.bind('<Return>', enter_pressionado, salvar_livros())

        label_username.grid(column=0, row=2, sticky='e')
        label_senha.grid(column=0, row=3, sticky='e')
        entry_username.grid(column=1, row=2, sticky='e', padx=5, pady=5)
        entry_senha.grid(column=1, row=3, sticky='e', padx=5, pady=5)
        btn_login.grid(column=0, row=0, sticky='s', columnspan=5, pady=5)
        btn_sair.grid(column=0, row=1)

    def validar_login(self, parent, entry_username, entry_senha, cont, label):
        usuário_encontrado = False
        usuário = entry_username.get()
        senha = entry_senha.get()
        for i in usuários:
            if usuário == i['usuário']:
                usuário_encontrado = True
                if senha == i['senha']:
                    if i['tipo']:
                        cont.show_frame(PáginaInicial)
                        entry_username.delete(0, END)
                        entry_senha.delete(0, END)
                        label.config(text='')
                        break
                    else:
                        PáginaUsuário(cont, usuário, senha)
                        entry_username.delete(0, END)
                        entry_senha.delete(0, END)
                        label.config(text='')
                    break
                else:
                    label.config(text='Senha incorreta')
                    break
        if not usuário_encontrado:
            label.config(text='Usuário não cadastrado')

class PáginaInicial(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text='Página Inicial', font=LARGEFONT)
        label.grid(row=0, column=4, padx=30, pady=40)

        button1 = ttk.Button(self, text='Cadastrar livro', width=20,
                             command=lambda : controller.show_frame(Cadastro))
        button1.grid(row=1, column=1, padx=10, pady=5)

        button2 = ttk.Button(self, text='Catálogo', width=20,
                             command=lambda : Listar(controller))
        button2.grid(row=2, column=1, padx=10, pady=5)

        button4 = ttk.Button(self, text='Atualizar livro', width=20,
                             command=lambda : Atualizar(controller))
        button4.grid(row=3, column=1, padx=10, pady=5)

        button3 = ttk.Button(self, text='Remover livro', width=20,
                             command=lambda : Remover(controller))
        button3.grid(row=4, column=1, padx=10, pady=5)

        button7 = ttk.Button(self, text='Cadastrar usuário', width=20,
                             command=lambda : controller.show_frame(UsuárioCadastro))
        button7.grid(row=5, column=1, padx=10, pady=5)

        button5 = ttk.Button(self, text='Salvar', width=20,
                             command=lambda : salvar_livros(mostrar_mensagem=True))
        button5.grid(row=6, column=1, padx=10, pady=5)

        button6 = ttk.Button(self, text='Voltar', width=20,
                             command=lambda : controller.show_frame(Login))
        button6.grid(row=7, column=1, padx=10, pady=5)

class UsuárioCadastro(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        vcmd = self.register(validar_cpf)

        label = ttk.Label(self, text='Cadastrar Usuário', font=LARGEFONT)
        label.pack(pady=20)

        frame_radio = ttk.Frame(self)
        frame_radio.pack(pady=20)

        frame_other = ttk.Frame(self)
        frame_other.pack()

        tipo_usuário = tk.IntVar(self, 0)

        lbl_erro = ttk.Label(self, text='', bootstyle='danger')
        lbl_sucesso = ttk.Label(self, text='', bootstyle='success')
        radio_usuário = ttk.Radiobutton(frame_radio, text='Usuário', variable=tipo_usuário, value=1)
        radio_admin = ttk.Radiobutton(frame_radio, text='Admin', variable=tipo_usuário, value=2)
        label_usuário = ttk.Label(frame_other, text='Usuário:')
        label_cpf = ttk.Label(frame_other, text='   CPF:')
        label_senha = ttk.Label(frame_other, text='Senha:')
        label_confirmar_senha = ttk.Label(frame_other, text='Confirmar Senha:')
        label_telefone = ttk.Label(frame_other, text='Telefone:')

        entry_usuário = ttk.Entry(frame_other, width=25, font=SMALLFONT)
        entry_cpf = ttk.Entry(frame_other, width=25, validate='key', validatecommand=(vcmd, '%P'), font=SMALLFONT)
        entry_cpf.bind("<KeyRelease>", formatar_cpf)
        entry_senha = ttk.Entry(frame_other, width=25, show='*', font=SMALLFONT)
        entry_confirmar_senha = ttk.Entry(frame_other, width=25, show='*', font=SMALLFONT)

        vcmd = self.register(validar_tel)

        entry_telefone = ttk.Entry(frame_other, width=25, validate='key', validatecommand=(vcmd, '%P'), font=SMALLFONT)
        entry_telefone.bind("<KeyRelease>", formatar_telefone)

        entry_list = [entry_usuário, entry_cpf, entry_senha, entry_confirmar_senha, entry_telefone]
        
        frame_buttons = ttk.Frame(self)
        frame_buttons.pack(pady=10)

        btn_limpar = ttk.Button(frame_buttons, text='Limpar', 
                                command=lambda : limpar(entry_list, lbl_erro, lbl_sucesso, tipo=tipo_usuário))
        btn_cadastrar = ttk.Button(frame_buttons, text='Cadastrar', 
                                   command=lambda : cadastrar_usuário(entry_list, tipo_usuário, lbl_erro, lbl_sucesso))
        
        btn_voltar = ttk.Button(self, text='Voltar', 
                                command=lambda : [controller.show_frame(PáginaInicial), limpar(entry_list, lbl_erro, lbl_sucesso, tipo=tipo_usuário)])
        
        lbl_erro.pack()
        lbl_sucesso.pack()
        radio_usuário.pack(side='left', padx=5)
        radio_admin.pack(side='right', padx=5)
        label_usuário.grid(column=0, row=1, sticky='e')
        label_cpf.grid(column=0, row=2, sticky='e')
        label_senha.grid(column=0, row=3, sticky='e')
        label_confirmar_senha.grid(column=0, row=4, sticky='w') 
        label_telefone.grid(column=0, row=5, sticky='e')
        entry_usuário.grid(column=2, row=1, sticky='e', padx=5, pady=5)
        entry_cpf.grid(column=2, row=2, sticky='e', padx=5, pady=5)
        entry_senha.grid(column=2, row=3, sticky='e', padx=5, pady=5)
        entry_confirmar_senha.grid(column=2, row=4, sticky='e', padx=5, pady=5)
        entry_telefone.grid(column=2, row=5, sticky='e', padx=5, pady=5)
        btn_limpar.grid(column=0, row=0, padx=5)
        btn_cadastrar.grid(column=1, row=0, padx=5)
        btn_voltar.pack(side='left', pady=10, padx=10)
