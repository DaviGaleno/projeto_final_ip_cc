
# Dicionário Interativo de Python com Integração Gemini

Este projeto é um site educacional desenvolvido com **Flask** que atua como um dicionário interativo de conceitos em Python. Ele também oferece integração com a API **Gemini** da Google para responder dúvidas dos usuários de forma contextual.

## Estrutura do Site

O site possui várias seções, cada uma explicando diferentes temas da linguagem Python:

- `/` – Página inicial
- `/vetoresematrizes` – Conceitos de vetores e matrizes
- `/estruturasdeseleção` – Estruturas de seleção (condicionais)
- `/funcoeseprocedimentos` – Funções e procedimentos em Python
- `/tratamento` – Tratamento de erros e exceções
- `/estruturasderepetição` – Estruturas de repetição (loops)
- `/dicionario` – Página para visualizar termos e definições
- `/novo_termo`, `/editar_termo` – Páginas para adicionar ou editar termos (funcionalidade CRUD)

## Tecnologias Utilizadas

- **Python 3**
- **Flask** – Framework web leve
- **HTML/CSS** – Estrutura e estilização das páginas
- **JavaScript (fetch API)** – Comunicação assíncrona com o backend
- **Google Generative AI (Gemini API)** – Integração com modelo LLM
- **dotenv** – Para gestão de variáveis de ambiente
- **CSV** – Usado como banco de dados leve para o dicionário

## Integração com a API Gemini

A integração com o modelo de IA generativa **Gemini 2.0 Flash** é feita via biblioteca `google.generativeai`. O chatbot é ativado via a rota `/chat`, que recebe uma mensagem do usuário e retorna uma resposta gerada pela IA com base em instruções como:

```python
model = genai.GenerativeModel("gemini-2.0-flash")
response = model.generate_content([
    "Você é um professor de python que tira dúvidas sobre assuntos de python, dando respostas curtas e diretas.",
    user_input
])
```

A chave da API é carregada usando a biblioteca `dotenv` e a variável de ambiente `GOOGLE_API_KEY`.

## Como Executar a Aplicação Localmente

1. **Clone o repositório:**

```bash
git clone <url-do-repo>
```

2. **Crie e ative um ambiente virtual (opcional mas recomendado):**

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

3. **Instale as dependências:**

```bash
pip install flask python-dotenv google-generativeai
```

4. **Configure a variável de ambiente da chave da API do Gemini:**

Altere o comando a abaixo trocando "sua_chave_aqui" para a sua chave da API.

```
genai.configure(api_key="sua_chave_aqui")
```

5. **Execute a aplicação:**

```bash
flask run
```

Acesse no navegador: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Principais Partes do Código Python

- **`app.py`**: Define as rotas, lógica de renderização de páginas e integração com o Gemini.
- **`bd_dicionario.csv`**: Banco de dados leve onde os termos e definições são armazenados.
- **Templates HTML**: Localizados em `/templates`, cada um representa uma página do site.
- **Arquivos estáticos**: Localizados em `/static`, contendo imagens ilustrativas e ícones.

---

### Desenvolvido para fins educacionais

Este projeto tem como objetivo auxiliar no aprendizado da linguagem Python de forma visual e interativa. A integração com IA torna o aprendizado mais dinâmico, simulando um tutor virtual.
