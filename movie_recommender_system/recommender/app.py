import streamlit as st
import pickle
import pandas as pd



with open('movies.pkl','rb') as f:
          movies = pickle.load(f)

movie_names = movies['title'].values
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'select your favourite movie',
    movie_names
)
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x : x[1])[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies




if st.button('Recommend'):
    #   st.write(selected_movie_name)
    recommendations  =  recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

