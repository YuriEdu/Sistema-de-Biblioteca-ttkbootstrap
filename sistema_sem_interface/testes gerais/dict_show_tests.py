import tkinter as tk

root = tk.Tk()
root.title("Dictionary Display")

my_dict = {"Name": "Alice", "Age": 30, "City": "New York"}
formatted_text = f"User Details:\nName: {my_dict['Name']}\nAge: {my_dict['Age']}\nCity: {my_dict['City']}"

label = tk.Label(root, text=formatted_text, justify=tk.LEFT, font=("Arial", 12))
label.pack(pady=10, padx=10)

root.mainloop()