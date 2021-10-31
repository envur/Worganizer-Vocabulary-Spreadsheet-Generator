from .imports import *
from src.models import users as user_model
from src.schemas import users as user_schema


#Functions to get user info from the database
#================================#
def get_user_by_id(db: Session, user_id: int):
    return db.query(user_model.Users).filter(user_model.Users.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(user_model.Users).filter(user_model.Users.email == email).first()

def get_user_email_by_token(db: Session, token: str):
    return db.query(user_model.Users).filter(user_model.Users.token == token).first()    
#================================#

#User register, update and delete functions
#================================#
def register_user(db: Session, user: user_schema.UserCreate):
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
    user_dict = user.dict()
    del user_dict['password']
    del user_dict['status']
    del user_dict['message']
    user_dict['created_at'] = datetime.today()
    user_dict['updated_at'] = datetime.today()
    db_user = user_model.Users(**user_dict, encrypted_password = hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user: user_schema.UserUpdate, user_id: int):
    db_user = update(user_model.Users)\
        .where(user_model.Users.id == user_id)\
            .values(**user.dict(exclude_unset=True))
    db.execute(db_user)
    db.commit()

def delete_user(db: Session, user_id: int):
    db_user = db.query(user_model.Users)\
        .filter(user_model.Users.id == user_id)\
            .first()
    db.delete(db_user)
    db.commit()
#================================#

#User authentication and password reset functions
#================================#
def auth_user(db: Session, user_login: user_schema.UserLogin):
    hashed_password = hashlib.sha256(user_login.password.encode()).hexdigest()
    db_user = get_user_by_email(db, email=user_login.email)
    if db_user and db_user.encrypted_password == hashed_password:
        return db_user
        
    return False

def insert_user_token(db:Session, user: user_schema.UserResetPassEmail, token: user_schema.UserResetPassToken):
    db_user = update(user_model.Users)\
        .where(user_model.Users.email == user.email)\
            .values(token = token)
    db_user = db.execute(db_user)
    db.commit()
    return db_user

def user_reset_password(db: Session, user: user_schema.UserResetPass, token: user_schema.UserResetPassToken):
    db_user = get_user_by_email(db, user.email)
    if db_user and db_user.token == token.token and user.new_password:
        new_pass_user = update(user_model.Users)\
        .where(user_model.Users.token == token.token)\
        .values(encrypted_password=hashlib.sha256(user.new_password.encode()).hexdigest(), token=None)
        db.execute(new_pass_user)
        db.commit()
        return db_user
#================================#