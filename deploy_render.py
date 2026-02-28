#!/usr/bin/env python3
"""
Deploy to Render - Step by step guide
"""

def main():
    print("🎨 Deploy to Render - Free Alternative to Railway")
    print("=" * 50)
    
    print("\n🚀 STEP 1: Create Render Account")
    print("1. Go to https://render.com")
    print("2. Sign up with GitHub (free)")
    print("3. Verify your email")
    
    print("\n🐳 STEP 2: Deploy Backend")
    print("1. Click 'New +' → 'Web Service'")
    print("2. Connect your GitHub repository")
    print("3. Configure:")
    print("   - Name: whiteboard-backend")
    print("   - Environment: Docker")
    print("   - Dockerfile Path: backend/Dockerfile")
    print("   - Build Context: backend")
    print("   - Plan: Free")
    
    print("\n🗄️ STEP 3: Add Redis Database")
    print("1. Click 'New +' → 'Redis'")
    print("2. Name: whiteboard-redis")
    print("3. Plan: Free (25MB)")
    print("4. Create Redis instance")
    
    print("\n🔗 STEP 4: Connect Redis to Backend")
    print("1. Go to your web service")
    print("2. Click 'Environment'")
    print("3. Add environment variable:")
    print("   - Key: REDIS_URL")
    print("   - Value: [Copy from Redis instance connection string]")
    
    print("\n⏳ STEP 5: Wait for Deployment")
    print("1. Deployment takes 2-5 minutes")
    print("2. Check logs for any errors")
    print("3. Your backend URL will be: https://your-app-name.onrender.com")
    
    backend_url = input("\n📝 Enter your Render app URL (e.g., whiteboard-backend.onrender.com): ").strip()
    if backend_url.startswith('https://'):
        backend_url = backend_url[8:]
    
    print(f"\n✅ Backend URL: {backend_url}")
    print(f"\n🔧 STEP 6: Update Frontend")
    print(f"Run: python update_backend_url.py {backend_url}")
    
    print(f"\n📄 STEP 7: Deploy Frontend to GitHub Pages")
    print(f"1. Create repository: whiteboard-frontend")
    print(f"2. Upload frontend files")
    print(f"3. Enable GitHub Pages")
    
    print(f"\n🎉 You're Done!")
    print(f"Backend: https://{backend_url}")
    print(f"Frontend: https://username.github.io/whiteboard-frontend")

if __name__ == "__main__":
    main()