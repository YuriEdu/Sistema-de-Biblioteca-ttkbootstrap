import tkinter as tk

def handle_click(event):
    print("The button was clicked!")

labels = ['First Name:', 'Last Name:',
          'Address Line 1:', 'Address Line 2:',
          'City:', 'State/Province:',
          'Postal Code:', 'Country:']

window = tk.Tk()

window.title('Address Entry Form')

frame_most_stuff = tk.Frame(master=window, relief='sunken', borderwidth=3)
frame_most_stuff.pack()

frame_labels = tk.Frame(master=frame_most_stuff)
frame_labels.grid(row=0, column=0)

frame_entries = tk.Frame(master=frame_most_stuff)
frame_entries.grid(row=0, column=1)

for a, b in enumerate(labels):
    label = tk.Label(master=frame_labels, text=b, fg='black')
    label.grid(row=a, column=0, padx=1, pady=1, sticky='e')
    entry = tk.Entry(master=frame_entries, width=45)
    entry.grid(row=a, column=1, sticky='n')

button_submit = tk.Button(text='Submit')
button_submit.pack(side='right', padx=3, pady=3)

button_clear = tk.Button(text='Clear')
button_clear.pack(side='right', padx=3, pady=3)

button_clear.bind('<Button 1>', handle_click)

window.mainloop()