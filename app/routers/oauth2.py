from jose import JWTError, jwt
from datetime import datetime, timedelta

#secret key
#algorithm
#expiration time

SECRET_KEY = '09d25e06b6f66307e556610a5120202020202020202020202020202020202020'
ALGORITHM = 'HS256'
EXPIRE_IN = 60 * 60 * 24 * 7

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})


    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt
