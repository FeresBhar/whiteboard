#!/usr/bin/env python3
"""
Automated deployment script for the collaborative whiteboard
"""

import os
import subprocess
import json
import sys

def run_command(cmd, cwd=None):
    """Run a shell command and return the result"""
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error running command: {cmd}")
            print(f"Error: {result.stderr}")
            return False, result.stderr
        return True, result.stdout
    except Exception as e:
        print(f"Exception running command: {cmd}")
        print(f"Exception: {e}")
        return False, str(e)

def check_requirements():
    """Check if required tools are installed"""
    print("🔍 Checking requirements...")
    
    # Check if git is installed
    success, _ = run_command("git --version")
    if not success:
        print("❌ Git is not installed. Please install Git first.")
        return False
    
    # Check if we're in a git repo
    success, _ = run_command("git status")
    if not success:
        print("📁 Initializing git repository...")
        run_command("git init")
        run_command("git add .")
        run_command('git commit -m "Initial commit"')
    
    print("✅ Requirements check passed!")
    return True

def deploy_to_railway():
    """Deploy backend to Railway"""
    print("\n🚂 Deploying to Railway...")
    print("1. Go to https://railway.app")
    print("2. Sign up with GitHub")
    print("3. Click 'New Project' → 'Deploy from GitHub repo'")
    print("4. Select this repository")
    print("5. Add Redis: Click 'New' → 'Database' → 'Add Redis'")
    print("6. Copy your app URL when deployment completes")
    
    backend_url = input("\n📝 Enter your Railway app URL (e.g., your-app.railway.app): ").strip()
    if backend_url.startswith('https://'):
        backend_url = backend_url[8:]  # Remove https://
    
    return backend_url

def deploy_to_render():
    """Deploy backend to Render"""
    print("\n🎨 Deploying to Render...")
    print("1. Go to https://render.com")
    print("2. Sign up with GitHub")
    print("3. New → Web Service → Connect your repo")
    print("4. Settings:")
    print("   - Environment: Docker")
    print("   - Dockerfile Path: backend/Dockerfile")
    print("   - Build Context: backend")
    print("5. Add Redis: New → Redis → Create")
    print("6. Copy your app URL when deployment completes")
    
    backend_url = input("\n📝 Enter your Render app URL (e.g., your-app.onrender.com): ").strip()
    if backend_url.startswith('https://'):
        backend_url = backend_url[8:]  # Remove https://
    
    return backend_url

def update_frontend_config(backend_url):
    """Update the frontend configuration with the backend URL"""
    print(f"\n⚙️ Updating frontend configuration...")
    
    canvas_js_path = "frontend/canvas.js"
    
    # Read the current file with UTF-8 encoding
    with open(canvas_js_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update the BACKEND_URL
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if 'const BACKEND_URL = ' in line:
            lines[i] = f'const BACKEND_URL = "{backend_url}"  // Updated by deploy script'
            break
    
    # Write back to file with UTF-8 encoding
    with open(canvas_js_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    
    print(f"✅ Updated BACKEND_URL to: {backend_url}")

def deploy_frontend_github():
    """Instructions for deploying frontend to GitHub Pages"""
    print("\n📄 Deploying Frontend to GitHub Pages...")
    print("1. Create a new repository on GitHub called 'whiteboard-frontend'")
    print("2. Upload all files from the 'frontend/' folder")
    print("3. Go to Settings → Pages")
    print("4. Source: Deploy from branch")
    print("5. Branch: main, Folder: / (root)")
    print("6. Click Save")
    print("7. Wait 1-2 minutes for deployment")
    
    github_username = input("\n📝 Enter your GitHub username: ").strip()
    frontend_url = f"https://{github_username}.github.io/whiteboard-frontend"
    
    print(f"\n🎉 Your frontend will be available at: {frontend_url}")
    return frontend_url

def create_github_repo():
    """Create and push to GitHub repository"""
    print("\n📦 Setting up GitHub repository...")
    
    repo_name = input("Enter repository name (default: collaborative-whiteboard): ").strip()
    if not repo_name:
        repo_name = "collaborative-whiteboard"
    
    print(f"1. Go to https://github.com/new")
    print(f"2. Repository name: {repo_name}")
    print(f"3. Make it Public (required for free GitHub Pages)")
    print(f"4. Don't initialize with README (we have files already)")
    print(f"5. Click 'Create repository'")
    
    github_username = input("Enter your GitHub username: ").strip()
    
    print(f"\n📤 Run these commands to push your code:")
    print(f"git remote add origin https://github.com/{github_username}/{repo_name}.git")
    print(f"git branch -M main")
    print(f"git push -u origin main")
    
    return github_username, repo_name

def main():
    """Main deployment function"""
    print("🚀 Collaborative Whiteboard Deployment Script")
    print("=" * 50)
    
    if not check_requirements():
        sys.exit(1)
    
    print("\nChoose your deployment platform:")
    print("1. Railway (Recommended - Easy setup)")
    print("2. Render (Alternative)")
    print("3. Local testing only")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    backend_url = None
    
    if choice == "1":
        backend_url = deploy_to_railway()
    elif choice == "2":
        backend_url = deploy_to_render()
    elif choice == "3":
        backend_url = "localhost:8000"
        print("\n🏠 Using localhost for testing")
    else:
        print("❌ Invalid choice")
        sys.exit(1)
    
    # Update frontend configuration
    update_frontend_config(backend_url)
    
    if choice in ["1", "2"]:
        # Deploy frontend
        frontend_url = deploy_frontend_github()
        
        print("\n" + "=" * 50)
        print("🎉 DEPLOYMENT COMPLETE!")
        print("=" * 50)
        print(f"Backend URL: https://{backend_url}")
        print(f"Frontend URL: {frontend_url}")
        print(f"\n📋 Next steps:")
        print(f"1. Upload frontend files to GitHub Pages")
        print(f"2. Test your whiteboard at: {frontend_url}")
        print(f"3. Share with friends!")
        print(f"\n🎨 Different rooms:")
        print(f"   {frontend_url}?room=design")
        print(f"   {frontend_url}?room=meeting")
    else:
        print("\n🏠 Local testing setup complete!")
        print("Run: docker-compose up")
        print("Then: cd frontend && python -m http.server 3000")
        print("Open: http://localhost:3000")

if __name__ == "__main__":
    main()