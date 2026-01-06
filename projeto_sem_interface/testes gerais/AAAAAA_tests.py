import tkinter as tk

root = tk.Tk()
root.title("Half X-axis Frames")
root.geometry("600x400") # Set an initial size for the window

# Create the first frame (left half)
frame1 = tk.Frame(root, bg="lightblue", relief=tk.RAISED, borderwidth=2)
frame1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create the second frame (right half)
frame2 = tk.Frame(root, bg="lightgreen", relief=tk.RAISED, borderwidth=2)
frame2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Add some content to the frames to visualize them
label1 = tk.Label(frame1, text="This is the left half", bg="lightblue")
label1.pack(pady=20)

label2 = tk.Label(frame2, text="This is the right half", bg="lightgreen")
label2.pack(pady=20)

root.mainloop()