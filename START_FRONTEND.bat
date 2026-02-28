@echo off
echo Starting frontend server on http://localhost:3000
echo.
echo Open your browser and go to: http://localhost:3000
echo.
cd frontend
python -m http.server 3000
