from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, BigInteger, DECIMAL, DateTime


class BoardDatabase(declarative_base()):
    __table__ = 'board'

    board_id = Column(BigInteger, primary_key=True, autoincrement=True)
    size = Column(Integer)
    time_to_find_solution = Column(DECIMAL)
    dt_created = Column(DateTime)

    def __repr__(self):
        return f'<board(id={self.board_id}, size={self.size},'\
                f' time={self.time_to_find_solution}, '\
                f' dt_created={self.dt_created}) '