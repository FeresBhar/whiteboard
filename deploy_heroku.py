#!/usr/bin/env python3
"""
Deploy to Heroku - Classic platform
"""

import subprocess

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
        print(f"Error: {e}")
        return False

def main():
    print("🚀 Deploy to Heroku")
    print("=" * 30)
    
    print("\n📦 STEP 1: Install Heroku CLI")
    print("Download from: https://devcenter.heroku.com/articles/heroku-cli")
    
    input("\nPress Enter after installing Heroku CLI...")
    
    print("\n🔑 STEP 2: Login")
    run_command("heroku login")
    
    print("\n🏗️ STEP 3: Create App")
    app_name = input("Enter app name (e.g., my-whiteboard): ").strip()
    
    if run_command(f"heroku create {app_name}"):
        print("\n🗄️ STEP 4: Add Redis")
        run_command(f"heroku addons:create heroku-redis:mini -a {app_name}")
        
        print("\n🐳 STEP 5: Set Stack to Container")
        run_command(f"heroku stack:set container -a {app_name}")
        
        print("\n📁 STEP 6: Create heroku.yml")
        with open("heroku.yml", "w") as f:
            f.write("""build:
  docker:
    web: backend/Dockerfile
run:
  web: uvicorn main:app --host 0.0.0.0 --port $PORT
""")
        
        print("\n🚀 STEP 7: Deploy")
        run_command("git add heroku.yml")
        run_command('git commit -m "Add heroku.yml"')
        run_command(f"git push heroku main")
        
        print(f"\n🎉 Deployed!")
        print(f"Your app: https://{app_name}.herokuapp.com")
        
        print(f"\n🔧 Update frontend:")
        print(f"python update_backend_url.py {app_name}.herokuapp.com")

if __name__ == "__main__":
    main()