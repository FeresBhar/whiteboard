@echo off
echo 🎨 Collaborative Whiteboard - Quick Start
echo ==========================================

echo.
echo 🔍 Checking requirements...

REM Check if Docker is available
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker is not available
    echo Please install Docker Desktop and try again
    pause
    exit /b 1
)
echo ✅ Docker is available

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not available
    echo Please install Python and try again
    pause
    exit /b 1
)
echo ✅ Python is available

echo.
echo 🚀 Starting services...
echo.

REM Start Docker Compose in background
echo 1️⃣ Starting backend (Docker Compose)...
start "Backend" cmd /c "docker-compose up"

REM Wait for backend to start
echo ⏳ Waiting for backend to start...
timeout /t 10 /nobreak >nul

REM Start frontend server
echo 2️⃣ Starting frontend server...
start "Frontend" cmd /c "cd frontend && python -m http.server 3000"

REM Wait for frontend to start
timeout /t 3 /nobreak >nul

REM Open browser
echo 🌐 Opening browser...
start http://localhost:3000

echo.
echo ==========================================
echo 🎉 WHITEBOARD IS READY!
echo ==========================================
echo 📱 Frontend: http://localhost:3000
echo 🔧 Backend API: http://localhost:8000
echo 📊 Backend Health: http://localhost:8000/health
echo.
echo 🎯 Test different rooms:
echo    http://localhost:3000?room=design
echo    http://localhost:3000?room=meeting
echo    http://localhost:3000?room=brainstorm
echo.
echo 📱 Share with others on same WiFi:
echo    Find your IP with: ipconfig
echo    Share: http://YOUR-IP:3000
echo.
echo 🌐 For internet sharing, see DEPLOY_FREE.md
echo 🛑 Close this window and the opened terminals to stop
echo ==========================================

pause
