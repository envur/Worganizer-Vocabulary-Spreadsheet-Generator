import os, sys
from dotenv import load_dotenv


#Set the OS enviroment to use the .env variables
BASE_DIR = os.path.dirname(os.path.abspath(os.path.join(__file__ ,"../..")))
load_dotenv(os.path.join(BASE_DIR, ".env"))
sys.path.append(BASE_DIR)