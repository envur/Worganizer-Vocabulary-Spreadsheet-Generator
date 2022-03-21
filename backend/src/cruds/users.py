from .imports import *
from src.models import users as u_model
from src.schemas import users as u_schemas


def get_user_by_id(db: Session, user_id: int):
    try:
        user = db.query(u_model.Users).filter(u_model.Users.id == user_id).first()
    except:
        raise exc.INTERNAL_ERROR_EXCEPTION
    if not user:
        raise exc.USER_ID_NOT_FOUND
    return user

def get_user_by_email(db: Session, email: str):
    try:
        user = db.query(u_model.Users).filter(u_model.Users.email == email).first()
    except:
        raise exc.INTERNAL_ERROR_EXCEPTION
    return user

def get_user_email_by_token(db: Session, token: str):
    try:
        user = db.query(u_model.Users).filter(u_model.Users.token == token).first()
    except:
        raise exc.INTERNAL_ERROR_EXCEPTION
    if not user:
        raise exc.INVALID_TOKEN
    return user

def register_user(db: Session, user: u_schemas.UserCreate):
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
    user_dict = user.dict()
    del user_dict['password']
    user_dict['created_at'] = datetime.today()
    user_dict['updated_at'] = datetime.today()
    db_user = u_model.Users(**user_dict, encrypted_password = hashed_password)
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except:
        raise exc.INTERNAL_ERROR_EXCEPTION

def update_user(db: Session, user: u_schemas.UserUpdate, user_id: int):
    get_user_by_id(db, user_id)
    db_user = update(u_model.Users)\
        .where(u_model.Users.id == user_id)\
            .values(**user.dict(exclude_unset=True), updated_at = datetime.today())
    try:
        db.execute(db_user)
        db.commit()
    except:
        raise exc.INTERNAL_ERROR_EXCEPTION

def delete_user(db: Session, user_id: int):
    get_user_by_id(db, user_id)
    db_user = db.query(u_model.Users)\
        .filter(u_model.Users.id == user_id)\
            .first()
    try:
        db.delete(db_user)
        db.commit()
    except:
        raise exc.INTERNAL_ERROR_EXCEPTION

def auth_user(db: Session, user_login: u_schemas.UserLogin):
    hashed_password = hashlib.sha256(user_login.password.encode()).hexdigest()
    db_user = get_user_by_email(db, email=user_login.email)
    if not db_user or db_user.encrypted_password != hashed_password:
        raise exc.INVALID_CREDENTIALS
    return db_user

def insert_user_token(db: Session, user: u_schemas.UserResetPassEmail):
    token = hashlib.sha256(str(datetime.today()).encode()).hexdigest()
    db_user = update(u_model.Users)\
        .where(u_model.Users.email == user.email)\
            .values(token = token)
    try:
        db_user = db.execute(db_user)
        db.commit()
        return db_user
    except:
        raise exc.INTERNAL_ERROR_EXCEPTION

def user_reset_password(db: Session, user: u_schemas.UserResetPass, token: u_schemas.UserResetPassToken):
    new_pass_user = update(u_model.Users)\
        .where(u_model.Users.token == token.token)\
            .values(encrypted_password=hashlib.sha256(user.new_password.encode()).hexdigest(), token=None)
    try:
        db.execute(new_pass_user)
        db.commit()
    except:
        raise exc.INTERNAL_ERROR_EXCEPTION