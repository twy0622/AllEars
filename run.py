import subprocess
import os

# Start FastAPI backend (main.py) from the backend directory
fastapi_process = subprocess.Popen(
    ["python", "backend/main.py"],
)

# Start Streamlit frontend (app.py) from the frontend directory
streamlit_process = subprocess.Popen(
    ["streamlit", "run", "frontend/app.py"],
)