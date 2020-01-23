import os

try:
    API_KEY = os.environ['API_KEY']
except KeyError:
    raise Exception('Missing API_KEY environment variable.')

try:
    GOOGLE_CLIENT_ID = os.environ['GOOGLE_CLIENT_ID']
except KeyError:
    raise Exception('Missing GOOGLE_CLIENT_ID environment variable.')

try:
    GOOGLE_CLIENT_SECRET = os.environ['GOOGLE_CLIENT_SECRET']
except KeyError:
    raise Exception('Missing GOOGLE_CLIENT_SECRET environment variable.')

GOOGLE_DISCOVERY_URL = (
    'https://accounts.google.com/.well-known/openid-configuration'
)
