from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


def __get_database_connection_data__():
    return 'postgresql://{0}:{1}@{2}/{3}'.format(
        os.environ.get('DATABASE_USERNAME'),
        os.environ.get('DATABASE_USERNAME'),
        os.environ.get('DATABASE_HOST'),
        os.environ.get('POSTGRESQL_DATABASE'))


class DataAccessBoard:
    def __init__(self):
        connection_string = __get_database_connection_data__()
        engine = create_engine(connection_string)
        session = sessionmaker(bind=engine)
        self.__session__ = session()

    def save_board(self, board_db):
        self.__session__.add(board_db)
        return board_db.id

    def finish_session(self):
        self.__session__.close()

    def rollback(self):
        self.__session__.rollback()

    def commit(self):
        self.__session__.commit()
