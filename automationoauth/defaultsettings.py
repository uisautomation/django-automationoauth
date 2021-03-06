"""
Default settings values for the :py:mod:`automationoauth` application.

"""
# Variables whose names are in upper case and do not start with an underscore from this module are
# used as default settings for the lookupapi application. See AutomationOAuthConfig in .apps for
# how this is achieved. This is a bit mucky but, at the moment, Django does not have a standard way
# to specify default values for settings.  See: https://stackoverflow.com/questions/8428556/

OAUTH2_CLIENT_ID = None
"""
OAuth2 client id which the API server uses to identify itself to the OAuth2 token introspection
endpoint.

"""

OAUTH2_CLIENT_SECRET = None
"""
OAuth2 client secret which the API server uses to identify itself to the OAuth2 token introspection
endpoint.

"""

OAUTH2_TOKEN_URL = None
"""
URL of the OAuth2 token endpoint the API server uses to request an authorisation token to perform
OAuth2 token introspection.

"""

OAUTH2_INTROSPECT_URL = None
"""
URL of the OAuth2 token introspection endpoint. The API server will first identify itself to the
OAuth2 token endpoint and request an access token for this endpoint.

"""

OAUTH2_INTROSPECT_SCOPES = ['hydra.introspect'],
"""
List of OAuth2 scopes the API server will request for the token it will use with the token
introspection endpoint.

"""

OAUTH2_MAX_RETRIES = 5
"""
Maximum number of retries when fetching URLs from the OAuth2 endpoint or OAuth2 authenticated URLs.
This applies only to failed DNS lookups, socket connections and connection timeouts, never to
requests where data has made it to the server.

"""
