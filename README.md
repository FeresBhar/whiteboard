# 🎨 Collaborative Whiteboard

A real-time collaborative whiteboard application that allows multiple users to draw together in real-time. Built with FastAPI, WebSockets, Redis, and vanilla JavaScript.

![Whiteboard Demo](https://img.shields.io/badge/Status-Ready%20to%20Deploy-brightgreen)
![Docker](https://img.shields.io/badge/Docker-Supported-blue)
![Free Hosting](https://img.shields.io/badge/Hosting-Free%20Options-success)

## ✨ Features

- **Real-time collaboration** - Multiple users can draw simultaneously
- **Multi-page support** - Create and manage multiple pages
- **Room system** - Private rooms with URL parameters (`?room=teamname`)
- **Touch support** - Works on mobile devices and tablets
- **Persistent storage** - Drawings are saved and restored
- **Zoom & Pan** - Navigate large canvases easily
- **Undo/Redo** - Per-page undo functionality
- **Color picker** - Choose any color for drawing
- **Brush thickness** - Adjustable brush size (1-20px)
- **Page management** - Add, delete, and switch between pages

## 🚀 Quick Start (Local)

### Prerequisites
- Docker and Docker Compose
- Python 3.7+ (for frontend server)

### Run Locally
```bash
# 1. Start backend services
docker-compose up

# 2. Start frontend (new terminal)
cd frontend
python -m http.server 3000

# 3. Open browser
# http://localhost:3000
```

## 🌐 Deploy for FREE

### Option 1: Railway + GitHub Pages (Recommended)

**Backend (Railway):**
1. Go to [railway.app](https://railway.app) and sign up
2. New Project → Deploy from GitHub repo
3. Select this repository
4. Add Redis: New → Database → Add Redis
5. Copy your app URL (e.g., `your-app.railway.app`)

**Frontend (GitHub Pages):**
1. Create new repo: `whiteboard-frontend`
2. Upload files from `frontend/` folder
3. Settings → Pages → Enable
4. Edit `canvas.js` line 6:
   ```javascript
   const BACKEND_URL = "your-app.railway.app"
   ```

**Done!** Share your GitHub Pages URL.

### Option 2: Automated Deployment

Run the deployment script:
```bash
python deploy.py
```

This will guide you through the entire process step-by-step.

### Option 3: Other Platforms

- **Render**: Use `render.yaml` configuration
- **Fly.io**: Use `fly.toml` configuration  
- **Heroku**: Standard Docker deployment

See [DEPLOY_FREE.md](DEPLOY_FREE.md) for detailed instructions.

## 🏗️ Architecture

```
Frontend (GitHub Pages)     Backend (Railway/Render)
┌─────────────────────┐    ┌──────────────────────┐
│  HTML/CSS/JS        │    │  FastAPI + WebSocket │
│  Static Hosting     │◄──►│  Real-time sync      │
│  Global CDN         │    │  Docker Container    │
└─────────────────────┘    └──────────────────────┘
                                      │
                           ┌──────────▼──────────┐
                           │  Redis Database     │
                           │  Persistent Storage │
                           └─────────────────────┘
```

## 📁 Project Structure

```
├── backend/
│   ├── main.py              # FastAPI application
│   ├── Dockerfile           # Backend container
│   ├── requirements.txt     # Python dependencies
│   ├── models/
│   │   └── draw_event.py    # Data models
│   ├── storage/
│   │   └── client.py        # Redis client
│   └── websocket/
│       └── manager.py       # WebSocket manager
├── frontend/
│   ├── index.html           # Main UI
│   ├── canvas.js            # Drawing logic
│   └── README.md            # Frontend docs
├── docker-compose.yml       # Local development
├── railway.json             # Railway deployment
├── render.yaml              # Render deployment
├── fly.toml                 # Fly.io deployment
├── deploy.py                # Automated deployment
└── DEPLOY_FREE.md           # Deployment guide
```

## 🎯 Usage

### Basic Drawing
- Click and drag to draw
- Use color picker to change colors
- Adjust brush thickness with slider
- Zoom with mouse wheel or buttons

### Multi-page Support
- View page thumbnails in sidebar
- Click thumbnail to switch pages
- Add new pages with "+" button
- Delete pages by hovering and clicking "×"

### Collaboration
- Share your URL with others
- Everyone sees changes in real-time
- Use different rooms: `?room=teamname`
- Works on desktop and mobile

### Room System
```
https://your-app.com/                    # Default room
https://your-app.com/?room=design        # Design team room
https://your-app.com/?room=meeting       # Meeting room
https://your-app.com/?room=brainstorm    # Brainstorm session
```

## 🔧 Configuration

### Environment Variables

**Backend:**
- `REDIS_URL`: Redis connection string (auto-detected in cloud)
- `PORT`: Server port (default: 8000)

**Frontend:**
- `BACKEND_URL`: Backend server URL (set in canvas.js)

### CORS Configuration
The backend allows all origins by default. For production, update `main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],  # Restrict to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 🐛 Troubleshooting

### Connection Issues
- Check `BACKEND_URL` in `canvas.js` matches your deployed backend
- Ensure no `https://` prefix in `BACKEND_URL`
- Verify backend is running at `/health` endpoint

### WebSocket Errors
- Use `wss://` for HTTPS frontends, `ws://` for HTTP
- Check browser console for detailed error messages
- Ensure Redis is connected to backend

### Drawing Not Syncing
- Multiple users must be in the same room
- Check WebSocket connection status in UI
- Verify Redis is storing data

### Mobile Issues
- Ensure `touch-action: none` is set on canvas
- Test touch events in browser dev tools
- Check viewport meta tag is present

## 🚀 Performance

### Optimization Features
- Batched WebSocket messages (50ms intervals)
- Canvas rendering optimizations
- Efficient Redis storage
- CDN delivery for frontend

### Scaling
- **Railway**: Auto-scales based on usage
- **Render**: Handles high concurrent connections
- **Redis**: Optimized for real-time data
- **Frontend**: Global CDN distribution

## 🔒 Security

- CORS protection
- WSS encrypted connections
- No authentication required (add if needed)
- Room-based data isolation
- Input validation on all endpoints

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally with `docker-compose up`
5. Submit a pull request

## 📄 License

MIT License - feel free to use for personal or commercial projects.

## 🎉 Demo

Try the live demo: [Your deployed URL here]

## 📞 Support

- Create an issue for bugs
- Check [DEPLOY_FREE.md](DEPLOY_FREE.md) for deployment help
- See [TESTING.md](TESTING.md) for testing instructions

---

**Made with ❤️ for collaborative creativity**