# Single ngrok Solution

## The Problem
Free ngrok only allows 1 tunnel at a time, but we need both frontend and backend accessible.

## Solution Options

### Option 1: Use Backend ngrok Only (Simplest)

Since you can only run one ngrok, use it for the backend and access frontend locally.

**Step 1: Start backend ngrok**
```bash
ngrok http 8000
```

Copy the URL (e.g., `abc123.ngrok-free.app`)

**Step 2: Update canvas.js**
```javascript
const BACKEND_URL = "abc123.ngrok-free.app"  // Your backend ngrok URL
```

**Step 3: Start frontend locally**
```bash
cd frontend
python -m http.server 3000
```

**Step 4: Share via screen share or deploy frontend**

Since you can't share the frontend via ngrok, you have two options:

A. **Screen share** - Share your screen on Zoom/Teams/Discord while others watch
B. **Deploy frontend** - Upload to GitHub Pages (free, takes 2 minutes)

---

### Option 2: Deploy Frontend to GitHub Pages (Recommended)

This is FREE and takes 2 minutes!

**Step 1: Create GitHub repo**
1. Go to https://github.com/new
2. Name it: `whiteboard`
3. Create repository

**Step 2: Upload frontend folder**
1. Click "uploading an existing file"
2. Drag all files from `frontend` folder
3. Commit

**Step 3: Enable GitHub Pages**
1. Go to Settings → Pages
2. Source: Deploy from branch
3. Branch: main
4. Folder: / (root)
5. Save

**Step 4: Get your URL**
Wait 1-2 minutes, then visit:
```
https://YOUR-USERNAME.github.io/whiteboard/
```

**Step 5: Update canvas.js on GitHub**
1. Click `canvas.js` on GitHub
2. Click edit (pencil icon)
3. Change line 19:
```javascript
const BACKEND_URL = "your-backend-ngrok.ngrok-free.app"
```
4. Commit changes

**Step 6: Share!**
- Backend ngrok: `ngrok http 8000` (keep running)
- Share GitHub Pages URL with friends
- Everyone can draw together!

**Benefits:**
- ✅ Frontend URL never changes
- ✅ No ngrok warning page for frontend
- ✅ Only need 1 ngrok for backend
- ✅ Completely free

---

### Option 3: Use Localhost for Backend (Testing Only)

If you're just testing with people on the same WiFi:

**Step 1: Find your local IP**
```bash
ipconfig
```
Look for IPv4 Address (e.g., `192.168.1.100`)

**Step 2: Update canvas.js**
```javascript
const BACKEND_URL = "192.168.1.100:8000"  // Your local IP
```

**Step 3: Start frontend**
```bash
cd frontend
python -m http.server 3000
```

**Step 4: Share with friends on same WiFi**
```
http://192.168.1.100:3000
```

**Limitations:**
- ❌ Only works on same WiFi network
- ❌ Won't work over internet

---

## Recommended Setup

**For testing with friends over internet:**

1. **Backend:** `ngrok http 8000` (keep running)
2. **Frontend:** Deploy to GitHub Pages (one-time setup)
3. **Update:** Change BACKEND_URL in GitHub when ngrok URL changes

**For local testing:**
1. **Backend:** `docker-compose up`
2. **Frontend:** `python -m http.server 3000` in frontend folder
3. **canvas.js:** Use `localhost:8000`
4. **Access:** `http://localhost:3000`

---

## Quick Start (GitHub Pages Method)

```bash
# Terminal 1: Backend
docker-compose up

# Terminal 2: Backend ngrok
ngrok http 8000
# Copy the URL

# Terminal 3: Update and deploy
cd frontend
# Edit canvas.js line 19 with your ngrok URL
# Upload to GitHub Pages (see steps above)

# Share GitHub Pages URL with friends!
```

---

## Need Help?

If you want to use GitHub Pages, I can help you:
1. Create the repo
2. Upload files
3. Configure it

Just let me know!
