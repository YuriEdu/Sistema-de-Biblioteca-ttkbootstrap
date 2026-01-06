from datetime import date
from utils.controle_dados import *
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

LARGEFONT = ('URW Bookman', 35)
MEDIUMFONT = ('Veranda', 15)
SMALLFONT = ('Veranda', 10)

class Remover(tk.Toplevel):
    def __init__(self, controller):
        tk.Toplevel.__init__(self)