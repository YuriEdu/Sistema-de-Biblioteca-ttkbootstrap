import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from menus.login import Login
from menus.página_inicial import PáginaInicial, UsuárioCadastro
from menus.cadastro import Cadastro
from menus.atualizar import Atualizar

class tkinterApp(tk.Tk):

    def __init__(self, janela_inicial, *args, **kwargs):

        tk.Tk.__init__(self)

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Login, PáginaInicial, Cadastro, UsuárioCadastro):

            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(janela_inicial)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def página_inicial(self):
        self.show_frame(PáginaInicial)