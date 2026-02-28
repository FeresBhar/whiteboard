#!/usr/bin/env python3
"""
Quick script to update the backend URL in canvas.js
"""

import sys
import os

def update_backend_url(new_url):
    """Update the BACKEND_URL in canvas.js"""
    canvas_js_path = "frontend/canvas.js"
    
    if not os.path.exists(canvas_js_path):
        print(f"❌ File not found: {canvas_js_path}")
        return False
    
    try:
        # Read the file with UTF-8 encoding
        with open(canvas_js_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the BACKEND_URL line
        lines = content.split('\n')
        updated = False
        
        for i, line in enumerate(lines):
            if 'const BACKEND_URL = ' in line and not line.strip().startswith('//'):
                old_line = line
                lines[i] = f'const BACKEND_URL = "{new_url}"  // Updated automatically'
                print(f"✅ Updated line {i+1}:")
                print(f"   Old: {old_line.strip()}")
                print(f"   New: {lines[i].strip()}")
                updated = True
                break
        
        if not updated:
            print("❌ Could not find BACKEND_URL line to update")
            return False
        
        # Write back to file with UTF-8 encoding
        with open(canvas_js_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        
        print(f"✅ Successfully updated {canvas_js_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating file: {e}")
        return False

def main():
    """Main function"""
    print("🔧 Update Backend URL in canvas.js")
    print("=" * 40)
    
    if len(sys.argv) > 1:
        # URL provided as command line argument
        backend_url = sys.argv[1]
    else:
        # Ask for URL interactively
        print("Enter your backend URL (without https://):")
        print("Examples:")
        print("  - your-app.railway.app")
        print("  - your-app.onrender.com")
        print("  - localhost:8000")
        print()
        backend_url = input("Backend URL: ").strip()
    
    # Clean up the URL
    if backend_url.startswith('https://'):
        backend_url = backend_url[8:]
    elif backend_url.startswith('http://'):
        backend_url = backend_url[7:]
    
    if not backend_url:
        print("❌ No URL provided")
        sys.exit(1)
    
    print(f"\n🎯 Updating to: {backend_url}")
    
    if update_backend_url(backend_url):
        print(f"\n🎉 Success! Your frontend is now configured to use:")
        print(f"   Backend: {backend_url}")
        print(f"\n📋 Next steps:")
        print(f"1. Test locally: python START_ALL.py")
        print(f"2. Or deploy frontend to GitHub Pages")
        print(f"3. Share your whiteboard with friends!")
    else:
        print(f"\n❌ Failed to update configuration")
        sys.exit(1)

if __name__ == "__main__":
    main()