from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DataAccessObject:
    def __init__(self):
        engine = create_engine('')
        session = sessionmaker(bind=engine)
        self.__session__ = session()

    def save_board(self, board_db):
        self.__session__.add(board_db)
        self.__session__.commit()
        return board_db.id


