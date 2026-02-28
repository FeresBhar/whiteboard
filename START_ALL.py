#!/usr/bin/env python3
"""
One-click start script for local development
"""

import subprocess
import sys
import time
import webbrowser
import os
from threading import Thread

def run_command_in_background(cmd, cwd=None, name="Process"):
    """Run a command in the background"""
    def run():
        try:
            print(f"🚀 Starting {name}...")
            process = subprocess.Popen(cmd, shell=True, cwd=cwd)
            process.wait()
        except KeyboardInterrupt:
            print(f"🛑 Stopping {name}...")
            process.terminate()
        except Exception as e:
            print(f"❌ Error in {name}: {e}")
    
    thread = Thread(target=run, daemon=True)
    thread.start()
    return thread

def check_docker():
    """Check if Docker is running"""
    try:
        result = subprocess.run("docker --version", shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Docker is available")
            return True
        else:
            print("❌ Docker is not available")
            return False
    except:
        print("❌ Docker is not installed")
        return False

def check_python():
    """Check if Python is available"""
    try:
        result = subprocess.run("python --version", shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Python is available: {result.stdout.strip()}")
            return True
        else:
            print("❌ Python is not available")
            return False
    except:
        print("❌ Python is not installed")
        return False

def main():
    """Main function to start everything"""
    print("🎨 Collaborative Whiteboard - Local Development")
    print("=" * 50)
    
    # Check requirements
    if not check_docker():
        print("\n❌ Docker is required for the backend")
        print("Please install Docker Desktop and try again")
        sys.exit(1)
    
    if not check_python():
        print("\n❌ Python is required for the frontend server")
        print("Please install Python and try again")
        sys.exit(1)
    
    print("\n🚀 Starting services...")
    
    # Start backend with Docker Compose
    print("\n1️⃣ Starting backend (Docker Compose)...")
    backend_thread = run_command_in_background("docker-compose up", name="Backend")
    
    # Wait a bit for backend to start
    print("⏳ Waiting for backend to start...")
    time.sleep(10)
    
    # Start frontend server
    print("\n2️⃣ Starting frontend server...")
    frontend_thread = run_command_in_background(
        "python -m http.server 3000", 
        cwd="frontend", 
        name="Frontend"
    )
    
    # Wait a bit for frontend to start
    time.sleep(3)
    
    # Open browser
    print("\n🌐 Opening browser...")
    try:
        webbrowser.open("http://localhost:3000")
    except:
        print("Could not open browser automatically")
    
    print("\n" + "=" * 50)
    print("🎉 WHITEBOARD IS READY!")
    print("=" * 50)
    print("📱 Frontend: http://localhost:3000")
    print("🔧 Backend API: http://localhost:8000")
    print("📊 Backend Health: http://localhost:8000/health")
    print("\n🎯 Test different rooms:")
    print("   http://localhost:3000?room=design")
    print("   http://localhost:3000?room=meeting")
    print("   http://localhost:3000?room=brainstorm")
    print("\n📱 Share with others on same WiFi:")
    print("   Find your IP with: ipconfig")
    print("   Share: http://YOUR-IP:3000")
    print("\n🛑 Press Ctrl+C to stop all services")
    print("=" * 50)
    
    try:
        # Keep the main thread alive
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down services...")
        print("Stopping Docker Compose...")
        subprocess.run("docker-compose down", shell=True)
        print("✅ All services stopped")

if __name__ == "__main__":
    main()