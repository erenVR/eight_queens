from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, BigInteger, ForeignKey
from sqlalchemy.orm import relationship


class QueenPosition(declarative_base()):
    __tablename__ = 'queen_position'

    queen_position_id = Column(BigInteger, primary_key=True, autoincrement=True)
    row = Column(Integer)
    column = Column(Integer)
    board_id = Column(BigInteger, ForeignKey('board_id'))

    board = relationship('Board', back_populates='queen_position')

    def __repr__(self):
        return f'<queen_position(id={self.queen_position_id}, row={self.row},' \
               f' column={self.column}, ' \
               f' board_id={self.board_id}) '
