#Importo librerias 
from fastapi import FastAPI, HTTPException
import pandas as pd
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional
import asyncio

#Creo una instancia de FastAPI
app = FastAPI()

#---- PRESENTACIÓN--------

@app.get("/")
def bienvenida():
    return "Bievenidos a esta PI_ML_OPS, aqui podrán encontrar películas y series de distintas plataformas de streaming."

@app.get("/menu")
def menu():
    return "Las funciones que encontrará son las siguientes:                                                         " \
           "                                                                                                          \
        (1) get_max_duration donde necesitarás los siguientes parámetros: '/get_max_duration/{year}/{platform}/{durat" \
           "ion_type}'                                                                                                 \
        (2) get_score_count donde necesitarás los siguientes parámetros: '/get_score_count/{platform}/{scored}/{relea" \
           "se_year}'                                                                                                  \
        (3) get_count_platform donde necesitarás los siguientes parámetros: '/get_count_platform/{platform}'         " \
           "                                                                                                           \
        (4) get_actor donde necesitarás los siguientes parámetros: '/get_actor/{platform}/{year}'                    " \
           "                                                                                                         " \
           "year: int. platform: netflix, hulu, amazon prime, disney plus. duration: min, seasons. scored: int. relea" \
           "se_year: int. "


# Primer consulta: Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN.
@app.get("/get_max_duration/{year}/{platform}/{duration_type}")
def get_max_duration(year: Optional[int] = None, platform: Optional[str] = None, duration_type: Optional[str] = None):
    df_duration = pd.read_csv('ETLcsvResults\\the_movies.csv')
    if year:
        df_duration = df_duration[(df_duration['release_year'] == year)]
                                  # & (df_duration['type'] == 'movie')]
    if platform:
        df_duration = df_duration[(df_duration['platform'] == platform)]
                                  # & (df_duration['type'] == 'movie')]
    if duration_type:
        df_duration = df_duration[(df_duration['duration_type'] == duration_type)]
                                  # & (df_duration['type'] == 'movie')]

    max_duration = df_duration['duration_type'].max()
    movie_title = df_duration[df_duration['duration_type'] == max_duration]['title'].iloc[0]

    return {f'{movie_title}.'}


# Segunda consulta: Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
@app.get("/get_score_count/{platform}/{score}/{release_year}")
def get_score_count(platform, score, release_year):
    platform = str(platform)
    score = float(score)
    year = int(release_year)
    movies = pd.read_csv('ETLcsvResults\\the_movies.csv')

    filtered_movies = movies[
        (movies['platform'] == platform) & (movies['release_year'] == year) & (movies['score'] > score)
        & (movies['type'] == 'movie')]
    count = (filtered_movies.groupby('platform').size()).to_dict()
    return count


# Tercera consulta: Cantidad de películas por plataforma con filtro de PLATAFORMA.
@app.get("/get_count_platform/{platform}")
def get_count_platform(platform):
    df_total_ratings = pd.read_csv('ETLcsvResults\\the_movies.csv')
    count_platform = df_total_ratings.loc[(df_total_ratings["platform"] == platform) &
                                          (df_total_ratings["type"] == "movie"), "type"].value_counts()["movie"]
    
    return f'{count_platform}.'


# Cuarta consulta: Actor que más se repite según plataforma y año.
@app.get("/get_actor/{platform}/{year}")
def get_actor(platform: str, year: int):
    df_actors = pd.read_csv('ETLcsvResults\\the_actors.csv')
    data = df_actors[(df_actors['year'] == year) & (df_actors['platform']==platform)]['actor']
    # return {data.value_counts().max()}
    if data.value_counts().index[0] == 'sin dato':
        actor = data.value_counts().index[1]
        times = data.value_counts()[1]
        return f'{actor}, {times}.'
    elif data.value_counts().index[0] != 'sin dato':
        actor = data.value_counts().index[0]
        times = data.value_counts()[0]
        return f'{actor}, {times}.'


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
     