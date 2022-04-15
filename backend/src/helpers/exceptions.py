from fastapi import HTTPException


#TODO: Create Words Exceptions
INTERNAL_ERROR_EXCEPTION = HTTPException(
    status_code=500,
    detail="An internal error occured. Please, contact the support!"
    )

# Users exceptions
USER_ID_NOT_FOUND = HTTPException(
    status_code=404, 
    detail="There isn't an user with this ID!"
    )
USER_EMAIL_NOT_FOUND = HTTPException(
    status_code=404, 
    detail="There isn't an user with this email!"
    )
EMAIL_NOT_AVAILABLE = HTTPException(
    status_code=400, 
    detail="Email already taken!"
    )
INVALID_RECOVERY_EMAIL = HTTPException(
    status_code=400, 
    detail="Invalid email!"
    )
INVALID_TOKEN = HTTPException(
    status_code=400, 
    detail="Invalid token!"
    )
INVALID_CREDENTIALS = HTTPException(
    status_code=401, 
    detail="Invalid login!"
    )

#Email system exceptions
EMAIL_SENDING_FAILED = HTTPException(
    status_code=400, 
    detail="Something is wrong when we try to send you an email!"
    )