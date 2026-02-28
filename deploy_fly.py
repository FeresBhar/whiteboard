#!/usr/bin/env python3
"""
Deploy to Fly.io - High performance option
"""

import subprocess
import sys

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(f"$ {cmd}")
        if result.stdout:
            print(result.stdout)
        if result.stderr and result.returncode != 0:
            print(f"Error: {result.stderr}")
        return result.returncode == 0
    except Exception as e:
        print(f"Error running {cmd}: {e}")
        return False

def main():
    print("🚀 Deploy to Fly.io - High Performance Hosting")
    print("=" * 50)
    
    print("\n📦 STEP 1: Install Fly CLI")
    print("Windows: Download from https://fly.io/docs/hands-on/install-flyctl/")
    print("Or run: iwr https://fly.io/install.ps1 -useb | iex")
    
    input("\nPress Enter after installing flyctl...")
    
    print("\n🔑 STEP 2: Login to Fly.io")
    if not run_command("flyctl auth login"):
        print("❌ Login failed. Make sure flyctl is installed.")
        return
    
    print("\n🐳 STEP 3: Launch App")
    print("This will create and deploy your app...")
    
    if run_command("flyctl launch --dockerfile backend/Dockerfile --name whiteboard-app"):
        print("✅ App launched successfully!")
        
        print("\n🗄️ STEP 4: Add Redis")
        run_command("flyctl redis create")
        
        print("\n🚀 STEP 5: Deploy")
        run_command("flyctl deploy")
        
        print("\n📋 STEP 6: Get Your URL")
        run_command("flyctl status")
        
        app_url = input("\nEnter your Fly.io app URL (e.g., whiteboard-app.fly.dev): ").strip()
        if app_url.startswith('https://'):
            app_url = app_url[8:]
        
        print(f"\n🔧 Update frontend:")
        print(f"python update_backend_url.py {app_url}")
        
        print(f"\n🎉 Deployment Complete!")
        print(f"Backend: https://{app_url}")
    else:
        print("❌ Launch failed. Check the error messages above.")

if __name__ == "__main__":
    main()