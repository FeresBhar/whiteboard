# Testing Your Collaborative Whiteboard

## Quick Test (Same WiFi Network)

1. **Find your local IP address:**
   ```bash
   ipconfig
   ```
   Look for "IPv4 Address" under your active network adapter (e.g., `192.168.1.100`)

2. **Update the WebSocket URL in `frontend/canvas.js`:**
   
   Change line 13 from:
   ```javascript
   const ws = new WebSocket(`ws://localhost:8000/ws/${roomId}`)
   ```
   
   To (replace with YOUR IP):
   ```javascript
   const ws = new WebSocket(`ws://192.168.1.100:8000/ws/${roomId}`)
   ```

3. **Start a simple file server for the frontend:**
   ```bash
   cd frontend
   python -m http.server 3000
   ```

4. **Share with friends on same WiFi:**
   - Send them: `http://192.168.1.100:3000`
   - Different rooms: `http://192.168.1.100:3000?room=myroom`

---

## Internet Testing (ngrok - Easiest for Remote Users)

### Step 1: Install ngrok
- Download from https://ngrok.com/download
- Sign up for free account
- Follow their setup instructions

### Step 2: Expose your backend
```bash
ngrok http 8000
```

You'll see output like:
```
Forwarding  https://abc123.ngrok-free.app -> http://localhost:8000
```

### Step 3: Update frontend to use ngrok URL

Edit `frontend/canvas.js` line 13:
```javascript
const ws = new WebSocket(`wss://abc123.ngrok-free.app/ws/${roomId}`)
```
Note: Use `wss://` (secure WebSocket) for https URLs!

### Step 4: Host frontend

**Option A - Local file server:**
```bash
cd frontend
python -m http.server 3000
```
Then use another ngrok tunnel:
```bash
ngrok http 3000
```
Share the frontend ngrok URL with friends.

**Option B - Quick online hosting:**
- Upload `frontend/` folder to GitHub
- Enable GitHub Pages in repo settings
- Share the GitHub Pages URL

---

## Production Deployment (For Permanent Hosting)

### Backend Options:

**Railway (Recommended - Free tier available):**
1. Go to https://railway.app
2. Create new project → Deploy from GitHub
3. Add your repo
4. Railway auto-detects Docker
5. Copy the public URL (e.g., `https://yourapp.railway.app`)

**Render:**
1. Go to https://render.com
2. New → Web Service
3. Connect your repo
4. Select Docker environment
5. Copy the public URL

**Fly.io:**
```bash
# Install flyctl
# Then in your project root:
fly launch
fly deploy
```

### Frontend Options:

**Netlify (Easiest):**
1. Go to https://netlify.com
2. Drag & drop your `frontend` folder
3. Done! Get instant URL

**Vercel:**
1. Go to https://vercel.com
2. Import your GitHub repo
3. Set root directory to `frontend`
4. Deploy

**GitHub Pages:**
1. Push `frontend` folder to GitHub
2. Settings → Pages → Enable
3. Access at `https://yourusername.github.io/repo-name`

### Update WebSocket URL:

After deploying backend, update `frontend/canvas.js` line 13:
```javascript
const ws = new WebSocket(`wss://yourapp.railway.app/ws/${roomId}`)
```

---

## Features

- **Zoom**: Mouse wheel or +/- buttons
- **Undo**: Removes last stroke on current page
- **Multiple Pages**: Click previews in sidebar or use Add Page button
- **Delete Pages**: Hover over preview and click × button
- **Color Picker**: Choose any color
- **Thickness Slider**: Adjust brush size (1-20)
- **Clear Page**: Wipes current page only
- **Room Support**: Add `?room=yourroom` to URL for separate rooms

All changes sync in real-time across all connected users!

---

## Troubleshooting

**Drawing doesn't work:**
- Check browser console (F12) for errors
- Verify WebSocket connection shows "Connected to room"
- Make sure backend is running (`docker-compose up`)

**Can't connect from other devices:**
- Check firewall settings (allow port 8000)
- Verify you're on the same network
- Try disabling Windows Firewall temporarily to test

**ngrok connection issues:**
- Free ngrok URLs expire after 2 hours
- Restart ngrok and update the URL in canvas.js
- Make sure to use `wss://` for secure connections
