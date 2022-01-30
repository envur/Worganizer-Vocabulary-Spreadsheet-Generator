import hashlib
from fastapi import HTTPException
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import update
from src.helpers import exceptions as exc