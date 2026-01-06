from utils.controle_dados import *
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from menus.página_inicial import PáginaInicial
from menus.página_usuário import PáginaUsuário


class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def enter_pressionado(event):
            self.validar_login(parent, entry_username, entry_senha, controller, lbl_erro)

        label = ttk.Label(self, text='Login', font=LARGEFONT)
        label.pack(pady=60, padx=150)

        lbl_erro = ttk.Label(self, text='', foreground='red')
        lbl_erro.pack()

        frame_other = ttk.Frame(self)
        frame_other.pack(pady=10)

        label_username = ttk.Label(frame_other, text='Usuário:')
        label_senha = ttk.Label(frame_other, text='Senha:')
        entry_username = ttk.Entry(frame_other, width=25)
        entry_senha = ttk.Entry(frame_other, width=25, show='*')

        frame_buttons = ttk.Frame(self)
        frame_buttons.pack(pady=20)

        btn_login = ttk.Button(frame_buttons, text='Login', width=10,
                               command=lambda : self.validar_login(parent, entry_username, entry_senha, controller, lbl_erro))
        
        self.master.master.bind('<Return>', enter_pressionado)

        label_username.grid(column=0, row=2, sticky='e')
        label_senha.grid(column=0, row=3, sticky='e')
        entry_username.grid(column=1, row=2, sticky='e', padx=5, pady=5)
        entry_senha.grid(column=1, row=3, sticky='e', padx=5, pady=5)
        btn_login.grid(column=0, row=0, sticky='s', columnspan=5, pady=40)

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
                        break
                    else:
                        cont.show_frame(PáginaInicial)
                    break
                else:
                    label.config(text='Senha incorreta')
                    break
        if not usuário_encontrado:
            label.config(text='Usuário não cadastrado')

