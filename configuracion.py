'''import os
import dotenv
from pathlib import Path  # python3 only
env_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path=env_path)
b

# Connect to the database
dbURL = os.getenv("MONGODB_URL")
if not dbURL:
    raise ValueError("You should specify MONGODB_URL environment variable") '''