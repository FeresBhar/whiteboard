#!/usr/bin/env python3
"""
Git setup helper script
"""

import subprocess
import sys

def run_command(cmd):
    """Run a command and return success status"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {cmd}")
            if result.stdout.strip():
                print(f"   {result.stdout.strip()}")
            return True
        else:
            print(f"❌ {cmd}")
            print(f"   Error: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"❌ {cmd}")
        print(f"   Exception: {e}")
        return False

def main():
    print("🚀 Git Setup Helper")
    print("=" * 30)
    
    # Get user input
    username = input("Enter your GitHub username: ").strip()
    repo_name = input("Enter repository name (e.g., whiteboard): ").strip()
    
    if not username or not repo_name:
        print("❌ Username and repository name are required")
        sys.exit(1)
    
    # Construct remote URL
    remote_url = f"https://github.com/{username}/{repo_name}.git"
    
    print(f"\n🎯 Setting up remote: {remote_url}")
    print("\n📋 Running commands:")
    
    # Add remote
    if not run_command(f"git remote add origin {remote_url}"):
        print("\n⚠️ Remote might already exist, trying to set URL...")
        run_command(f"git remote set-url origin {remote_url}")
    
    # Switch to main branch
    run_command("git branch -M main")
    
    # Push to GitHub
    if run_command("git push -u origin main"):
        print(f"\n🎉 SUCCESS!")
        print(f"Your code is now on GitHub: https://github.com/{username}/{repo_name}")
        print(f"\n📋 Next steps:")
        print(f"1. Deploy backend to Railway/Render")
        print(f"2. Deploy frontend to GitHub Pages")
        print(f"3. Update BACKEND_URL in canvas.js")
    else:
        print(f"\n❌ Push failed. Make sure:")
        print(f"1. Repository exists: https://github.com/{username}/{repo_name}")
        print(f"2. Repository is public")
        print(f"3. You have push access")

if __name__ == "__main__":
    main()