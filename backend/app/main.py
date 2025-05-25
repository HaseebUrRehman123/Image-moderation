from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app import auth, moderation

app = FastAPI(title="Image Moderation API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(moderation.router)
