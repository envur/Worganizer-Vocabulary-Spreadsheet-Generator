from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# FastAPI instance
app = FastAPI(
    version="0.0.3",
    title="Worganizer",
    description="The Ultimate Vocabulary Organizer For Language Learning"
)

# CORS treatment
origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
from src.routes import users, words

# Root route of the backend
@app.get('/', tags=['Root Route'])
def worganizer_root_route():
    return {'Worganizer': 'The Ultimate Vocabulary Organizer For Language Learning'}