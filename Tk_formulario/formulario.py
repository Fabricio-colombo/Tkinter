import tkinter as tk

class FormularioCadastro:
    def __init__(self, master):
        self.master = master
        self.master.title("Formulário de Cadastro")
        self.master.geometry("800x600")

        self.criar_formulario()

    def criar_formulario(self):
        # LabelFrame para agrupar os campos do formulário
        frame_formulario = tk.LabelFrame(self.master, text="Cadastro")
        frame_formulario.pack(padx=20, pady=20, fill="both", expand="yes")

        # Lista de campos
        campos = ["Nome", "Email", "Telefone", "Curso", "Sexo", "Idade", "Cidade",
                  "Estado", "Pais", "Profissão", "Empresa", "Observações"]

        # Dicionário para armazenar os Entry widgets e StringVar
        self.dados = {campo: tk.StringVar() for campo in campos}
        self.entries = {}

        # Criar e posicionar os campos do formulário
        for i, campo in enumerate(campos):
            label = tk.Label(frame_formulario, text=f"{campo}:")
            label.grid(row=i, column=0, padx=10, pady=5, sticky=tk.E)

            entry = tk.Entry(frame_formulario, textvariable=self.dados[campo])
            entry.grid(row=i, column=1, padx=10, pady=5, sticky=tk.W)
            self.entries[campo] = entry

        # Botões de Enviar e Cancelar
        btn_enviar = tk.Button(self.master, text="Enviar", command=self.enviar_formulario)
        btn_enviar.pack(side=tk.LEFT, padx=10)

        btn_cancelar = tk.Button(self.master, text="Cancelar", command=self.master.destroy)
        btn_cancelar.pack(side=tk.RIGHT, padx=10)

    def enviar_formulario(self):
        # Exemplo: Imprimir os dados do formulário
        for campo, valor in self.dados.items():
            print(f"{campo}: {valor.get()}")
        # Adicione aqui a lógica para processar os dados do formulário.

if __name__ == "__main__":
    root = tk.Tk()
    app = FormularioCadastro(root)
    root.mainloop()
