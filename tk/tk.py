import tkinter as tk

def clique_do_botao():
    print("Botão clicado!")
    
def botao1():
    print('Clicou novamente!')

root = tk.Tk()

label = tk.Label(root, text="Eae caga tronco")
label.pack()

botao = tk.Button(root, text="Clica ai", command=clique_do_botao)
botao.pack()

botao1 = tk.Button(root, text='Salve', command=botao1)
botao1.pack()

root.mainloop()
