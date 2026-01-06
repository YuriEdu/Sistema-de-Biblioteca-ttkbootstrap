from utils.controle_dados import *
from ttkbootstrap.constants import *
from core.tkinterapp import *

app = tkinterApp(janela_inicial=PáginaInicial)
style = ttk.Style(theme='darkly')
app.title('Biblioteca')
app.resizable(False, False)
app.mainloop()