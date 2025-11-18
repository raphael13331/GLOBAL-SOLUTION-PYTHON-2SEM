import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# Classe Perfil Profissional
class Perfil:
    def __init__(self, nome, competencias):
        self.nome = nome
        self.competencias = competencias  # dicionário {competencia: valor}

    def media(self):
        return sum(self.competencias.values()) / len(self.competencias)

# Classe Orientador Inteligente
class Orientador:
    def __init__(self):
        # Dicionário de possíveis áreas futuras
        self.carreiras = {
            "Engenharia de Software": ("lógica", "análise", "criatividade"),
            "Design e UX": ("criatividade", "empatia", "colaboração"),
            "Ciência de Dados": ("lógica", "análise", "adaptabilidade"),
            "Gestão de Projetos": ("liderança", "colaboração", "planejamento"),
            "Pesquisa e Inovação": ("curiosidade", "criatividade", "adaptabilidade"),
            "IA e Robótica": ("lógica", "curiosidade", "análise"),
            "Educação Digital": ("empatia", "comunicação", "adaptabilidade"),
        }

    def recomendar(self, perfil: Perfil):
        # Calcula afinidade com cada carreira
        afinidades = {}
        for carreira, comps in self.carreiras.items():
            pontuacao = sum(perfil.competencias.get(c, 0) for c in comps)
            afinidades[carreira] = pontuacao

        # Ordena as carreiras por pontuação
        recomendadas = sorted(afinidades.items(), key=lambda x: x[1], reverse=True)
        return recomendadas[:3]  # top 3 recomendações

# Tela do Teste de Perfil
class TelaTeste(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Descobrir Meu Perfil Profissional")
        self.geometry("600x800")
        self.orientador = Orientador()
        self.criar_interface()

    def criar_interface(self):
        tk.Label(self, text="Análise de Perfil Profissional do Futuro",
                 font=("Arial", 16, "bold")).pack(pady=10)

        frame = tk.Frame(self)
        frame.pack(pady=10)

        tk.Label(frame, text="Nome:").grid(row=0, column=0, sticky="w")
        self.nome_entry = tk.Entry(frame, width=40)
        self.nome_entry.grid(row=0, column=1, pady=5)

        # Competências
        self.competencias = ["lógica", "criatividade", "colaboração",
                             "adaptabilidade", "liderança", "empatia",
                             "análise", "comunicação", "planejamento", "curiosidade"]
        self.sliders = {}

        for i, comp in enumerate(self.competencias):
            tk.Label(frame, text=f"{comp.capitalize()}:").grid(row=i+1, column=0, sticky="w", pady=2)
            slider = ttk.Scale(frame, from_=0, to=10, orient="horizontal")
            slider.set(5)
            slider.grid(row=i+1, column=1, padx=5, pady=2, sticky="we")
            self.sliders[comp] = slider

        # Botão de análise
        tk.Button(self, text="Analisar Perfil", command=self.analisar_perfil, bg="#007acc", fg="white", font=("Arial", 12, "bold")).pack(pady=20)

        self.resultado_box = tk.Text(self, height=10, width=70, wrap="word", state="disabled")
        self.resultado_box.pack(pady=10)

    def analisar_perfil(self):
        nome = self.nome_entry.get().strip()
        if not nome:
            messagebox.showwarning("Atenção", "Digite o nome do perfil!")
            return

        competencias = {comp: int(self.sliders[comp].get()) for comp in self.competencias}
        perfil = Perfil(nome, competencias)
        recomendacoes = self.orientador.recomendar(perfil)

        self.resultado_box.config(state="normal")
        self.resultado_box.delete(1.0, tk.END)
        self.resultado_box.insert(tk.END, f"  Análise do perfil de {nome}:\n\n")

        media = perfil.media()
        self.resultado_box.insert(tk.END, f"Média geral de competências: {media:.2f}\n\n")

        self.resultado_box.insert(tk.END, "  Carreiras recomendadas:\n")
        for carreira, nota in recomendacoes:
            self.resultado_box.insert(tk.END, f" - {carreira} (afinidade: {nota:.1f})\n")

        self.resultado_box.insert(tk.END, "\n Sugestão: explore trilhas e cursos nessas áreas.")
        self.resultado_box.config(state="disabled")

# Tela de Faculdades
class TelaFaculdades(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Faculdades Recomendadas")
        self.geometry("600x400")
        self.criar_interface()

    def criar_interface(self):
        tk.Label(self, text="Faculdades e Áreas Promissoras do Futuro",
                 font=("Arial", 16, "bold")).pack(pady=10)

        texto = tk.Text(self, height=20, width=70, wrap="word")
        texto.pack(pady=10)

        conteudo = """
Áreas em alta no futuro:

- Inteligência Artificial e Robótica → Engenharia da Computação, Ciência de Dados, Sistemas de Informação.
- Sustentabilidade e Meio Ambiente → Engenharia Ambiental, Biotecnologia.
- Design e Experiência Digital → Design Gráfico, UX/UI Design.
- Educação e Tecnologia → Pedagogia Digital, Licenciatura em Computação.
- Neurociência e Psicologia Cognitiva → Psicologia, Neuroengenharia.

Integração com API da Alura:
Em versões futuras, será possível acessar trilhas da Alura automaticamente,
com base no perfil do usuário.
"""
        texto.insert(tk.END, conteudo)
        texto.config(state="disabled")

# Tela Inicial (Home)
class HomeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Orientador de Carreiras do Futuro")
        self.attributes('-fullscreen', True)  # tela cheia
        self.bind("<Escape>", lambda e: self.attributes('-fullscreen', False))

        # Imagem de fundo
        self.bg_image = Image.open("bg.png")  # substitua pelo caminho da sua imagem
        self.bg_label = tk.Label(self)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.bind("<Configure>", self.redimensionar_imagem)

        # Criar o menu
        self.criar_menu()

    def redimensionar_imagem(self, event):
        # Redimensiona imagem ao tamanho da tela
        nova_imagem = self.bg_image.resize((event.width, event.height))
        self.bg_photo = ImageTk.PhotoImage(nova_imagem)
        self.bg_label.config(image=self.bg_photo)

    def criar_menu(self):
        frame = tk.Frame(self, bg="black")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(text="🌐 Orientador de Carreiras do Futuro", font=("Arial", 24, "bold"), fg="black").pack(pady=20)

        tk.Button(frame, text=" Descobrir meu perfil", font=("Arial", 16), width=30, command=self.abrir_teste).pack(pady=10)

        tk.Button(frame, text=" Faculdades recomendadas", font=("Arial", 16), width=30, command=self.abrir_faculdades).pack(pady=10)

        tk.Button(frame, text=" Sair", font=("Arial", 16), width=30, command=self.destroy).pack(pady=10)

    def abrir_teste(self):
        TelaTeste(self)

    def abrir_faculdades(self):
        TelaFaculdades(self)

# Execução
if __name__ == "__main__":
    app = HomeApp()
    app.mainloop()

