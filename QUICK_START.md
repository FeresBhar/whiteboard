# Quick Start - Test with ngrok

## Step 1: Start Backend
```bash
docker-compose up
```
Wait for: `INFO: Application startup complete.`

## Step 2: Install ngrok
1. Download: https://ngrok.com/download
2. Extract and run: `ngrok config add-authtoken YOUR_TOKEN`
   (Get token from: https://dashboard.ngrok.com/get-started/your-authtoken)

## Step 3: Expose Backend
Open NEW terminal:
```bash
ngrok http 8000
```

Copy the URL (e.g., `abc123-456.ngrok-free.app`) - WITHOUT `https://`

## Step 4: Update Frontend
Edit `frontend/canvas.js` line 16:
```javascript
const BACKEND_URL = "abc123-456.ngrok-free.app"  // Your ngrok URL here
```

## Step 5: Test Locally
```bash
cd frontend
python -m http.server 3000
```

Open browser: `http://localhost:3000`
Check console (F12): Should see "Connected to room: room1"
Try drawing!

## Step 6: Share with Others

### Option A: ngrok (easiest)
Open ANOTHER terminal:
```bash
ngrok http 3000
```
Share the URL with friends!

### Option B: GitHub Pages
1. Create GitHub repo
2. Upload `frontend` folder
3. Enable Pages in Settings
4. Share the Pages URL

---

## Testing
- Same room: Everyone uses same URL
- Different rooms: Add `?room=teamname` to URL
- Example: `https://xyz.ngrok-free.app?room=design`

## Troubleshooting
- Drawing doesn't work? Check BACKEND_URL in canvas.js matches your ngrok URL
- WebSocket error? Make sure backend ngrok is running
- Can't connect? Click "Visit Site" on ngrok warning page
