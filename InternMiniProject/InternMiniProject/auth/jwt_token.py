import os

import jwt
from dotenv import load_dotenv

load_dotenv()

secret_key = os.getenv("SECRET_KEY")
algo = os.getenv("JWT_ALGO")
exp = os.getenv("JWT_EXP")


def encode(payload):
    return jwt.encode(payload, secret_key, algorithm=algo)


def decode(token):
    return jwt.decode(token, secret_key, algorithms=[algo])
