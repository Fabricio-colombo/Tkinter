import tkinter as tk

class Cronometro:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronômetro")

        self.label = tk.Label(root, text='Contagem Regressiva')
        self.label.pack()

        self.botao_iniciar = tk.Button(root, text='Iniciar', command=self.iniciar_cronometro)
        self.botao_iniciar.pack()

        self.botao_pausar = tk.Button(root, text='Pausar', command=self.pausar_cronometro)
        self.botao_pausar.pack()

        self.botao_reset = tk.Button(root, text='Resetar', command=self.resetar_cronometro)
        self.botao_reset.pack()

        self.contando = False
        self.tempo_restante = 11
        self.atualizar_label()

    def iniciar_cronometro(self):
        if not self.contando:
            self.contando = True
            self.contagem_regressiva()

    def pausar_cronometro(self):
        self.contando = False

    def resetar_cronometro(self):
        self.contando = False
        self.tempo_restante = 11
        self.atualizar_label()

    def contagem_regressiva(self):
        if self.contando and self.tempo_restante > 0:
            self.tempo_restante -= 1
            self.atualizar_label()
            self.root.after(1000, self.contagem_regressiva)
        else:
            self.contando = False

    def atualizar_label(self):
        self.label.config(text=f'Tempo restante: {self.tempo_restante}s')

if __name__ == "__main__":
    root = tk.Tk()
    cronometro_app = Cronometro(root)
    root.mainloop()
