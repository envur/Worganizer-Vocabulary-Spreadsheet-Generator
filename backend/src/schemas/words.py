from .imports import *


class WordBase(BaseModel):
    word: str
    language: str
    category: str
    translation: Optional[str] = None
    description: Optional[str] = None

class Word(WordBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True

class WordUpdate(BaseModel):
    id: int
    word: Optional[str] = None
    language: Optional[str] = None
    category: Optional[str] = None
    translation: Optional[str] = None
    description: Optional[str] = None

class WordsListResponse(BaseModel):
    words: List[Word]
    total_words: int

class WordFilter(BaseModel):
    user_id: int
    id: Optional[int] = None
    word_equal: Optional[str] = None
    word_like: Optional[str] = None
    language_equal: Optional[str] = None
    language_like: Optional[str] = None
    translation_equal: Optional[str] = None
    translation_like: Optional[str] = None
    description_equal: Optional[str] = None
    description_like: Optional[str] = None
    category: Optional[str] = None
    created_at_min: Optional[datetime] = None
    created_at_max: Optional[datetime] = None
    updated_at_min: Optional[datetime] = None
    updated_at_max: Optional[datetime] = None
    skip: Optional[int] = None
    limit: Optional[int] = None
    sort: Optional[str] = None
    order: Optional[bool] = None