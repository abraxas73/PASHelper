#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$SCRIPT_DIR/.."

echo "Stopping any running frontend processes on port 3000..."
lsof -ti:3000 | xargs kill -9 2>/dev/null || true

echo "Starting Frontend..."
cd "$PROJECT_ROOT/frontend"

echo "Installing dependencies..."
npm install

echo "Starting Next.js dev server..."
npm run dev
