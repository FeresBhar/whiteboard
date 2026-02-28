# Deploy Your Whiteboard for FREE - Complete Guide

## 🚀 Quick Deploy (5 minutes)

### Option 1: Railway + GitHub Pages (Easiest)

**Step 1: Deploy Backend to Railway**
1. Go to [railway.app](https://railway.app) and sign up with GitHub
2. Click "New Project" → "Deploy from GitHub repo"
3. Select this repository
4. Railway will auto-detect Docker and deploy!
5. Add Redis: Click "New" → "Database" → "Add Redis"
6. Copy your app URL (e.g., `your-app.railway.app`)

**Step 2: Deploy Frontend to GitHub Pages**
1. Create new GitHub repo called `whiteboard-frontend`
2. Upload files from `frontend/` folder
3. Go to Settings → Pages → Enable (Source: Deploy from branch, main, root)
4. Edit `canvas.js` on GitHub:
   ```javascript
   const BACKEND_URL = "your-app.railway.app"  // Your Railway URL
   ```
5. Commit changes

**Done!** Share your GitHub Pages URL with friends.

---

### Option 2: Render (Alternative)

**Backend:**
1. Go to [render.com](https://render.com) and sign up
2. New → Web Service → Connect your repo
3. Settings:
   - Environment: Docker
   - Dockerfile Path: `backend/Dockerfile`
   - Build Context: `backend`
4. Add Redis: New → Redis → Create
5. Copy your app URL

**Frontend:** Same as GitHub Pages above

---

### Option 3: Fly.io (Advanced)

```bash
# Install flyctl first
curl -L https://fly.io/install.sh | sh

# In your project root:
fly launch --dockerfile backend/Dockerfile
fly deploy
```

---

## 🔧 Local Development

**Start everything:**
```bash
# Terminal 1: Backend
docker-compose up

# Terminal 2: Frontend  
cd frontend
python -m http.server 3000
```

Open: `http://localhost:3000`

---

## 🌐 Production URLs

After deployment, your URLs will be:
- **Backend**: `https://your-app.railway.app` (API + WebSocket)
- **Frontend**: `https://username.github.io/whiteboard-frontend` (Static site)

**Benefits:**
- ✅ Completely free forever
- ✅ No expiring URLs
- ✅ Professional domains
- ✅ HTTPS/WSS secure connections
- ✅ Global CDN for frontend
- ✅ Auto-scaling backend

---

## 🎯 Features

- **Real-time collaboration** - Multiple users draw together
- **Multi-page support** - Create unlimited pages
- **Room system** - Add `?room=teamname` for private rooms
- **Mobile friendly** - Touch drawing support
- **Persistent storage** - Drawings saved in Redis
- **Zoom & pan** - Mouse wheel or buttons
- **Undo/Clear** - Per-page controls
- **Color picker** - Any color
- **Brush thickness** - 1-20px

---

## 🔄 Updating Your App

**Backend changes:**
1. Push to GitHub
2. Railway/Render auto-deploys

**Frontend changes:**
1. Edit files on GitHub directly
2. Or push to your frontend repo
3. GitHub Pages updates automatically

---

## 🐛 Troubleshooting

**"Can't connect to backend"**
- Check BACKEND_URL in canvas.js matches your deployed URL
- No `https://` prefix in BACKEND_URL
- Make sure backend is deployed and running

**"WebSocket connection failed"**
- Backend must support WSS for HTTPS frontends
- Check browser console for exact error
- Verify backend health at `https://your-backend-url/health`

**"Drawing doesn't sync"**
- Check Redis is connected to backend
- Multiple users must be in same room
- Check browser console for WebSocket messages

---

## 💡 Pro Tips

**Custom domains:**
- Railway: Add custom domain in settings (free)
- GitHub Pages: Add CNAME file with your domain

**Environment variables:**
- Set `REDIS_URL` in Railway/Render dashboard
- Backend auto-detects cloud Redis

**Scaling:**
- Railway: Auto-scales based on usage
- Render: Upgrade to paid for more resources
- Both handle thousands of concurrent users on free tier

**Monitoring:**
- Railway: Built-in metrics dashboard
- Render: Logs and metrics in dashboard
- Add health checks at `/health` endpoint

---

## 🎉 Share Your Whiteboard

Send friends your GitHub Pages URL:
```
https://yourusername.github.io/whiteboard-frontend/
```

Different rooms:
```
https://yourusername.github.io/whiteboard-frontend/?room=design
https://yourusername.github.io/whiteboard-frontend/?room=meeting
```

Everyone can draw together in real-time!

---

## 📱 Mobile Support

Works perfectly on phones and tablets:
- Touch to draw
- Pinch to zoom
- Responsive design
- Same features as desktop

---

## 🔒 Security

- CORS enabled for your frontend domain
- WSS encrypted WebSocket connections
- No authentication required (add if needed)
- Redis data isolated by room

---

## Next Steps

1. **Deploy backend** to Railway/Render (5 minutes)
2. **Deploy frontend** to GitHub Pages (2 minutes)  
3. **Update BACKEND_URL** in canvas.js
4. **Test and share!**

Your whiteboard will be live at a permanent URL that never expires!