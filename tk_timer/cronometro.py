import time
import tkinter as tk

def cronometro():
    for num in range(10, 0, -1):
        time.sleep(1)
        print(num, end=' \r')
    print('fim')
    
#cronometro()


janela = tk.Tk()

label = tk.Label(janela, text='TEXTO DA JANELA', width=50, height=2, foreground='Black', relief='groove',)
label.pack()

botao1 = tk.Button(janela, text='BOTÃO 1', bg='Black', height=1, font=4, foreground='Red', relief='sunken')
botao1.pack()

botao2 = tk.Button(janela, text='BOTÃO 2', bg='Black', height=1, font=4, foreground='Red', relief='ridge')
botao2.pack()

botao3 = tk.Entry(janela, textvariable='HAHA', insertbackground='Green')
botao3.pack()

janela.mainloop() 