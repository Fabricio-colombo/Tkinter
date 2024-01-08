import tkinter as tk

root = tk.Tk()
sub_window = tk.Toplevel(root)

canvas = tk.Canvas(root, width=200, height=100)
canvas.pack()

canvas.create_rectangle(50, 25, 150, 75, fill="blue")


root.mainloop()