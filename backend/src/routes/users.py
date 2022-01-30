from .imports import *
from src.cruds import users as u_cruds
from src.schemas import users as u_schemas
from src.schemas import status as s_schemas


@app.get("/user/token/{token}/", tags=["Users"], response_model=u_schemas.UserByTokenResponse)
def get_user_by_token(token: str, db: Session = Depends(get_db)):
    db_user = u_cruds.get_user_email_by_token(db, token)
    return u_schemas.UserByTokenResponse(email=db_user.email)

@app.post("/user/get/token", tags=["Users"], response_model=s_schemas.StatusModel)
def user_generate_reset_token(user: u_schemas.UserResetPassEmail, db: Session = Depends(get_db)):
    db_user = u_cruds.get_user_by_email(db, user.email)
    if not db_user:
        raise HTTPException(status_code=404, detail="There isn't an user with this email!")
    u_cruds.insert_user_token(db, user)
    email_sender.email_sender(user, db_user.token)
    return s_schemas.StatusModel(message="Email sent! Please make sure to check your spam.")

@app.post("/user/login", tags=["Users"], response_model=s_schemas.StatusModel)
def login_user(db: Session = Depends(get_db), user_login: u_schemas.UserLogin = Body(..., embed=True)):
    db_user = u_cruds.auth_user(db, user_login)
    if db_user:
        return s_schemas.StatusModel(message="Successfully logged in!")

@app.post("/user/register", tags=["Users"], response_model=s_schemas.StatusModel)
def register_user(user: u_schemas.UserCreate = Body(..., embed=True), db: Session = Depends(get_db)):
    db_user = u_cruds.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already taken!")
    u_cruds.register_user(db, user)
    return s_schemas.StatusModel(message="User registered successfully!")

@app.put("/user/reset/password", tags=["Users"], response_model=s_schemas.StatusModel, response_model_exclude_unset=True)
def user_reset_pass(user: u_schemas.UserResetPass, token: u_schemas.UserResetPassToken, db: Session = Depends(get_db)):
    db_user = u_cruds.get_user_email_by_token(db, token.token)
    if db_user.email != user.email:
        raise HTTPException(status_code=400, detail="Invalid email!")
    u_cruds.user_reset_password(db, user, token)
    return s_schemas.StatusModel(message="Password updated successfully!")

@app.put("/user/update/{user_id}", tags=["Users"], response_model=s_schemas.StatusModel)
def update_user(user_id: int, user: u_schemas.UserUpdate = Body(..., embed=True), db: Session = Depends(get_db)):
    db_user = u_cruds.get_user_by_email(db, email=user.email)
    if db_user and db_user.id != user_id:
        raise HTTPException(status_code=400, detail="Email already taken!")
    u_cruds.update_user(db, user, user_id)
    return s_schemas.StatusModel(message="User updated successfully!")

@app.delete("/user/delete/{user_id}", tags=["Users"], response_model= s_schemas.StatusModel)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    u_cruds.delete_user(db, user_id)
    return s_schemas.StatusModel(message="User deleted successfully!")
