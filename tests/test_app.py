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


def test_omdb_search_searies_season(test_client):
    response = test_client.get('/search?title="How I Met Your Mother"&season=5')
    assert response.status == '200 OK'
    assert response.json == {
        "actors": "Josh Radnor, Jason Segel, Cobie Smulders, Neil Patrick Harris",
        "awards": "Nominated for 2 Golden Globes. Another 25 wins & 91 nominations.",
        "country": "USA", "director": "N/A", "genre": "Comedy, Romance", "imdb_id": "tt0460649",
        "imdb_rating": "8.3", "imdb_votes": "561,014", "language": "English, Persian, Chinese",
        "metascore": "N/A",
        "plot": "A father recounts to his children, through a series of flashbacks, the journey he and his four best "
                "friends took leading up to him meeting their mother.",
        "poster": "https://m.media-amazon.com/images/M/MV5BZWJjMDEzZjUtYWE1Yy00M2ZiLThlMmItODljNTAzODFiMzc2XkEyXkFqcGde"
                  "QXVyNTA4NzY1MzY@._V1_SX300.jpg",
        "rated": "TV-14", "ratings": [{"source": "Internet Movie Database", "value": "8.3/10"}],
        "released": "19 Sep 2005", "response": "True", "runtime": "22 min",
        "title": "How I Met Your Mother", "total_seasons": "9", "type": "series",
        "writer": "Carter Bays, Craig Thomas", "year": "2005\u20132014"
    }
