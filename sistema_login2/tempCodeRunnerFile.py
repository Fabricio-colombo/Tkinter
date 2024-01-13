import tkinter as tk
from tkinter import messagebox
import pygame
import sys

# Função para verificar o login e senha
def verificar_login():
    login = entry_login.get()
    senha = entry_senha.get()

    if login == "fabriciodoidao" and senha == "fabriciomaluco":
        messagebox.showinfo("Sucesso", "Parabéns, você entrou no sistema!")
        # Fechar a janela de login
        window.destroy()
        # Abrir a nova janela com o jogo da cobrinha
        abrir_janela_jogo()
    else:
        messagebox.showerror("Erro", "Login ou senha incorretos. Tente novamente.")

# Função para abrir a janela do jogo da cobrinha
def abrir_janela_jogo():
    # Criar a janela do jogo
    jogo_window = tk.Tk()
    jogo_window.title("Jogo da Cobrinha")
    jogo_window.geometry("400x400")

    # Configurar a cor de fundo da janela para preto
    jogo_window.configure(bg="black")

    # Inicialização do Pygame
    pygame.init()

    # Configurações da tela
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Jogo da Cobrinha")

    # Cores
    golden_color = (255, 215, 0)  # Cor dourada em formato RGB

    # Classe Snake (Cobra)
    class Snake:
        def __init__(self):
            self.size = 1
            self.x = 0
            self.y = 0
            self.color = golden_color
            self.direction = "right"

        def draw(self):
            # Método para desenhar a cobrinha
            # Use self.color ao desenhar a cobrinha
            pass

    # Instância da cobrinha
    snake = Snake()

    # Loop principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Lógica do jogo aqui
        # Desenhe a cobrinha usando snake.draw()

        pygame.display.flip()

    # Iniciar o loop principal da aplicação do jogo
    jogo_window.mainloop()

# Criar a janela principal
window = tk.Tk()
window.title("Sistema de Login")
window.geometry("300x200")

# Configurar a cor de fundo da janela para verde
window.configure(bg="#D8CEC6")

# Criar os widgets da janela
label_title = tk.Label(window, text="Sistema de Login", font=("Arial", 16, "bold"), fg="#cf8f2a")
label_title.pack(pady=20)

label_login = tk.Label(window, text="Login:", bg="#c6d0d8")
label_login.pack()

entry_login = tk.Entry(window, bg="#c6d0d8")
entry_login.pack()

label_senha = tk.Label(window, text="Senha:", bg="#c6d0d8")
label_senha.pack()

entry_senha = tk.Entry(window, show="*", bg="#c6d0d8")
entry_senha.pack()

button_entrar = tk.Button(window, text="Entrar", command=verificar_login)
button_entrar.pack()

# Centralizar a janela
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())

# Iniciar o loop principal da aplicação
window.mainloop()
