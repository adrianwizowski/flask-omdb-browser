# Flash OMDB Browser
Simple website that allows searching movie database provided by http://www.omdbapi.com/​ .

## Local development
Environment variables should be stored in `.env` file in main project directory.

`API_KEY` can be obtain here: http://www.omdbapi.com/apikey.aspx
It's needed to make OMDB API calls.

Also, `FLASK_APP` variable should be set in `.env` file, ex:

    FLASK_APP=flask_app/app
    
### Helpful Makefile commands:

    make run - runs app locally
    make test - runs tests locally
    make docker - runs dockerized app
    make lint - runs pylint on flask_app dir
