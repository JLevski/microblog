# rename this as config.py and add your password details to make it work

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
WHOOSH_BASE = os.path.join(basedir, 'search.db')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'example'

app.config['OAUTH_CREDENTIALS'] = {
    'facebook': {
        'id': 'example',
        'secret': 'example'
    },
    'twitter': {
        'id': 'example',
        'secret': 'example'
    }
}

# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['example@email.com']

# pagination
POSTS_PER_PAGE = 3
MAX_SEARCH_RESULTS = 50
