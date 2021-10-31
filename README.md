# Worganizer: The Ultimate Vocabulary Organizer For Language Learning (Maybe)

I love learning languages, it's a great mind expanding hobby that allows anyone to learn a lot of other things besides the languages themselves. Well, since the study method that I use requires to learn a lot of the most used words in the daily basis, I end up needing to organize all of my new acquired vocabulary, usually on a .xlsx file, wich is kind of a pain to me.

I truly love spreadsheets and everything you can do with them, but a simple spreadsheet with a lot of words and translations is pretty boring to make IMO.

So, why not create a software to automatize this and add into it a lot of not so essential features for the sake of practice and learning new things?

## Installation & Setup

After cloning the project, you'll need to add a .env file in the backend folder with the following variables:

```.env
#Database variables
#================================#
DATABASE_URL = your database url, I made the project using mariadb so, if you end up using another database, you might need to change the code on the models files
#================================#

#Email service variables
#================================#
PORT = 465
SMTP_SERVER = smtp.gmail.com
SENDER_EMAIL = the email wich worganizer will use to send emails. It's interesting to create a new one for this. See more on: https://realpython.com/python-send-email/
EMAIL_PASS = the password for the email defined above
URL_LINK = your front-end url
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

I will update this when the software becomes truly functional, for now, you can play with the users CRUD on the back-end at http://localhost:8080/docs.


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Also, I'm open to any critics to my code. Looking forward to learn from your advice!
