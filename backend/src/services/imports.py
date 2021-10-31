#Imports file created in order to have a cleaner code
#================================#
from sqlalchemy.orm import Session
import os
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from typing import Optional
#================================#