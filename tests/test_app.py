import pytest


def test_omdb_search(test_client):
    response = test_client.get('/search?title=Joker')
    assert response.status == '200 OK'
    assert response.json == {
        "actors": "Joaquin Phoenix, Robert De Niro, Zazie Beetz, Frances Conroy",
         "awards": "Won 2 Golden Globes. Another 27 wins & 129 nominations.", "box_office": "N/A",
         "country": "Canada, USA", "director": "Todd Phillips", "dvd": "17 Dec 2019",
         "genre": "Crime, Drama, Thriller", "imdb_id": "tt7286456", "imdb_rating": "8.6",
         "imdb_votes": "593,943", "language": "English", "metascore": "59",
         "plot": "In Gotham City, mentally troubled comedian Arthur Fleck is disregarded "
                 "and mistreated by society. He then embarks on a downward spiral of revolution and bloody crime. "
                 "This path brings him face-to-face with his alter-ego: the Joker.",
         "poster": "https://m.media-amazon.com/images/M/MV5BNGVjNWI4ZGUtNzE0MS00YTJmLWE0ZDctN2Zi"
                   "YTk2YmI3NTYyXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_SX300.jpg",
         "production": "Warner Bros. Pictures", "rated": "R",
         "ratings": [{"source": "Internet Movie Database", "value": "8.6/10"},
                     {"source": "Rotten Tomatoes", "value": "69%"},
                     {"source": "Metacritic", "value": "59/100"}], "released": "04 Oct 2019",
         "response": "True", "runtime": "122 min", "title": "Joker", "type": "movie",
         "website": "N/A",
         "writer": "Todd Phillips, Scott Silver, Bob Kane (based on characters created by), "
                   "Bill Finger (based on characters created by), "
                   "Jerry Robinson (based on characters created by)",
         "year": "2019"
        }


def test_omdb_without_title(test_client):
    response = test_client.get('/search')
    assert response.status == '400 BAD REQUEST'
    assert response.data == b'Missing title'
