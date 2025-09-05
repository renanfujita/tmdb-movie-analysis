# 🎬 Pipeline de Dados e Análise de Filmes do TMDB

## 📖 Descrição do Projeto

Este projeto demonstra a construção de um pipeline de dados completo, desde a coleta via API até a preparação de um dataset limpo para análise. Utilizando a API oficial do The Movie Database (TMDB), o processo extrai, trata e enriquece informações de filmes populares lançados a partir de 2015 e com, pelo menos, 500 avaliações.

O objetivo final é gerar dois datasets estruturados para a criação de dashboards e análises visuais no Power BI. 

## 📊 Dashboard de Análise no Power BI

*O dashboard interativo para este projeto está atualmente em fase de desenvolvimento e o link para a versão publicada será adicionado aqui em breve.*

## 🛠️ Ferramentas e Tecnologias

- **Python:** Linguagem principal para a coleta e o processamento dos dados.
- **Pandas:** Biblioteca utilizada para a manipulação, limpeza e transformação dos dados em DataFrames.
- **Requests:** Biblioteca para realizar as chamadas à API do TMDB de forma eficiente.
- **python-dotenv:** Para o gerenciamento seguro da chave de API, evitando a exposição de credenciais no código.
- **VS Code:** Ambiente de Desenvolvimento Integrado (IDE) para a construção do projeto.
- **Jupyter Notebook:** Utilizado para a orquestração do pipeline de processamento e para a validação dos dados.
- **Git & GitHub:** Para versionamento de código e publicação do portfólio.
- **Power BI:** Ferramenta de Business Intelligence utilizada para a criação do dashboard e visualização final dos dados.

## ⚙️ Como Executar o Projeto

Siga os passos abaixo para recriar o ambiente e executar o pipeline de dados em sua máquina local.

1.  **Clonar o repositório:**

    Primeiro, clone este repositório para sua máquina.
    ```bash
    git clone [https://github.com/renanfujita/tmdb-movie-analysis.git](https://github.com/renanfujita/tmdb-movie-analysis.git)
    cd tmdb-movie-analysis
    ```

2.  **Criar o arquivo de ambiente (.env):**

    Na pasta raiz do projeto, crie o arquivo .env para armazenar sua chave de API de forma segura. Adicione o seguinte conteúdo a ele:
    ```
    TMDB_API_KEY="sua_chave_secreta_aqui"
    ```

3.  **Instalar as dependências:**

    Este projeto utiliza um arquivo `requirements.txt` para gerenciar as bibliotecas necessárias.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Executar o pipeline de coleta de dados:**

    Este script irá buscar os dados da API do TMDB e salvá-los na pasta `data/raw/`.
    ```bash
    python get_data.py
    ```

5.  **Executar o notebook de processamento:**
    
    Abra o projeto no VS Code, navegue até a pasta `notebooks/` e execute todas as células do notebook `analise-tmdb.ipynb`. Ao final, os arquivos CSV limpos estarão na pasta `data/processed/`.

## 👨‍💻 Autor

Projeto desenvolvido por **Renan Fujita**

Linkedin: www.linkedin.com/in/renanyukifujita
