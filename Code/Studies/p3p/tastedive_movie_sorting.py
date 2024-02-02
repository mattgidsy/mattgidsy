import requests_with_caching
import json

#returns a dictionary of similar movies
def get_movies_from_tastedive(query)->dict:
    parameters = {'q':query , 'type': 'movies' , 'limit':5}
    response = requests_with_caching.get('https://tastedive.com/api/similar', params=parameters)
    res_data = json.loads(response.text)
    return res_data

#filters the movie titles from the dict of similar movies
def extract_movie_titles(res_data:dict)->list:
    movie_titles = [data['Name'] for data in res_data['Similar']['Results']]

    return movie_titles

def get_related_titles(movie_titles=list)->list:
    movie_list = []
    for movie in movie_titles:
        similar_movies = extract_movie_titles(get_movies_from_tastedive(movie))
        for movie in similar_movies:
            if movie not in movie_list:
                movie_list.append(movie)
    return movie_list

def get_movie_data(query=str)->dict:
    parameters = {'t':query , 'r':'json'}
    response = requests_with_caching.get('http://www.omdbapi.com/', params=parameters)
    res_data = json.loads(response.text)
    return res_data

def get_movie_rating(res_data)->int:
    for data in res_data['Ratings']:
        if 'Rotten Tomatoes' in data['Source']:
            rt_rating = int(data['Value'][:2])
            return(rt_rating)
    return 0
def get_sorted_recommendations(movie_titles):
    related_movies = get_related_titles(movie_titles)
    movies_with_rating = [(movie, get_movie_rating(get_movie_data(movie))) for movie in related_movies]

    # Sorting the movies by rating in descending order, and then by title in reverse alphabetical order for ties
    sorted_movies = sorted(movies_with_rating, key=lambda x: (x[1], x[0]), reverse=True)

    # Extracting just the movie titles
    sorted_movie_titles = [movie[0] for movie in sorted_movies]

    return sorted_movie_titles


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
#get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

