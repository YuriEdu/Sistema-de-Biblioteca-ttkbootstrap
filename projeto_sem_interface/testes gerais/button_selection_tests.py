import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Create the main window
root = tb.Window(themename="superhero") # You can choose any theme

# Create a Checkbutton with the 'outline-toolbutton' bootstyle
outline_tool_button = tb.Checkbutton(
    root,
    text="Outline Tool Button",
    bootstyle="outline-toolbutton"
)
outline_tool_button.pack(pady=10)

# Create a Checkbutton with a colored 'outline-toolbutton' bootstyle
primary_outline_tool_button = tb.Checkbutton(
    root,
    text="Primary Outline Tool Button",
    bootstyle="primary-outline-toolbutton"
)
primary_outline_tool_button.pack(pady=10)

# Run the application
root.mainloop()