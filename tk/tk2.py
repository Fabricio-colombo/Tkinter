import tkinter as tk

def bom_dia():
    print('Bom dia')
    
def boa_tarde():
    print('Boa tarde')
    
def boa_noite():
    print('Boa noite')

root = tk.Tk()
root.configure(bg='black')

label = tk.Label(root, text='INICIO', background='orange', width=50)
label.pack()

botao1 = tk.Button(root, text='Bom-dia', command=bom_dia, width=20, height=2, background='red')
botao1.pack(pady=10)

botao2 = tk.Button(root, text='Boa-tarde', command=boa_tarde, width=15, height=1, background='blue')
botao2.pack(pady=10)

botao3 = tk.Button(root, text='Boa-noite', command=boa_noite)
botao3.pack(pady=10)

root.mainloop()