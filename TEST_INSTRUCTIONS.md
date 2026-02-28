# How to Test Your Whiteboard

## Current Setup Status
✅ Backend ngrok URL configured: `20c2-196-176-254-74.ngrok-free.app`

---

## Step 1: Make Sure Backend is Running

In your first terminal, you should see:
```
backend-1  | INFO:     Application startup complete.
```

And ngrok should show:
```
Forwarding  https://20c2-196-176-254-74.ngrok-free.app -> http://localhost:8000
```

---

## Step 2: Start Frontend Server

Open a NEW terminal and run:
```bash
cd frontend
python -m http.server 3000
```

OR double-click: `START_FRONTEND.bat`

You should see:
```
Serving HTTP on :: port 3000
```

---

## Step 3: Test Locally

1. Open your browser
2. Go to: **http://localhost:3000**
3. Press F12 to open console
4. You should see: "Connected to room: room1"
5. Try drawing on the canvas!

---

## Step 4: Share with Others

### Option A: Use ngrok for frontend (Recommended)

Open ANOTHER terminal:
```bash
ngrok http 3000
```

You'll get a URL like: `https://xyz789.ngrok-free.app`

**Share this URL with your friends!**

When they visit:
1. They might see an ngrok warning - click "Visit Site"
2. They'll see the whiteboard
3. Everyone can draw together in real-time!

### Option B: Use GitHub Pages

1. Create a new repo on GitHub
2. Upload everything in the `frontend` folder
3. Go to Settings → Pages
4. Enable Pages from main branch
5. Share the GitHub Pages URL

---

## Different Rooms

To create separate rooms, add `?room=roomname` to the URL:

- Design team: `http://localhost:3000?room=design`
- Dev team: `http://localhost:3000?room=dev`
- Meeting: `http://localhost:3000?room=meeting123`

Each room is completely separate!

---

## Troubleshooting

### Drawing doesn't work
1. Open browser console (F12)
2. Check for "Connected to room: room1" message
3. Look for any red errors
4. Make sure `canvas.js` has the correct ngrok URL (no https://, no trailing space)

### "WebSocket error" in console
- Backend ngrok might have stopped
- Check that ngrok is still running
- Restart ngrok and update the URL in `canvas.js`

### Can't see the whiteboard
- Make sure you're going to `http://localhost:3000` (frontend)
- NOT `https://20c2-196-176-254-74.ngrok-free.app` (that's the backend API)

### ngrok shows "status: ok"
- That's the backend API endpoint
- You need to serve the frontend separately with Python
- Then optionally use another ngrok tunnel for the frontend

---

## What You Should See

**Correct setup:**
- Terminal 1: `docker-compose up` (backend)
- Terminal 2: `ngrok http 8000` (backend tunnel)
- Terminal 3: `python -m http.server 3000` in frontend folder
- Terminal 4 (optional): `ngrok http 3000` (frontend tunnel for sharing)

**In browser:**
- Go to: `http://localhost:3000` or your frontend ngrok URL
- See: Whiteboard with toolbar and page sidebar
- Console: "Connected to room: room1"
- Drawing works!
