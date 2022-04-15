from .imports import *
from src.models import words as w_model
from src.schemas import words as w_schemas
from src.services import xlsx_generator
from sqlalchemy.sql.expression import asc, desc


def get_words(db: Session, search_filter: w_schemas.WordFilter):
    conditions = []
    limit = None
    sort = "id"
    skip = search_filter.skip
    order = desc

    conditions.append(w_model.Words.user_id == search_filter.user_id)
    
    if search_filter.id:
        conditions.append(w_model.Words.id == search_filter.id)

    if search_filter.word_equal:
        conditions.append(w_model.Words.word == search_filter.word_equal)

    if search_filter.word_like:
        conditions.append(w_model.Words.word.like(f'%{search_filter.word_like}%'))
    
    if search_filter.language_equal:
        conditions.append(w_model.Words.language == search_filter.language_equal)

    if search_filter.language_like:
        conditions.append(w_model.Words.language.like(f'%{search_filter.language_like}%'))
    
    if search_filter.translation_equal:
        conditions.append(w_model.Words.translation == search_filter.translation_equal)

    if search_filter.translation_like:
        conditions.append(w_model.Words.translation.like(f'%{search_filter.translation_like}%'))

    if search_filter.description_equal:
        conditions.append(w_model.Words.description == search_filter.description_equal)

    if search_filter.description_like:
        conditions.append(w_model.Words.description.like(f'%{search_filter.description_like}%'))

    if search_filter.category:
        conditions.append(w_model.Words.category == search_filter.category)

    if search_filter.created_at_min:
        conditions.append(w_model.Words.created_at >= search_filter.created_at_min)

    if search_filter.created_at_max:
        conditions.append(w_model.Words.created_at <= search_filter.created_at_max)

    if search_filter.updated_at_min:
        conditions.append(w_model.Words.updated_at >= search_filter.updated_at_min)

    if search_filter.updated_at_max:
        conditions.append(w_model.Words.updated_at <= search_filter.updated_at_max)

    if search_filter.limit:
        limit = int(filter.limit)

    if search_filter.order:
        order = asc

    if search_filter.sort and search_filter.sort in w_model.Words.__table__.columns:
        sort = search_filter.sort

    db_query = db.query(w_model.Words)
    for condition in conditions:
        db_query = db_query.filter(condition)

    db_total_words = db_query.count()
    db_query = db_query.order_by(order(sort))\
                            .limit(limit)\
                                .offset(skip)
                                
    return db_query.all(), db_total_words

def register_word(db: Session, word: w_schemas.Word, user_id: int):
    word_dict = word.dict()
    word_dict['created_at'] = datetime.today()
    word_dict['updated_at'] = datetime.today()
    word_dict['user_id'] = user_id
    db_word = w_model.Words(**word_dict)
    try:
        db.add(db_word)
        db.commit()
        db.refresh(db_word)
    except:
        raise exc.INTERNAL_ERROR_EXCEPTION

def update_word(db: Session, word: w_schemas.WordUpdate):
    db_word = update(w_model.Words)\
        .where(w_model.Words.id == word.id)\
            .values(**word.dict(exclude_unset = True), updated_at = datetime.today())
    try:
        db.execute(db_word)
        db.commit()
    except:
        raise exc.INTERNAL_ERROR_EXCEPTION

def delete_word(db: Session, word_id: int):
    db_word = db.query(w_model.Words)\
        .filter(w_model.Words.id == word_id)\
            .first()
    try:
        db.delete(db_word)
        db.commit()
    except:
        raise exc.INTERNAL_ERROR_EXCEPTION

def generate_words_xlsx(db: Session, search_filter: w_schemas.WordFilter):
    words = get_words(db, search_filter)
    xlsx_generator.xlsx_generator(words[0])
