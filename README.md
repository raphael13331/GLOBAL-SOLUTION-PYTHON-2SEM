(https://github.com/user-attachments/files/23607849/README.md)
# Orientador de Carreiras do Futuro


Este projeto consiste em uma aplicação interativa desenvolvida em Python com Tkinter, capaz de analisar competências pessoais e recomendar carreiras promissoras para o futuro.  
O sistema também apresenta uma tela dedicada a **faculdades recomendadas**, alinhadas às áreas tecnológicas e emergentes.

O objetivo é fornecer uma ferramenta simples, visual e intuitiva que ajude estudantes e profissionais a descobrirem possíveis caminhos profissionais com base em habilidades individuais.

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


### Classes Principais

#### `Perfil`
Representa o usuário avaliado, armazenando nome e competências.  
Métodos:
- `media()` → calcula a média das competências.

#### `Orientador`
Processa o conjunto de competências para gerar afinidade com carreiras do futuro.  
Métodos:
- `recomendar(perfil)` → retorna as três principais recomendações.

#### `TelaTeste`
Interface gráfica para preenchimento das competências e exibição das carreiras sugeridas.

#### `TelaFaculdades`
Exibe áreas de estudo e cursos promissores para o futuro.

#### `HomeApp`
Tela inicial e central de navegação da aplicação.

---

## Demonstração

A seguir estão **três áreas reservadas para demonstrar o funcionamento do projeto**.  

---

### 1. Demonstração – Caso 1: Recomendações de Carreira (Perfil A)

Perfil com competências focadas em lógica e análise.

 
![Image](https://github.com/user-attachments/assets/fc1eb116-5292-421c-9d51-534233da4ac4)

---

### 2. Demonstração – Caso 2: Recomendações de Carreira (Perfil B)

Perfil com competências focadas em comunicação e liderança.

 
![Image](https://github.com/user-attachments/assets/b856e405-d858-496f-876d-a526f7d957b0)

---

### 3. Demonstração – Faculdades Recomendadas
 
Print da tela exibindo as áreas promissoras e cursos recomendados.


![Image](https://github.com/user-attachments/assets/e6d50201-2064-496d-ab1d-f84050612fd0)

---
