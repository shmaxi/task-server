import sqlite3

from sqlalchemy.util.compat import contextmanager

from api.v1 import CURRENT_CONFIG


session = None


class DBHelper:
    def __init__(self):
        global session

        if not session:
            db = self.__get_db_connection()
            with open('utils/schema.sql', mode='r') as f:
                db.cursor().executescript(f.read())
            db.commit()
            session = db
            db.close()

    @staticmethod
    def __get_db_connection():
        db = sqlite3.connect(CURRENT_CONFIG.DATABASE, check_same_thread=False)
        db.row_factory = sqlite3.Row
        return db

    @staticmethod
    def __is_connection_open(connection):
        try:
            connection.cursor()
            return True
        except Exception as ex:
            return False

    # Connect to the database
    @contextmanager
    def session_scope(self):
        global session

        if not self.__is_connection_open(session):
            session = self.__get_db_connection()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

