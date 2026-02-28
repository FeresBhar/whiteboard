#!/usr/bin/env python3
"""
Simple deployment script for the collaborative whiteboard
"""

import os
import sys

def main():
    """Simple deployment guide"""
    print("🎨 Collaborative Whiteboard - Simple Deployment")
    print("=" * 50)
    
    print("\n🚀 STEP 1: Deploy Backend")
    print("1. Go to https://railway.app and sign up")
    print("2. Click 'New Project' → 'Deploy from GitHub repo'")
    print("3. Select this repository")
    print("4. Add Redis: Click 'New' → 'Database' → 'Add Redis'")
    print("5. Wait for deployment to complete")
    
    backend_url = input("\n📝 Enter your Railway app URL (e.g., your-app.railway.app): ").strip()
    if backend_url.startswith('https://'):
        backend_url = backend_url[8:]  # Remove https://
    if backend_url.startswith('http://'):
        backend_url = backend_url[7:]   # Remove http://
    
    print(f"\n✅ Backend URL: {backend_url}")
    
    print("\n🌐 STEP 2: Update Frontend Configuration")
    print("Edit frontend/canvas.js and change line 19:")
    print(f'const BACKEND_URL = "{backend_url}"  // Your Railway URL')
    
    print("\n📄 STEP 3: Deploy Frontend to GitHub Pages")
    print("1. Create new repository: 'whiteboard-frontend'")
    print("2. Upload all files from 'frontend/' folder")
    print("3. Go to Settings → Pages")
    print("4. Source: Deploy from branch, main, / (root)")
    print("5. Click Save")
    
    github_username = input("\n📝 Enter your GitHub username: ").strip()
    frontend_url = f"https://{github_username}.github.io/whiteboard-frontend"
    
    print(f"\n🎉 DEPLOYMENT COMPLETE!")
    print("=" * 50)
    print(f"Backend: https://{backend_url}")
    print(f"Frontend: {frontend_url}")
    print(f"\n📋 Next steps:")
    print(f"1. Update BACKEND_URL in canvas.js to: {backend_url}")
    print(f"2. Upload frontend files to GitHub Pages")
    print(f"3. Test at: {frontend_url}")
    print(f"4. Share with friends!")
    
    print(f"\n🎯 Different rooms:")
    print(f"   {frontend_url}?room=design")
    print(f"   {frontend_url}?room=meeting")
    print(f"   {frontend_url}?room=brainstorm")

if __name__ == "__main__":
    main()