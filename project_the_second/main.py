from utils.controle_dados import *
from ttkbootstrap.constants import *
from core.tkinterapp import *

app = tkinterApp(janela_inicial=Login)
style = ttk.Style(theme='darkly')
style.configure(
    'TButton',
    font=BUTTONFONT
)
app.title('Biblioteca')
app.resizable(False, False)
app.mainloop()