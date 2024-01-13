import tkinter as tk
import time

class Cronometro:
    def __init__(self, root):
        self.root = root
        self.root.title("Meu_Cronometro")
        self.root.geometry("500x400")

        self.root.configure(bg="navy")

        self.frame = tk.Frame(self.root, bg="navy")
        self.frame.pack(pady=10)

        self.titulo = tk.Label(self.frame, text="Meu_Cronometro", font=("Arial", 20), bg="navy", fg="white")
        self.titulo.pack()

        self.buttons_frame = tk.Frame(self.root, bg="navy")
        self.buttons_frame.pack(pady=10)

        self.iniciar = tk.Button(self.buttons_frame, text="Iniciar", command=self.iniciar_cronometro, bg="green", fg="white", font=("Arial", 16))
        self.iniciar.pack(side=tk.LEFT, padx=5)

        self.parar = tk.Button(self.buttons_frame, text="Parar", command=self.parar_cronometro, state=tk.DISABLED, bg="red", fg="white", font=("Arial", 16))
        self.parar.pack(side=tk.LEFT, padx=5)

        self.label = tk.Label(self.root, text="00:00:00", font=("Arial", 24), bg="navy", fg="white")
        self.label.pack(pady=20)

        self.tempo_inicial = None
        self.tempo_parado = 0
        self.executando = False
    
    def iniciar_cronometro(self):
        if not self.executando:
            self.tempo_inicial = time.time() - self.tempo_parado
            self.executando = True
            self.atualizar_cronometro()
            self.iniciar.config(state=tk.DISABLED)
            self.parar.config(state=tk.NORMAL)
            
    def parar_cronometro(self):
        if self.executando:
            self.root.after_cancel(self.atualizar_cronometro)
            self.tempo_parado = time.time() - self.tempo_inicial
            self.executando = False
            self.iniciar.config(state=tk.NORMAL)
            self.parar.config(state=tk.DISABLED)
            
    def atualizar_cronometro(self):
        if self.executando:
            tempo_atual = time.time() - self.tempo_inicial
            horas = int(tempo_atual / 3600)
            minutos = int((tempo_atual % 3600) / 60)
            segundos = int(tempo_atual % 60)
            tempo_formatado = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
            self.label.config(text=tempo_formatado)
            self.root.after(1000, self.atualizar_cronometro)
            
root = tk.Tk()
cronometro = Cronometro(root)
root.mainloop()
