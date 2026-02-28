# Correct ngrok Setup - Two Tunnels Required

## The Problem

You're using the frontend ngrok URL in BACKEND_URL. That's why you get 404 errors.

You need TWO separate ngrok tunnels running at the same time!

---

## Step-by-Step Setup

### Terminal 1: Backend (Docker)
```bash
docker-compose up
```
Leave this running. You should see:
```
backend-1  | INFO:     Application startup complete.
```

---

### Terminal 2: Backend ngrok (Port 8000)
```bash
ngrok http 8000
```

You'll see:
```
Forwarding  https://abc123-456.ngrok-free.app -> http://localhost:8000
```

**COPY THIS URL!** This is your BACKEND_URL.

Example: `abc123-456.ngrok-free.app` (without https://)

Test it: Open `https://abc123-456.ngrok-free.app` in browser
- Click "Visit Site"
- Should see: `{"status":"ok"}`

---

### Terminal 3: Frontend Server (Port 3000)
```bash
cd frontend
python -m http.server 3000
```

Leave this running.

---

### Terminal 4: Frontend ngrok (Port 3000)
```bash
ngrok http 3000
```

You'll see:
```
Forwarding  https://xyz789-012.ngrok-free.app -> http://localhost:3000
```

**COPY THIS URL!** This is what you share with friends.

---

## Update canvas.js

Edit `frontend/canvas.js` line 19:

```javascript
const BACKEND_URL = "abc123-456.ngrok-free.app"  // Use BACKEND ngrok (port 8000)
```

**IMPORTANT:** Use the port 8000 ngrok URL here, NOT the port 3000 one!

---

## Test

1. Restart frontend server (Ctrl+C, then run again)
2. Open browser: `http://localhost:3000`
3. Console should show: "✅ Connected to room: room1"
4. Try drawing - should work!

---

## Share with Others

Give them the FRONTEND ngrok URL (port 3000):
```
https://xyz789-012.ngrok-free.app
```

They will:
1. Click "Visit Site" on ngrok warning
2. See the whiteboard
3. Draw together in real-time!

---

## Summary

**Four terminals running:**
1. `docker-compose up` - Backend server
2. `ngrok http 8000` - Backend tunnel → Use in canvas.js
3. `python -m http.server 3000` - Frontend server
4. `ngrok http 3000` - Frontend tunnel → Share with friends

**Two ngrok URLs:**
- Backend (8000): Put in `canvas.js` BACKEND_URL
- Frontend (3000): Share with friends

---

## Current Status

Your frontend ngrok: `85b9-196-176-254-74.ngrok-free.app` (port 3000)

You need to:
1. Start backend ngrok: `ngrok http 8000`
2. Copy that URL (will be different)
3. Put it in canvas.js BACKEND_URL
4. Restart frontend server
5. Test!
