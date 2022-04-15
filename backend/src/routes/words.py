from .imports import *
from src.cruds import words as w_cruds
from src.schemas import words as w_schemas
from src.schemas import status as s_schemas

# TODO: Change StatusModel for a response that returns the object data
@app.post("/words/list", tags=["Words"], response_model=w_schemas.WordsListResponse)
def list_words(search_filter: w_schemas.WordFilter = Body(..., embed=True), db: Session = Depends(get_db)):
    words, total_words = w_cruds.get_words(db, search_filter)
    return w_schemas.WordsListResponse(words=words, total_words=total_words)

@app.post("/words/xlsx", tags=["Words"])
def generate_words_xlsx_file(search_filter: w_schemas.WordFilter = Body(..., embed=True), db: Session = Depends(get_db)):
    w_cruds.generate_words_xlsx(db, search_filter)

@app.post("/word/register", tags=["Words"], response_model=s_schemas.StatusModel)
def register_word(user_id: int, word: w_schemas.WordBase = Body(..., embed=True), db: Session = Depends(get_db)):
    w_cruds.register_word(db, word, user_id)
    return s_schemas.StatusModel(message="Word successfully registered!")

@app.put("/word/update", tags=["Words"], response_model=s_schemas.StatusModel)
def update_user(word: w_schemas.WordUpdate = Body(..., embed=True), db: Session = Depends(get_db)):
    w_cruds.update_word(db, word)
    return s_schemas.StatusModel(message="Word successfully updated!")

@app.delete("/word/delete/{word_id}", tags=["Words"], response_model=s_schemas.StatusModel)
def delete_user(word_id: int, db: Session = Depends(get_db)):
    w_cruds.delete_word(db, word_id)
    return s_schemas.StatusModel(message="Word successfully deleted!")
