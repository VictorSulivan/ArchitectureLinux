import binascii
from datetime import date
SECRET_KEY = binascii.hexlify(date.today().strftime("%m-%Y-%d").encode())
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60000