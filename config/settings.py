import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet
load_dotenv()

BASE_URL = os.getenv("BASE_URL", "http://localhost:3000")
BROWSER = os.getenv("BROWSER", "chrome")
HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))
EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "60"))
FERNET_KEY = os.getenv("FERNET_KEY")

fernet = Fernet(FERNET_KEY.encode())

def get_credentials(alias):
    username = os.getenv(f"USER_{alias}")
    encrypted_password = os.getenv(f"PASS_{alias}")
    if not username or not encrypted_password:
        raise ValueError(f"Credentials not found for alias: {alias}")
    password = fernet.decrypt(encrypted_password.encode()).decode()
    return username, password