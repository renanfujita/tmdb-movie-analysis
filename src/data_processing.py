# Em: src/data_processing.py

import pandas as pd

def process_main_movie_data(df_raw):
    """
    Recebe o DataFrame bruto da API e aplica toda a limpeza, 
    transformação E FILTRAGEM para criar a tabela de análise principal.
    """
    # 1. Copia o DataFrame para evitar modificar o original
    df = df_raw.copy()

    # 2. Ordena e reseta o index
    df = df.sort_values(by='Avaliação', ascending=False)
    df.reset_index(drop=True, inplace=True)

    # 3. Converte a coluna de Lançamento para datetime, tratando erros
    df['Lançamento'] = pd.to_datetime(df['Lançamento'], errors='coerce')

    # 4. Preenche valores nulos em colunas de texto
    df['Nacionalidade'] = df['Nacionalidade'].fillna('Não informado')
    df['Atores Principais'] = df['Atores Principais'].fillna('Não informado')

    # 5. Substitui zeros que deveriam ser nulos
    df['Orçamento'] = df['Orçamento'].replace(0, pd.NA)
    df['Receita'] = df['Receita'].replace(0, pd.NA)

    # 6. Cria a coluna de Receita Líquida
    df['Receita Líquida'] = df['Receita'] - df['Orçamento']

    # 7. Arredonda a avaliação
    df['Avaliação'] = df['Avaliação'].round(1)
    
    # 8. Filtra o DataFrame para manter apenas os filmes válidos;
    # Mantém apenas filmes com data de lançamento válida E a partir de 2015
    df_filtrado = df.dropna(subset=['Lançamento'])
    df_filtrado = df_filtrado[df_filtrado['Lançamento'].dt.year >= 2015].copy()

    print(f"Processamento concluído. DataFrame final com {len(df_filtrado)} filmes.")
    return df_filtrado


def create_genre_dataset(df_cleaned):
    """
    Recebe o DataFrame já limpo e cria uma nova tabela explodida por gênero.
    """
    df = df_cleaned.copy()
    
    # Garante que a coluna Gênero é do tipo string
    df['Gênero'] = df['Gênero'].astype(str)
    
    # Separa os gêneros que estão em uma única string
    df['Gênero'] = df['Gênero'].str.split(',')
    
    # "Explode" o DataFrame, criando uma linha para cada gênero de um filme
    df_genre = df.explode('Gênero')
    
    # Limpa os espaços em branco e substitui valores vazios
    df_genre['Gênero'] = df_genre['Gênero'].str.strip()
    df_genre['Gênero'] = df_genre['Gênero'].replace('', 'Sem Gênero')

    print("Criação do DataFrame de gêneros concluída.")
    return df_genre