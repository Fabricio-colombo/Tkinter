import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Criar a janela principal
window = tk.Tk()
window.title("Sistema de Login")

# Lista para armazenar imagens
imagens = []

# Função para centralizar a janela
def center_window(width=600, height=400):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))
    window.configure(bg="black")

# Função para o título da janela
def title():
    title_label = tk.Label(window, text="Sistema de Login", bg="black", fg="gold", font=("Montserrat", 20))
    title_label.pack(pady=(10, 10))

# Função para chamar uma imagem (logotipo)
def logo():
    try:
        # Ajuste o caminho conforme a nova estrutura de pastas
        imagem_pil = Image.open("C:/Users/fabri/OneDrive/Documentos/DESKTOP/Python_projetos/Tkinter/Tkinter_Pillow/download.png")
        imagem_tk = ImageTk.PhotoImage(imagem_pil)
        imagens.append(imagem_tk)  # Manter uma referência à imagem
        logo_label = tk.Label(window, image=imagem_tk, bg="black")
        logo_label.pack(pady=(10, 10))
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")

# Função para os campos de login e senha
def login_senha():
    login_label = tk.Label(window, text="Login:", bg="black", fg="gold", font=("Montserrat", 14))
    login_label.pack(pady=(10, 10))

    login_entry = tk.Entry(window, font=("Montserrat", 12))
    login_entry.pack(pady=(0, 10))

    senha_label = tk.Label(window, text="Senha:", bg="black", fg="gold", font=("Montserrat", 14))
    senha_label.pack(pady=(10, 10))

    senha_entry = tk.Entry(window, show="*", font=("Montserrat", 12))
    senha_entry.pack(pady=(0, 10))

    return login_entry, senha_entry

# Função para o botão de entrar no sistema
def entrar():
    login_digitado = login_entry.get()
    senha_digitada = senha_entry.get()

    # Verificar se o login e a senha estão corretos (substitua isso com a lógica real do banco de dados)
    if login_digitado == "fabricio" and senha_digitada == "fab12345":
        messagebox.showinfo("Login Bem-Sucedido", "Login realizado com sucesso!", icon="info")
    else:
        messagebox.showerror("Credenciais Inválidas", "Login ou senha incorretos. Tente novamente.", icon="error")

# Função para criar o botão de entrar no sistema
def criar_botao_entrar():
    lembrar_senha = tk.Checkbutton(window, text="Lembrar senha", bg="black", fg="gold", font=("Montserrat", 16))
    lembrar_senha.pack(pady=(10, 10))
    
    entrar_button = tk.Button(window, text="Entrar", bg="green", fg="white", font=("Montserrat", 16), command=entrar)
    entrar_button.pack(pady=(10, 10))

# Centralizar a janela
center_window(800, 600)

# Adicionar o título
title()

# Adicionar a imagem (logotipo)
logo()

# Adicionar os campos de login e senha
login_entry, senha_entry = login_senha()

# Adicionar o botão de entrar
criar_botao_entrar()

# Iniciar o loop de eventos
window.mainloop()
