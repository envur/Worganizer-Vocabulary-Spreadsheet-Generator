# Worganizer: The Ultimate Vocabulary Organizer For Language Learning (Maybe)

This is a very specific software for a very specific problem I have when it comes to a hobby of mine, which is language learning. It's just an overcomplicated .xlsx generator for all the new words I learn.

## Installation & Setup

After cloning the project, you'll need to add a .env file in the backend folder with the following variables:

```.env
#Database variables
#================================#
DATABASE_URL = None #your database url, I made the project using mariadb so, if you end up using another database, you might need to change the code on the models files
#================================#

#Email service variables
#================================#
PORT = 465
SMTP_SERVER = smtp.gmail.com
SENDER_EMAIL = None #the email wich worganizer will use to send emails. It's interesting to create a new one for this. See more on: https://realpython.com/python-send-email/
EMAIL_PASS = None #the password for the email defined above
URL_LINK = None #your front-end url
#================================#
```
Now, create a python virtual environment, also in the backend folder:

```bash
python3 -m venv env
```
Remember to activate it everytime you execute the software:

```bash
source env/bin/activate
```
After that, you can install the dependencies listed on requirements.txt:

```bash
pip install -r requirements.txt
```
Run the database migrations:

```bash
alembic upgrade head
```
Now, you can finally run the server:

```bash
uvicorn main:app --reload
```

## Alembic and Changes in the Database

If you make any changes to the tables, remember to use alembic revision to apply them:

```bash
alembic revision --autogenerate -m "Explain what changes you made here"
```
Now, run the migrations again:

```bash
alembic upgrade head
```

## Usage

I will update this when the software becomes truly functional, for now, you can only play with the users CRUD on the back-end at http://localhost:8080/docs.


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Also, I'm open to any critics to my code. Looking forward to learn from your advice!
