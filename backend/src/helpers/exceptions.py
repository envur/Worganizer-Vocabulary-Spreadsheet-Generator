from fastapi import HTTPException


INTERNAL_ERROR_EXCEPTION = HTTPException(
    status_code=500,
    detail="An internal error occured. Please, contact the support!"
    )