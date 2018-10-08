from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, BigInteger, DateTime, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class BoardDatabase(Base):
    __tablename__ = 'board'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    size = Column(Integer)
    dt_created = Column(DateTime)
    queen_positions = relationship('QueenPosition')

    def __repr__(self):
        return f'<board(id={self.id}, size={self.size},' \
               f' time={self.time_to_find_solution}, ' \
               f' dt_created={self.dt_created}) '


class QueenPosition(Base):
    __tablename__ = 'queen_position'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    row = Column(Integer)
    col = Column(Integer)
    board_id = Column(BigInteger, ForeignKey('board.id'))

    def __repr__(self):
        return f'<queen_position(id={self.id}, row={self.row},' \
               f' column={self.col}, ' \
               f' board_id={self.board_id}) '
