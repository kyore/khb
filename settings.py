import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

KHANBANK_USERNAME = os.getenv('KHANBANK_USERNAME')
KHANBANK_PASSWORD = os.getenv('KHANBANK_PASSWORD')
KHANBANK_ACCOUNT = os.getenv('KHANBANK_ACCOUNT')
