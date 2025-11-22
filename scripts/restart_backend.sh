#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$SCRIPT_DIR/.."

echo "Stopping any running backend processes on port 8000..."
lsof -ti:8000 | xargs kill -9 2>/dev/null || true

echo "Starting Backend..."
cd "$PROJECT_ROOT/backend"

# Check if venv exists, if not create it
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Starting Uvicorn server..."
uvicorn main:app --reload --host 0.0.0.0 --port 8000
