# Backend Connection Check

## Step 1: Check if backend is accessible

Open your browser and go to:
```
http://localhost:8000
```

You should see:
```json
{"status":"ok"}
```

If you see this, backend is working! ✅

---

## Step 2: Check ngrok

Is ngrok still running? Check the terminal where you ran `ngrok http 8000`

You should see something like:
```
Session Status                online
Forwarding                    https://abc123.ngrok-free.app -> http://localhost:8000
```

**IMPORTANT:** The URL changes every time you restart ngrok!

---

## Step 3: Get your CURRENT ngrok URL

From the ngrok terminal, copy the URL (WITHOUT https://)

Example:
- ❌ Wrong: `https://20c2-196-176-254-74.ngrok-free.app`
- ✅ Correct: `20c2-196-176-254-74.ngrok-free.app`

---

## Step 4: Test ngrok backend

Open browser to your ngrok URL:
```
https://YOUR-NGROK-URL.ngrok-free.app
```

1. Click "Visit Site" on the warning page
2. You should see: `{"status":"ok"}`

If you see this, ngrok backend is working! ✅

---

## Step 5: Update canvas.js

Edit `frontend/canvas.js` line 17:

```javascript
const BACKEND_URL = "YOUR-CURRENT-NGROK-URL.ngrok-free.app"
```

Make sure:
- ❌ No `https://` at the start
- ❌ No trailing spaces
- ✅ Just the domain

---

## Step 6: Restart frontend

```bash
# Press Ctrl+C in frontend terminal
cd frontend
python -m http.server 3000
```

---

## Step 7: Test

1. Open browser: `http://localhost:3000`
2. Press F12 for console
3. You should see: "✅ Connected to room: room1"
4. Toolbar should show: "🟢 Connected"
5. Try drawing!

---

## If ngrok stopped:

Restart it:
```bash
ngrok http 8000
```

Copy the NEW URL and update canvas.js again.

---

## Alternative: Use localhost for testing

If you just want to test locally without ngrok:

Edit `frontend/canvas.js` line 17:
```javascript
const BACKEND_URL = "localhost:8000"
```

Then test on same computer:
- Open: `http://localhost:3000`
- Drawing should work!

This won't work for sharing with others, but good for testing.
