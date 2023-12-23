from functools import wraps

from flask import request
from sqlalchemy import text

from utils.db_helper import DBHelper

db_instance = DBHelper()


def check_auth(username, password):
    try:
        with db_instance.session_scope() as db_session:
            cur = db_session.execute('SELECT * FROM users WHERE username=?', (username,))
            # Usually I would introduce some sqlalchemy
            # with bindparams to avoid sql injection
            user = cur.fetchone()
            return user is not None and user['password'] == password
    except Exception as e:
        return False


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return 'Unauthorized', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'}
        return f(*args, **kwargs)
    return decorated_function

