import streamlit as st
import pickle
import pandas as pd
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

st.subheader("Machine Learning Project :movie_camera:")
def get_poster(movie_id):
     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=7ddf3a07ce8eca194db9bcc5637df7cb&language=en-US'.format(movie_id))
     data = response.json()
     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

animation = load_lottieurl("https://assets1.lottiefiles.com/private_files/lf30_bb9bkg1h.json")
def recc(movie):
     movie_index = movies[movies['title'] == movie].index[0]
     distances = similarity[movie_index]
     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

     recommended_movies = []
     recommended_movies_posters = []
     for i in movies_list:
          movie_id = movies.iloc[i[0]].movie_id

          recommended_movies.append(movies.iloc[i[0]].title)
          recommended_movies_posters.append(get_poster(movie_id))
     return recommended_movies,recommended_movies_posters

movies_list = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl','rb'))

with st.container():
     st.write("---")
     left, right = st.columns((1,2))
     with left:
          st.title('Movie Recommender System')

          selected_movie_name = st.selectbox(
               'Select Movie',
               movies['title'].values)

     with right:
          st_lottie(animation, width=900, height=300, key="Hello")

     if st.button('Recommend'):
          names, posters = recc(selected_movie_name)
          col1, col2, col3, col4, col5 = st.columns(5)

          with col1:
               st.text(names[0])
               st.image(posters[0])

          with col2:
               st.text(names[1])
               st.image(posters[1])

          with col3:
               st.text(names[2])
               st.image(posters[2])

          with col4:
               st.text(names[3])
               st.image(posters[3])

          with col5:
               st.text(names[4])
               st.image(posters[4])