from datetime import datetime, timedelta
from jose import jwt
from app.config import SECRET_KEY, ALGORITHM
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Substitua pelo username do admin
username_admin = "admin"

payload = {
    "sub": username_admin,
    "exp": datetime.utcnow() + timedelta(minutes=60)  # expira em 60 min
}

token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
print("Token JWT do admin:", token)
