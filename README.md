
# Orientador de Carreiras do Futuro


Este projeto apresenta uma aplicação interativa criada em Python utilizando a biblioteca Tkinter. Ela permite analisar habilidades pessoais e, a partir disso, sugerir carreiras com grande potencial para os próximos anos.
Além disso, o sistema conta com uma tela específica destinada a faculdades indicadas, alinhadas às áreas tecnológicas e profissionais emergentes.

A ideia central é disponibilizar uma ferramenta simples, visual e prática que auxilie estudantes e profissionais a explorarem possíveis caminhos de carreira com base em suas competências.

---

## Instruções de Execução

### Pré-requisitos
- Python 3.10+
- Instalar dependências:
`pip install pillow`

- Arquivo de imagem `bg.png` deve estar no mesmo diretório do projeto.

### Executando o programa
1. Baixe ou clone este repositório.  
2. Certifique-se de que o arquivo `gs_python.py` está no diretório principal.  
3. Execute a aplicação com:
`python gs_python.py`

4. Utilize a tela inicial para navegar entre:
- **Descobrir meu perfil**
- **Faculdades recomendadas**

---

## Estrutura de Arquivos e Classes

├── gs_python.py # Código principal do projeto

├── bg.png # Imagem de fundo da tela inicial

├── README.md # Documentação do projeto


### Principais Classes

#### `Perfil`
Representa o usuário que está sendo avaliado, contendo seu nome e as competências inseridas.
Métodos:
- `media()` → calcula a média das competências.

#### `Orientador`
Analisa os valores das competências e determina a afinidade com carreiras futuramente promissoras.
Métodos:
- `recomendar(perfil)` → retorna as três principais recomendações.

#### `TelaTeste`
Tela gráfica onde o usuário preenche suas competências e visualiza as sugestões de carreira.

#### `TelaFaculdades`
Mostra áreas de estudo e cursos considerados relevantes para o futuro.

#### `HomeApp`
Tela inicial responsável pela navegação entre as demais interfaces.

---

## Demonstração

A seguir estão **Abaixo estão três exemplos que ilustram o funcionamento da aplicação.**.  

---

### 1. Demonstração – Caso 1: Sugestões de Carreira (Perfil A)

Perfil com foco em competências analíticas e de raciocínio lógico.

 
![Image](https://github.com/user-attachments/assets/6e238636-4016-4659-9eac-4bf17b1fe993)

---

### 2. Demonstração – Caso 2: Sugestões de Carreira (Perfil B)

Perfil com competências focadas em comunicação e liderança.

 
![Image](https://github.com/user-attachments/assets/b856e405-d858-496f-876d-a526f7d957b0)

---

### 3. Demonstração – Faculdades Recomendadas
 
Demonstração da tela que apresenta áreas de estudo promissoras e os cursos correspondentes.


![Image](https://github.com/user-attachments/assets/e6d50201-2064-496d-ab1d-f84050612fd0)

---
