import tkinter as tk

def f_to_c():
    value = float(ent_temperature.get())
    celsius = (value - 32) / 1.8
    c_label['text'] = f'{celsius:5.1f}\N{DEGREE CELSIUS}'

window = tk.Tk()

window.title('Temperature Converter')
window.resizable(width=False, height=False)

window.rowconfigure(0, weight=1, minsize=50)
window.columnconfigure([0, 1, 2, 3], weight=1, minsize=20)

ent_temperature = tk.Entry(master=window, width=15)
ent_temperature.grid(row=0, column=0, pady=5, padx=5)

f_label = tk.Label(text="\N{DEGREE FAHRENHEIT}")
f_label.grid(row=0, column=1)

btn_convert = tk.Button(master=window, text='\N{RIGHTWARDS BLACK ARROW}', command=f_to_c)
btn_convert.grid(row=0, column=2)

c_label = tk.Label(text='0.0 \N{DEGREE CELSIUS}')
c_label.grid(row=0, column=3, pady=5, padx=5)

window.mainloop()