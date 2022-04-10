from .imports import *
from . import words


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    encrypted_password = Column(String(255), nullable=False)
    token = Column(String(255), unique=True, nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    words = relationship("Words")