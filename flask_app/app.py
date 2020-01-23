import json

import requests
from flask import request, redirect, url_for
from flask_login import current_user, login_user, login_required, logout_user

from flask_app import app, omdb_client, login_manager, oauth_client, GOOGLE_CLIENT_ID
from flask_app.config import GOOGLE_CLIENT_SECRET, GOOGLE_DISCOVERY_URL
from flask_app.user import User


# Flask-Login helper to retrieve a user from our db
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route("/")
def index():
    if current_user.is_authenticated:
        return (
            "<p>Hello, {}! You're logged in! Email: {}</p>"
            "<div><p>Google Profile Picture:</p>"
            '<img src="{}" alt="Google profile pic"></img></div>'
            '<a class="button" href="/logout">Logout</a>'.format(
                current_user.name, current_user.email, current_user.profile_pic
            )
        )
    else:
        return '<a class="button" href="/login">Google Login</a>'


@app.route("/login")
def login():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = oauth_client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)


@app.route("/login/callback")
def callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    # Find out what URL to hit to get tokens that allow you to ask for
    # things on behalf of a user
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send request to get tokens! Yay tokens!
    token_url, headers, body = oauth_client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code,
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens!
    oauth_client.parse_request_body_response(json.dumps(token_response.json()))

    # Now that we have tokens (yay) let's find and hit URL
    # from Google that gives you user's profile information,
    # including their Google Profile Image and Email
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = oauth_client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # We want to make sure their email is verified.
    # The user authenticated with Google, authorized our
    # app, and now we've verified their email through Google!
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400

    # Create a user in our db with the information provided
    # by Google
    user = User(
        id_=unique_id, name=users_name, email=users_email, profile_pic=picture
    )

    # Doesn't exist? Add to database
    if not User.get(unique_id):
        User.create(unique_id, users_name, users_email, picture)

    # Begin user session by logging the user in
    login_user(user)

    # Send user back to homepage
    return redirect(url_for("index"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()


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
    if current_user.is_authenticated:
        if request.args.get('title'):
            return omdb_client.get(
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
    return '<a class="button" href="/login">Google Login</a>'
