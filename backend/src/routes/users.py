from .imports import *
from src.cruds import users as u_cruds
from src.schemas import users as u_schemas
from src.schemas import status as s_schemas


#Route to get the user email using the token, useful to the front-end and also if you want to validate the token
#================================#
@app.get("/user/token/{token}/", tags=["Users"], response_model=u_schemas.UserByToken, response_model_exclude_unset=True)
def get_user_by_token(token: str, db: Session = Depends(get_db)):
    db_user = u_cruds.get_user_email_by_token(db, token)
    if db_user:
        return u_schemas.UserByToken(status="success", email=db_user.email)
    else:
        return u_schemas.UserByToken(status="error", message="Token inválido!")
#================================#

#Route that generates the user token and sends it via email
#================================#
@app.post("/user/get/token", tags=["Users"], response_model=s_schemas.StatusModel)
def user_generate_reset_token(user: u_schemas.UserResetPassEmail, db: Session = Depends(get_db)):
    db_user = u_cruds.get_user_by_email(db, user.email)
    if db_user:
        token = hashlib.sha256(str(datetime.today()).encode()).hexdigest()
        u_cruds.insert_user_token(db, user, token)
        email_sender.email_sender(user, token)
        return s_schemas.StatusModel(status="success", message="Email enviado! Cheque sua caixa de entrada e spam")
    if not db_user:
        return s_schemas.StatusModel(status="error", message="Não é possível enviar o email!")
#================================#

#Login route
#================================#
@app.post("/user/login", tags=["Users"], response_model= s_schemas.StatusModel)
def login_user(db: Session = Depends(get_db), user_login: u_schemas.UserLogin = Body(..., embed=True)):
    db_user = u_cruds.auth_user(db, user_login)
    if db_user:
        return s_schemas.StatusModel(status="success", message="Logado com sucesso!")
    return s_schemas.StatusModel(status="error", message="Login inválido!")
#================================#

#User register route
#================================#
@app.post("/user/register", tags=["Users"], response_model=s_schemas.StatusModel)
def register_user(user: u_schemas.UserCreate = Body(..., embed=True), db: Session = Depends(get_db)):
    db_user = u_cruds.get_user_by_email(db, email=user.email)
    if db_user:
        return s_schemas.StatusModel(status="error", message="Email já cadastrado!") 
    db_user = u_cruds.register_user(db, user)
    return s_schemas.StatusModel(status="success", message="Usuário adicionado com sucesso!")
#================================#

#User reset password route
#================================#
@app.put("/user/reset/password", tags=["Users"], response_model=s_schemas.StatusModel, response_model_exclude_unset=True)
def user_reset_pass(user: u_schemas.UserResetPass, token: u_schemas.UserResetPassToken, db: Session = Depends(get_db)):
    db_user = u_cruds.get_user_email_by_token(db, token.token)
    if not db_user:
        return s_schemas.StatusModel(status="error", message="Token inválido!")
    if db_user.email != user.email:
        return s_schemas.StatusModel(status="error", message="Email inválido!")
    db_user = u_cruds.user_reset_password(db, user, token)
    if db_user:
        return s_schemas.StatusModel(status="success", message="Senha alterada com sucesso!")
    else:
        return s_schemas.StatusModel(status="error", message="Não foi possível redefinir a senha")
#================================#

#User update route
#================================#
@app.put("/user/update/{user_id}", tags=["Users"], response_model=s_schemas.StatusModel)
def update_user(user_id: int, user: u_schemas.UserUpdate = Body(..., embed=True), db: Session = Depends(get_db)):
    db_user = u_cruds.get_user_by_email(db, email=user.email)
    if db_user and db_user.id != user_id:
        return s_schemas.StatusModel(status="error", message="Email já cadastrado!")
    u_cruds.update_user(db, user, user_id)
    return s_schemas.StatusModel(status="success", message="Usuário atualizado!")
#================================#

#User delete route
#================================#
@app.delete("/user/delete/{user_id}", tags=["Users"], response_model= s_schemas.StatusModel)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = u_cruds.get_user_by_id(db, user_id)    
    if not db_user:
        return s_schemas.StatusModel(status="error", message="Usuário não encontrado!")
    db_user = u_cruds.delete_user(db, user_id)
    return s_schemas.StatusModel(status="success", message="Usuário deletado!")
#================================#
