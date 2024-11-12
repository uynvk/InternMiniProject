import os
import secrets
from datetime import datetime, timedelta

import jwt
from dotenv import load_dotenv


class JWTToken:
    load_dotenv()
    algo = os.getenv("JWT_ALGO")
    exp = os.getenv("JWT_EXP_SECOND")
    secret_key_char_len = int(os.getenv("JWT_SECRET_CHAR_LEN"))

    @classmethod
    def generate_secret(cls):
        return secrets.token_hex(cls.secret_key_char_len >> 1)

    @classmethod
    def encode(cls, secret_key, payload):
        # don't need salt because exp will be different each time already..
        payload["exp"] = datetime.utcnow() + timedelta(seconds=int(cls.exp))
        return jwt.encode(payload, secret_key, algorithm=cls.algo)

    @classmethod
    def decode(cls, secret_key, token):
        return jwt.decode(token, secret_key, algorithms=[cls.algo])

    @classmethod
    def decode_no_secret(cls, token):
        return jwt.decode(
            token,
            algorithms=[cls.algo],
            options={"verify_signature": False, "verify_exp": True},
        )
