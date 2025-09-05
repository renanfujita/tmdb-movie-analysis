print("--- O SCRIPT get_data.py COMEÇOU A SER EXECUTADO ---")
# Em: get_data.py (na pasta raiz)

import os
import pandas as pd
from tqdm import tqdm
from src.api_handler import discover_all_movies, get_movie_details # <--- PASSO CHAVE 1

# --- CONFIGURAÇÃO ---
# Define onde os dados brutos serão salvos
OUTPUT_DIR = 'data/raw'
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'tmdb_movies_raw.csv')


# --- FUNÇÃO PRINCIPAL ---
def main():
    """
    Função principal que orquestra a busca e o salvamento dos dados.
    """
    # Garante que a pasta data/raw/ exista antes de salvar
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 1. Busca todos os IDs de filmes
    print("Iniciando busca de IDs de filmes na API...")
    movie_ids = discover_all_movies() # <--- PASSO CHAVE 2

    # 2. Busca os detalhes para cada ID
    all_movie_details = []
    if movie_ids:
        # A função tqdm cria uma barra de progresso no terminal
        for movie_id in tqdm(movie_ids, desc="Buscando detalhes dos filmes"):
            details = get_movie_details(movie_id) # <--- PASSO CHAVE 3
            if details:
                all_movie_details.append(details)

    # 3. Cria o DataFrame final e salva o arquivo .csv
    if all_movie_details:
        df = pd.DataFrame(all_movie_details)
        df.to_csv(OUTPUT_FILE, index=False)
        print(f"\nSUCESSO! {len(df)} filmes foram salvos em: {OUTPUT_FILE}")
    else:
        print("\nNenhum detalhe de filme foi coletado. O arquivo não foi criado.")


# --- PONTO DE ENTRADA DO SCRIPT ---
if __name__ == "__main__": # <--- PASSO CHAVE 4
    main()