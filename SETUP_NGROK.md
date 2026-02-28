# Testing with ngrok - Step by Step

## Step 1: Start Your Backend

Make sure Docker containers are running:
```bash
docker-compose up
```

Wait until you see:
```
backend-1  | INFO:     Application startup complete.
```

---

## Step 2: Install and Setup ngrok

1. **Download ngrok:**
   - Go to https://ngrok.com/download
   - Download for Windows
   - Extract the zip file

2. **Sign up (free):**
   - Create account at https://dashboard.ngrok.com/signup
   - Copy your authtoken from https://dashboard.ngrok.com/get-started/your-authtoken

3. **Authenticate ngrok:**
   ```bash
   ngrok config add-authtoken YOUR_TOKEN_HERE
   ```

---

## Step 3: Expose Backend with ngrok

Open a NEW terminal and run:
```bash
ngrok http 8000
```

You'll see output like:
```
Forwarding  https://abc123-456-789.ngrok-free.app -> http://localhost:8000
```

**IMPORTANT:** Copy the full URL (e.g., `abc123-456-789.ngrok-free.app`)

---

## Step 4: Update Frontend Configuration

1. Open `frontend/canvas.js`
2. Find line 16 (around the top):
   ```javascript
   const BACKEND_URL = "localhost:8000"
   ```

3. Replace with your ngrok URL (WITHOUT https:// or wss://):
   ```javascript
   const BACKEND_URL = "abc123-456-789.ngrok-free.app"
   ```

4. Save the file

---

## Step 5: Host Frontend

Open ANOTHER terminal and run:
```bash
cd frontend
python -m http.server 3000
```

You should see:
```
Serving HTTP on :: port 3000 (http://[::]:3000/) ...
```

---

## Step 6: Test Locally First

1. Open your browser
2. Go to: `http://localhost:3000`
3. Open browser console (F12)
4. You should see: "Connected to room: room1"
5. Try drawing - it should work!

---

## Step 7: Share with Others

### Option A: Share via ngrok (Easiest)

Open a THIRD terminal:
```bash
ngrok http 3000
```

Copy the URL (e.g., `https://xyz789.ngrok-free.app`) and share it with friends!

### Option B: Share via GitHub Pages

1. Create a new GitHub repo
2. Upload the `frontend` folder
3. Go to Settings → Pages
4. Enable Pages from main branch
5. Share the GitHub Pages URL

---

## Testing with Multiple People

1. **Same room:** Everyone opens the same URL
   - They'll all see each other's drawings in real-time

2. **Different rooms:** Add `?room=roomname` to URL
   - Example: `https://xyz789.ngrok-free.app?room=team1`
   - Example: `https://xyz789.ngrok-free.app?room=team2`

---

## Troubleshooting

**"WebSocket error" in console:**
- Make sure backend ngrok is running
- Check that BACKEND_URL in canvas.js matches your ngrok URL exactly
- Don't include `https://` or `wss://` in BACKEND_URL

**Drawing doesn't appear:**
- Check browser console (F12) for errors
- Verify "Connected to room" message appears
- Try refreshing the page (Ctrl+F5)

**ngrok "Visit Site" button:**
- Free ngrok shows a warning page first
- Click "Visit Site" to continue
- This is normal for free tier

**Connection closes after 2 hours:**
- Free ngrok sessions expire
- Restart ngrok and update BACKEND_URL with new URL

---

## Quick Reference

**Three terminals you need:**

1. **Backend:** `docker-compose up`
2. **Backend ngrok:** `ngrok http 8000` → Copy URL to canvas.js
3. **Frontend server:** `cd frontend && python -m http.server 3000`
4. **Frontend ngrok (optional):** `ngrok http 3000` → Share this URL

**Files to edit:**
- `frontend/canvas.js` line 16: Update BACKEND_URL with ngrok URL (no protocol)
