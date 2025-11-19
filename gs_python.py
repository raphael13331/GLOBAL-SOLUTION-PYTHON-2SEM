import tkinter as tk
from tkinter import ttk, messagebox
import traceback

# Modelos: Perfil e Orientador
class Perfil:
    def _init_(self, nome, competencias):
        self.nome = nome
        self.competencias = competencias # dict {competencia: valor}

    # Calcula a média das competências do perfil
    def media(self):
        if not self.competencias:
            return 0
        return sum(self.competencias.values()) / len(self.competencias)


class Orientador:
    def _init_(self):
        # Mapeia carreiras para suas competências chave
        self.carreiras = {
            "Engenharia de Software": ("lógica", "análise", "criatividade"),
            "Design e UX": ("criatividade", "empatia", "colaboração"),
            "Ciência de Dados": ("lógica", "análise", "adaptabilidade"),
            "Gestão de Projetos": ("liderança", "colaboração", "planejamento"),
            "Pesquisa e Inovação": ("curiosidade", "criatividade", "adaptabilidade"),
            "IA e Robótica": ("lógica", "curiosidade", "análise"),
            "Educação Digital": ("empatia", "comunicação", "adaptabilidade"),
            "Engenharia de Prompt (IA)": ("lógica", "criatividade", "comunicação"),
            "Cibersegurança": ("análise", "lógica", "planejamento"),
            "Desenvolvedor Mobile": ("lógica", "criatividade", "análise"),
            "Marketing Digital e Growth": ("criatividade", "análise", "comunicação"),
            "Desenvolvedor de Games": ("criatividade", "lógica", "colaboração"),
            "Biotecnologia e Saúde Digital": ("curiosidade", "análise", "adaptabilidade"),
            "Engenharia Ambiental Futurista": ("planejamento", "análise", "adaptabilidade"),
            "Arquitetura de Sistemas de IA": ("lógica", "análise", "planejamento"),
            "Analista de UX Writing": ("comunicação", "empatia", "criatividade"),
            "Criador de Conteúdo e Influência Digital": ("criatividade", "comunicação", "adaptabilidade"),
            "Especialista em Realidade Aumentada/Virtual": ("criatividade", "análise", "colaboração"),
            "Consultor de Ética em IA": ("curiosidade", "comunicação", "análise"),
        }

    # Calcula a afinidade entre o perfil e as carreiras
    def recomendar(self, perfil: Perfil, top_n=3):
        # Afinidade simples: soma das competências presentes (pode ser estendida com pesos)
        afinidades = {}
        for carreira, comps in self.carreiras.items():
            pontuacao = sum(perfil.competencias.get(c, 0) for c in comps)
            # Normaliza a pontuação pelo número de competências da carreira
            pontuacao_normalizada = pontuacao / max(len(comps), 1)
            afinidades[carreira] = pontuacao_normalizada

        # Ordena e retorna as top_n carreiras mais recomendadas
        recomendadas = sorted(afinidades.items(), key=lambda x: x[1], reverse=True)
        return recomendadas[:top_n]


# Tema / Estética (Dark Tech)
class Theme:
    # Paleta de cores para o tema escuro
    DARK = {
        "bg": "#0b0f14",
        "panel": "#071022",
        "accent": "#00e6d6",
        "muted": "#8b98a6",
        "text": "#dff6f5",
        "danger": "#ff5c7c",
        "card": "#0f1720",
        "button_bg": "#06212a"
    }

    # Paleta de cores para o tema claro
    LIGHT = {
        "bg": "#f6f7fb",
        "panel": "#ffffff",
        "accent": "#0066cc",
        "muted": "#6b7280",
        "text": "#0f1720",
        "danger": "#b91c1c",
        "card": "#ffffff",
        "button_bg": "#e6eef9"
    }


# UI: Tela principal e teste
# Janela de teste de perfil (Toplevel)
class TelaTeste(tk.Toplevel):
    def _init_(self, master, theme, *args, **kwargs):
        super()._init_(master, *args, **kwargs)
        self.master = master
        self.theme = theme
        self.orientador = Orientador()
        self.title("Descobrir Meu Perfil Profissional — Orientador Futuro")
        self.geometry("820x760")
        self.resizable(False, False)
        self.configure(bg=self.theme["bg"])
        self.competencias = [
            "lógica", "criatividade", "colaboração",
            "adaptabilidade", "liderança", "empatia",
            "análise", "comunicação", "planejamento", "curiosidade"
        ]
        self.sliders = {}
        self.criar_interface()

    # Constrói a interface do formulário com sliders
    def criar_interface(self):
        card = tk.Frame(self, bg=self.theme["card"])
        card.place(relx=0.5, rely=0.5, anchor="center", width=760, height=700)

        titulo = tk.Label(card, text="Análise de Perfil Profissional", font=("Segoe UI", 16, "bold"),
                          bg=self.theme["card"], fg=self.theme["accent"])
        titulo.pack(pady=(18, 6))

        subt = tk.Label(card, text="Avalie suas competências (0-10)", font=("Segoe UI", 10),
                        bg=self.theme["card"], fg=self.theme["muted"])
        subt.pack(pady=(0, 14))

        form = tk.Frame(card, bg=self.theme["card"])
        form.pack(padx=20, pady=6, fill="x")

        nome_label = tk.Label(form, text="Nome:", bg=self.theme["card"], fg=self.theme["text"], font=("Segoe UI", 10))
        nome_label.grid(row=0, column=0, sticky="w")
        self.nome_entry = tk.Entry(form, font=("Segoe UI", 11), bd=0, highlightthickness=1, relief="flat")
        self.nome_entry.grid(row=0, column=1, sticky="we", padx=(8, 0), pady=6)
        form.columnconfigure(1, weight=1)

        sliders_frame = tk.Frame(form, bg=self.theme["card"])
        sliders_frame.grid(row=1, column=0, columnspan=2, pady=(6, 0), sticky="we")

        for i, comp in enumerate(self.competencias):
            r = i // 2
            c = (i % 2) * 2
            label = tk.Label(sliders_frame, text=f"{comp.capitalize()}:", bg=self.theme["card"],
                             fg=self.theme["text"], anchor="w", font=("Segoe UI", 10))
            label.grid(row=r, column=c, sticky="w", padx=(0, 6), pady=6)

            # Armazena o slider para recuperar seu valor depois
            slider = ttk.Scale(sliders_frame, from_=0, to=10, orient="horizontal", length=260)
            slider.set(5)
            slider.grid(row=r, column=c+1, sticky="w", padx=(0, 14), pady=6)
            self.sliders[comp] = slider

        botoes = tk.Frame(card, bg=self.theme["card"])
        botoes.pack(pady=(12, 8))

        analisar_btn = tk.Button(botoes, text="Analisar Perfil", command=self.analisar_perfil,
                                 bg=self.theme["button_bg"], fg=self.theme["text"],
                                 font=("Segoe UI", 11, "bold"), bd=0, padx=18, pady=8)
        analisar_btn.pack(side="left", padx=8)

        fechar_btn = tk.Button(botoes, text="Fechar", command=self.destroy,
                               bg=self.theme["card"], fg=self.theme["muted"],
                               font=("Segoe UI", 10), bd=0, padx=14, pady=8)
        fechar_btn.pack(side="left", padx=8)

        resultado_card = tk.Frame(card, bg=self.theme["panel"])
        resultado_card.pack(padx=20, pady=(12, 18), fill="both", expand=True)

        self.resultado_box = tk.Text(resultado_card, height=8, width=82, wrap="word",
                                     bg=self.theme["panel"], fg=self.theme["text"], bd=0)
        self.resultado_box.pack(padx=10, pady=10, fill="both", expand=True)
        self.resultado_box.insert("1.0", "Resultado aparecerá aqui...")
        self.resultado_box.config(state="disabled")

    # Coleta dados e exibe o resultado da análise de perfil
    def analisar_perfil(self):
        nome = self.nome_entry.get().strip()
        if not nome:
            messagebox.showwarning("Atenção", "Digite o nome do perfil!")
            return

        try:
            # Cria o dicionário de competências a partir dos valores dos sliders
            competencias = {comp: int(round(self.sliders[comp].get())) for comp in self.competencias}
        except Exception:
            competencias = {comp: 0 for comp in self.competencias}

        perfil = Perfil(nome, competencias)
        recomendacoes = self.orientador.recomendar(perfil, top_n=5)

        # Atualiza a caixa de texto com o resultado
        self.resultado_box.config(state="normal")
        self.resultado_box.delete(1.0, tk.END)
        self.resultado_box.insert(tk.END, f"Análise do perfil: {nome}\n\n")
        self.resultado_box.insert(tk.END, f"Média geral de competências: {perfil.media():.2f}\n\n")
        self.resultado_box.insert(tk.END, "Carreiras recomendadas (top):\n")

        for carreira, nota in recomendacoes:
            self.resultado_box.insert(tk.END, f" • {carreira} — Afinidade: {nota:.2f}\n")

        self.resultado_box.insert(tk.END, "\nSugestão: explore cursos e trilhas nessas áreas para fortalecer pontos fracos.")
        self.resultado_box.config(state="disabled")


# Janela principal da aplicação (HomeApp)
class HomeApp(tk.Tk):
    def _init_(self):
        super()._init_()
        self.title("Orientador de Carreiras do Futuro — Dark Tech")
        self.geometry("1200x720")
        self.minsize(1000, 640)

        # Configuração inicial do tema
        self.is_dark = True
        self.theme = Theme.DARK if self.is_dark else Theme.LIGHT
        self.configure(bg=self.theme["bg"])

        style = ttk.Style(self)
        try:
            style.theme_use('default')
        except Exception:
            pass

        self.criar_interface()

    # Constrói a interface principal (header, conteúdo e painéis laterais)
    def criar_interface(self):
        top = tk.Frame(self, bg=self.theme["panel"], height=72)
        top.pack(fill="x", side="top")

        title = tk.Label(top, text="⚡ Orientador de Carreiras do Futuro", font=("Segoe UI", 18, "bold"),
                         bg=self.theme["panel"], fg=self.theme["accent"])
        title.pack(side="left", padx=24)

        subtitle = tk.Label(top, text="Estilo: Dark Tech Futurista — Toggle Claro/Escuro disponível",
                            bg=self.theme["panel"], fg=self.theme["muted"], font=("Segoe UI", 10))
        subtitle.pack(side="left", padx=(12, 0), pady=6)

        toggle_btn = tk.Button(top, text="Alternar Tema", command=self.toggle_tema,
                               bg=self.theme["button_bg"], fg=self.theme["text"], bd=0, padx=12)
        toggle_btn.pack(side="right", padx=18, pady=12)

        content = tk.Frame(self, bg=self.theme["bg"])
        content.pack(fill="both", expand=True, padx=28, pady=18)

        left = tk.Frame(content, bg=self.theme["card"], width=620)
        left.pack(side="left", fill="both", expand=True, padx=(0, 12), pady=4)

        right = tk.Frame(content, bg=self.theme["card"], width=420)
        right.pack(side="right", fill="y", padx=(12, 0), pady=4)

        hero = tk.Frame(left, bg=self.theme["card"], pady=20)
        hero.pack(fill="x", padx=18, pady=12)

        h1 = tk.Label(hero, text="Descubra carreiras compatíveis com seu perfil", font=("Segoe UI", 16, "bold"),
                      bg=self.theme["card"], fg=self.theme["accent"])
        h1.pack(anchor="w")

        p = tk.Label(hero, text="Avalie suas competências e receba recomendações de profissões emergentes.",
                      font=("Segoe UI", 11), bg=self.theme["card"], fg=self.theme["muted"])
        p.pack(anchor="w", pady=(8, 0))

        actions = tk.Frame(left, bg=self.theme["card"])
        actions.pack(padx=18, pady=8, fill="x")

        abrir_teste_btn = tk.Button(actions, text="▶️ Fazer teste de perfil", command=self.abrir_teste,
                                    bg=self.theme["button_bg"], fg=self.theme["text"], bd=0, padx=14, pady=12,
                                    font=("Segoe UI", 11, "bold"))
        abrir_teste_btn.pack(side="left", padx=6)

        abrir_fac_btn = tk.Button(actions, text="📚 Ver carreiras adicionadas", command=self.abrir_faculdades,
                                  bg=self.theme["panel"], fg=self.theme["text"], bd=0, padx=14, pady=12,
                                  font=("Segoe UI", 10, "bold"))
        abrir_fac_btn.pack(side="left", padx=6)

        quick_title = tk.Label(right, text="Novas Carreiras (destaque)", font=("Segoe UI", 12, "bold"),
                               bg=self.theme["card"], fg=self.theme["accent"])
        quick_title.pack(anchor="nw", padx=18, pady=(18, 8))

        carreiras_frame = tk.Frame(right, bg=self.theme["card"])
        carreiras_frame.pack(fill="both", expand=True, padx=12, pady=6)

        orientador = Orientador()
        novas = [
            "Engenharia de Prompt (IA)",
            "Cibersegurança",
            "Desenvolvedor Mobile",
            "Marketing Digital e Growth",
            "Desenvolvedor de Games",
            "Biotecnologia e Saúde Digital",
            "Engenharia Ambiental Futurista",
            "Arquitetura de Sistemas de IA",
            "Analista de UX Writing",
            "Criador de Conteúdo e Influência Digital",
            "Especialista em Realidade Aumentada/Virtual",
            "Consultor de Ética em IA"
        ]

        for c in novas:
            box = tk.Frame(carreiras_frame, bg=self.theme["panel"], pady=8, padx=8)
            box.pack(fill="x", pady=6, padx=8)
            lbl = tk.Label(box, text=c, font=("Segoe UI", 10, "bold"),
                           bg=self.theme["panel"], fg=self.theme["text"], anchor="w")
            lbl.pack(side="left", padx=(6, 8))
            skills = orientador.carreiras.get(c, ())
            sk_lbl = tk.Label(box, text=", ".join(skills), font=("Segoe UI", 9),
                              bg=self.theme["panel"], fg=self.theme["muted"], anchor="e")
            sk_lbl.pack(side="right", padx=(8, 6))

        footer = tk.Frame(left, bg=self.theme["card"], height=56)
        footer.pack(fill="x", side="bottom", padx=18, pady=14)
        dica = tk.Label(footer,
                         text="Dica: use o teste para receber as 5 melhores recomendações. Modo claro/escuro preserva o visual futurista.",
                         font=("Segoe UI", 9), bg=self.theme["card"], fg=self.theme["muted"])
        dica.pack(anchor="w", padx=8)

    # Alterna entre os temas claro e escuro
    def toggle_tema(self):
        self.is_dark = not self.is_dark
        self.theme = Theme.DARK if self.is_dark else Theme.LIGHT
        self.recolorizar_ui()

    # Recria a interface com as novas cores do tema
    def recolorizar_ui(self):
        for w in self.winfo_children():
            w.destroy()
        self.configure(bg=self.theme["bg"])
        self.criar_interface()

    # Abre a janela do teste de perfil
    def abrir_teste(self):
        TelaTeste(self, self.theme)

    # Abre a janela de carreiras/faculdades
    def abrir_faculdades(self):
        TelaFaculdades(self, self.theme)


# Janela Toplevel para exibir informações de faculdades
class TelaFaculdades(tk.Toplevel):
    def _init_(self, master, theme, *args, **kwargs):
        super()._init_(master, *args, **kwargs)
        self.theme = theme
        self.title("Faculdades e Áreas Promissoras")
        self.geometry("720x520")
        self.configure(bg=self.theme["bg"])
        self.criar_interface()

    # Constrói a interface de exibição de texto
    def criar_interface(self):
        card = tk.Frame(self, bg=self.theme["card"])
        card.pack(fill="both", expand=True, padx=18, pady=18)

        titulo = tk.Label(card, text="Faculdades e Áreas Promissoras do Futuro",
                          font=("Segoe UI", 14, "bold"), bg=self.theme["card"], fg=self.theme["accent"])
        titulo.pack(anchor="w", pady=(8, 6), padx=8)

        texto = tk.Text(card, height=20, wrap="word", bg=self.theme["panel"], fg=self.theme["text"], bd=0)
        texto.pack(fill="both", expand=True, padx=8, pady=(4, 8))
        conteudo = (
            "Áreas em alta no futuro e cursos relacionados:\n\n"
            "- Inteligência Artificial e Robótica → Engenharia da Computação, Ciência de Dados, Sistemas de Informação.\n"
            "- Sustentabilidade e Meio Ambiente → Engenharia Ambiental, Biotecnologia.\n"
            "- Design e Experiência Digital → Design Gráfico, UX/UI Design.\n"
            "- Educação e Tecnologia → Pedagogia Digital, Licenciatura em Computação.\n"
            "- Neurociência e Psicologia Cognitiva → Psicologia, Neuroengenharia.\n"
            "- Cibersegurança → Segurança da Informação, Engenharia de Redes.\n"
            "- Biotecnologia e Saúde Digital → Biomedicina, Engenharia Biomédica.\n"
            "- Realidade Aumentada/Virtual → Design de Interação, Engenharia Multimídia.\n\n"
            "Observação: essas são sugestões iniciais. Combine interesses pessoais com as competências técnicas e comportamentais "
            "avaliadas no teste para escolher a trilha ideal."
        )
        texto.insert("1.0", conteudo)
        texto.config(state="disabled")

        fechar = tk.Button(card, text="Fechar", command=self.destroy,
                           bg=self.theme["button_bg"], fg=self.theme["text"], bd=0, padx=12, pady=8)
        fechar.pack(pady=(8, 10))


# Execução
# Ponto de entrada da aplicação
def main():
    try:
        app = HomeApp()
        app.mainloop()
    except Exception as e:
        # Log de erro e exibição de alerta
        err = traceback.format_exc()
        print("Erro ao executar a aplicação:\n", err)
        try:
            messagebox.showerror("Erro", f"Ocorreu um erro ao iniciar a aplicação.\nVeja o terminal para mais detalhes.\n\n{e}")
        except Exception:
            pass


if _name_ == "_main_":
    main()
