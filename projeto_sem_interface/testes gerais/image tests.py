import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Image Display Example")

# Load the image using Pillow (for PNG, JPG, etc.)
# Ensure 'example.png' exists in the same directory as your script
# or provide the full path to the image file.
try:
    pil_image = Image.open("projeto Linguagem de Programação/teste.png")
    # Optional: Resize the image if needed
    # pil_image = pil_image.resize((200, 150), Image.LANCZOS)
    tk_image = ImageTk.PhotoImage(pil_image)
except FileNotFoundError:
    print("Error: 'example.png' not found. Please provide a valid image path.")
    root.destroy()
    exit()

# Create a Label widget to display the image
image_label = tk.Label(root, image=tk_image)
image_label.pack(pady=10) # Add some padding

# Run the Tkinter event loop
root.mainloop()