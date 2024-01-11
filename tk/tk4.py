import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text='Sistema de Login')
label.pack()

botao1 = tk.Checkbutton(root, text='Login')
botao1.pack()

entry = tk.Entry(root)
entry.pack(pady=5)
root.mainloop()
