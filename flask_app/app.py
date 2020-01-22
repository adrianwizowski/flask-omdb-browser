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
    if request.args.get('title'):
        return client.get(
            title=request.args.get('title'),
            year=request.args.get('year', None),
            media_type=request.args.get('type', None),
            imdbid=request.args.get('imdbid', None),
            page=request.args.get('page', 1),
            fullplot=request.args.get('fullplot', None),
            tomatoes=request.args.get('tomatoes', None),
            season=request.args.get('seasons', None),
            episode=request.args.get('episode', None),
            timeout=request.args.get('timeout', None)
        )
    else:
        return "Missing title", 400
