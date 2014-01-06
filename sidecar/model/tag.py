from sqlalchemy import Column, types

from .base import Base


class Tag(Base):
    __tablename__ = 'tags'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    id = Column(types.Integer, primary_key=True)
    name = Column(types.Unicode(255), nullable=False)
