"""Base application module."""
import os

from flask import Flask, request
import omdb

app = Flask(__name__)

try:
    client = omdb.OMDBClient(apikey=os.environ['API_KEY'])
except KeyError:
    raise Exception("Missing API_KEY environment variable.")


@app.route('/search')
def omdb_search():
    """
    Basic OMDB search view.

    All search parameters should be passed by query params.
    title - Title of media to search for. (required) Titles should be passed in quotation marks,
        ex: title="How I Met Your Mother"
    year - Year of media. (optional)
    media_type - Media type to return. (one of movie, episode, or series, optional)
    imdbid - IMDb media ID. (optional)
    page - Page to return. (optional)
    fullplot - Include extended plot. Short plot will be returned as default. (optional)
    tomatoes - Add Rotten Tomatoes data to response. (optional)
    season - Number of season to return. (optional)
    episode - Number of episode to return. (optional)
    timeout - Timeout in seconds. (optional)
    """
    if request.args.get('title'):
        return client.get(
            title=request.args.get('title'),
            year=request.args.get('year'),
            media_type=request.args.get('type'),
            imdbid=request.args.get('imdbid'),
            page=request.args.get('page', 1),
            fullplot=request.args.get('fullplot'),
            tomatoes=request.args.get('tomatoes'),
            season=request.args.get('seasons'),
            episode=request.args.get('episode'),
            timeout=request.args.get('timeout')
        )

    return "Missing title", 400
