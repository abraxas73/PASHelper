import os
from dotenv import load_dotenv

print(f"CWD: {os.getcwd()}")
dotenv_path = os.path.join(os.getcwd(), "..", ".env")
print(f"Target .env path: {dotenv_path}")

if os.path.exists(dotenv_path):
    print("File exists.")
    with open(dotenv_path, "r") as f:
        print(f"File content:\n{f.read()}")
else:
    print("File does not exist.")

print(f"Before load_dotenv: DATABASE_URL={os.getenv('DATABASE_URL')}")
load_dotenv(dotenv_path, override=True)
print(f"After load_dotenv: DATABASE_URL={os.getenv('DATABASE_URL')}")
