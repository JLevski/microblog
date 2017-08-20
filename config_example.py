# rename this as config.py and add your password details to make it work

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


WTF_CSRF_ENABLED = True
SECRET_KEY = 'example'

app.config['OAUTH_CREDENTIALS'] = {
    'facebook': {
        'id': 'example',
        'secret': 'example'
    }
}
