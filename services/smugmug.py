import flask
import foauth.providers


class SmugMug(foauth.providers.OAuth1):
    # General info about the provider
    provider_url = 'http://smugmug.com/'
    favicon_url = 'http://smugmug.com/favicon.ico'
    docs_url = 'http://wiki.smugmug.net/display/API/API+1.3.0'

    # URLs to interact with the API
    request_token_url = 'http://api.smugmug.com/services/oauth/getRequestToken.mg'
    authorize_url = 'http://api.smugmug.com/services/oauth/authorize.mg?Access=Full&Permissions=Modify'
    access_token_url = 'http://api.smugmug.com/services/oauth/getAccessToken.mg'
    api_domain = 'api.smugmug.com'

    available_permissions = [
        (None, 'read and write your photos'),
    ]
