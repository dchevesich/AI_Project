import pandas as pd
import numpy as np # Necesario para algunas operaciones, Copilot lo sugiere si es útil
from sklearn.metrics.pairwise import cosine_similarity # Puede ser necesario si la lógica de similitud es más compleja

def recommend_movies(user_id, num_recommendations=5):
    # Esta funcion deberia cargar un dataset de ratings de peliculas
    # Por ejemplo, usar pandas para leer un CSV
    # Luego, deberia calcular la similitud entre usuarios o peliculas
    # Basado en la similitud, recomendar las peliculas no vistas por el usuario
    # Cargar el dataset de peliculas
    movies_df = pd.read_csv('movies.csv')  # Asegúrate de tener un archivo 'movies.csv' con los datos de las peliculas
    ratings_df = pd.read_csv('ratings.csv')  # Asegúrate de tener un archivo 'ratings.csv' con los ratings de los usuarios

    # Filtrar las peliculas que el usuario ya ha visto
    user_ratings = ratings_df[ratings_df['userId'] == user_id]
    seen_movies = user_ratings['movieId'].tolist()

    # Filtrar las peliculas no vistas por el usuario
    unseen_movies = movies_df[~movies_df['movieId'].isin(seen_movies)]

    # Calcular la media de ratings de las peliculas no vistas
    unseen_movies = unseen_movies.merge(ratings_df.groupby('movieId')['rating'].mean().
                                         reset_index(), on='movieId', how='left')
    unseen_movies = unseen_movies.rename(columns={'rating': 'average_rating'})

    # Ordenar las peliculas por la media de ratings
    recommendations = unseen_movies.sort_values(by='average_rating', ascending=False)

    # Devolver las mejores recomendaciones
    return recommendations.head(num_recommendations)[['movieId', 'title', 'average_rating']]