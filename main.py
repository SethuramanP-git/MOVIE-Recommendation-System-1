import streamlit as st
import pandas as pd
import requests
import pickle
import numpy as np
import warnings
warnings.filterwarnings("ignore")

with open('movie_data.pkl', 'rb') as file:
    temp, cosine = pickle.load(file)  


def get_movies(name, cosine=cosine):
    idx=temp[temp["title"]==name].index[0]
    cosine_score=list(enumerate(cosine[idx])) ##
    cosine_score=sorted(cosine_score,key=lambda x:x[1],reverse=True)
    cosine_score=cosine_score[0:10]
    moviesidex=[i[0] for i in cosine_score]
    return temp[["movie_id","title"]].iloc[moviesidex]


import requests

def fetch_poster(movie_id):
    api_key={api_key0}
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    response = requests.get(url)
    data = response.json()
    poster_path = data['poster_path']
    full_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
    return full_path  
     
st.header("Personalized Content Recommendation System 🔍")
st.title("Movie Recommendation System🎥")

select=st.selectbox("select the movie (total movies: 5000)",temp["title"].values)

st.sidebar.info(body="""

Summary: Movie Recommendation System
A Movie Recommendation System is a smart tool that suggests movies to users based on their interests. It works just like how Netflix or Amazon Prime shows you what to watch next.


1.Content-Based Filtering

Suggests movies similar to what a user liked before.

It looks at movie details like genre, actors, director, etc.


2.Collaborative Filtering

Recommends movies based on what similar users liked.

It doesn’t focus on movie details but on user preferences.


3.Combines both content-based and collaborative methods for better results.


These systems often use machine learning, user ratings, and big data to personalize recommendation.




""", icon="📃")

if st.button('Recommend'):
    recommendations = get_movies(select)
    st.write("Top 10 recommended movies:")

    with st.spinner("ROLLING...🎞️"):
        for i in range(0,20,5):
            cols=st.columns(5)
            for col ,j in zip(cols,range(i,i+5)):
                if j < len(recommendations):
                    movie_title=recommendations.iloc[j]["title"]
                    movie_id=recommendations.iloc[j]["movie_id"]

                    poster=fetch_poster(movie_id)
                    with col:
                        if poster:
                            st.image(poster,width=130)
                        st.write(movie_title)
      

