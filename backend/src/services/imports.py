import os
import smtplib, ssl
from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Session
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from src.helpers import exceptions as exc