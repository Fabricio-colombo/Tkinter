import tkinter as tk

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Verificar as credenciais do usuário
    if username == "admin" and password == "12345":
        print("Login bem-sucedido!")
    else:
        print("Credenciais inválidas!")

# Criar a janela principal
window = tk.Tk()
window.title("Login")
window.geometry("400x300")  # Definir o tamanho da janela

# Definir estilos personalizados
window.configure(bg="lightblue")  # Definir cor de fundo da janela

# Criar os widgets
username_label = tk.Label(window, text="Nome de usuário:", bg="lightblue", font=("Arial", 14))
username_label.pack()

username_entry = tk.Entry(window, font=("Arial", 12))
username_entry.pack()

password_label = tk.Label(window, text="Senha:", bg="lightblue", font=("Arial", 14))
password_label.pack()

password_entry = tk.Entry(window, show="*", font=("Arial", 12))
password_entry.pack()

login_button = tk.Button(window, text="Entrar", command=login, bg="lightgreen", fg="white", font=("Arial", 12))
login_button.pack()

# Iniciar o loop de eventos
window.mainloop()
