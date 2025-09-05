import requests
import pandas as pd
import os 
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("TMDB_API_KEY")
print(f"DEBUG: Chave da API carregada:{api_key}")
base_url = "https://api.themoviedb.org/3"

def discover_all_movies():
    movie_ids = []
    page = 1

    while True:
        url = (
            f"{base_url}/discover/movie?"
            f"api_key={api_key}"
            f"&language=pt-BR"
            f"&release_date.gte=2015-01-01"
            f"&vote_count.gte=500"
            f"&sort_by=vote_average.desc"
            f"&page={page}"
        )

        response = requests.get(url).json()

        results = response.get('results', [])
        if not results:
            break

        for movie in results:
            movie_ids.append(movie.get('id'))

        total_pages = response.get('total_pages')
        if page >= total_pages:
            break

        page += 1

    unique_movie_ids = list(set(movie_ids))
    print(f"Total de IDs únicos coletados: {len(unique_movie_ids)}")
    return unique_movie_ids

def get_movie_details(movie_id):
    url = f'{base_url}/movie/{movie_id}?api_key={api_key}&language=pt-BR&append_to_response=release_dates,credits'
    response = requests.get(url).json()

    movie_info = {
        'ID do Filme': movie_id,
        'Nome do Filme': None,
        'Gênero': None,
        'Avaliação': None,
        'Nº de Avaliações': None,
        'Lançamento': None,
        'Nacionalidade': None,
        'Duração': None,
        'Popularidade': None,
        'Orçamento': None,
        'Receita': None,
        'Atores Principais': None
    }

    try:
        movie_info['Nome do Filme'] = response.get('title')
        movie_info['Gênero'] = ', '.join([g['name'] for g in response.get('genres', [])])
        movie_info['Avaliação'] = response.get('vote_average')
        movie_info['Nº de Avaliações'] = response.get('vote_count')
        movie_info['Lançamento'] = response.get('release_date')
        movie_info['Nacionalidade'] = ', '.join([c['name'] for c in response.get('production_countries', [])])
        movie_info['Duração'] = response.get('runtime')
        movie_info['Popularidade'] = response.get('popularity')
        movie_info['Orçamento'] = response.get('budget')
        movie_info['Receita'] = response.get('revenue')

        cast = response.get('credits', {}).get('cast', [])
        movie_info['Atores Principais'] = ', '.join([actor['name'] for actor in cast[:3]])

        return movie_info
    except Exception as e:
        print(f'Erro ao processar campos do filme {movie_id}: {e}')
        return movie_info