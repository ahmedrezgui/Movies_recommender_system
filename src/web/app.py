import pickle
import streamlit as st
import requests
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('TMDB_API_KEY')

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(movie_id, api_key)
    data = requests.get(url)
    data = data.json()
    try:
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    except KeyError:
        return "https://upload.wikimedia.org/wikipedia/en/6/60/No_Picture.jpg"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
movies = pickle.load(open('../model/movie_list.pkl','rb'))
similarity = pickle.load(open('../model/similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    title1, title2, title3, title4, title5 = st.columns(5, gap="small", vertical_alignment="bottom")
    col1, col2, col3, col4, col5 = st.columns(5, gap="small", vertical_alignment="center")

    title1.text(recommended_movie_names[0])
    col1.image(recommended_movie_posters[0])

    title2.text(recommended_movie_names[1])
    col2.image(recommended_movie_posters[1])


    title3.text(recommended_movie_names[2])
    col3.image(recommended_movie_posters[2])

    title4.text(recommended_movie_names[3])
    col4.image(recommended_movie_posters[3])

    title5.text(recommended_movie_names[4])
    col5.image(recommended_movie_posters[4])