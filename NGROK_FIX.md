# Fix ngrok WebSocket Connection

## The Problem
ngrok's free tier shows a warning page that blocks WebSocket connections.

## Solutions

### Option 1: Skip ngrok Warning (Easiest)

When sharing the frontend ngrok URL with others, tell them:

1. Visit the URL
2. Click "Visit Site" button on the ngrok warning page
3. The whiteboard will load and WebSocket will connect
4. Drawing will work!

The warning only appears once per session.

---

### Option 2: Use ngrok Agent API (Better)

Add this to your ngrok command:

```bash
ngrok http 8000 --domain=your-static-domain.ngrok-free.app
```

You can get a free static domain from: https://dashboard.ngrok.com/cloud-edge/domains

Benefits:
- No warning page
- Same URL every time
- Better for sharing

---

### Option 3: Deploy to Production (Best)

**Backend (Railway - Free):**
1. Go to https://railway.app
2. New Project → Deploy from GitHub
3. Connect your repo
4. Railway auto-detects Docker
5. Get permanent URL like: `yourapp.railway.app`

**Frontend (Netlify - Free):**
1. Go to https://netlify.com
2. Drag & drop `frontend` folder
3. Get permanent URL like: `yourapp.netlify.app`

Update `canvas.js` with Railway URL:
```javascript
const BACKEND_URL = "yourapp.railway.app"
```

---

## Performance Improvements Added

✅ **Local drawing prediction** - Your strokes appear instantly
✅ **Batched updates** - Sends points every 50ms instead of every pixel
✅ **Auto-reconnect** - Reconnects if connection drops
✅ **Connection status indicator** - See connection state in toolbar

The lag should be much better now!

---

## Testing the Fix

1. Restart frontend server (Ctrl+C, then run again)
2. Refresh browser (Ctrl+F5)
3. Check toolbar - should show "🟢 Connected"
4. Drawing should feel smoother
5. Share ngrok URL - others click "Visit Site" on warning page

---

## Current Status

Your setup:
- Backend ngrok: `20c2-196-176-254-74.ngrok-free.app` ✅
- Frontend: `http://localhost:3000` ✅
- Connection status: Now visible in toolbar ✅
- Lag: Reduced with batching ✅
