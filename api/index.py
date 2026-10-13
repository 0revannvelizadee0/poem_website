import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app_mysql import app, init_db

# Create tables on first cold start if they don't exist
try:
    init_db()
except Exception as e:
    print(f"init_db warning: {e}")
