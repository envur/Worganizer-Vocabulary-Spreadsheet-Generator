from .imports import *


class Words(Base):
    __tablename__ = 'words'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    word = Column(String(255), unique=False, nullable=False)
    language = Column(String(255), nullable=False)
    category = Column(String(255), nullable=False)
    translation = Column(String(255), nullable=True)
    description = Column(String(255), nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)