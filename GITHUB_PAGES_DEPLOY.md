# Deploy to GitHub Pages - Step by Step

## Step 1: Create GitHub Account (if you don't have one)

1. Go to https://github.com/signup
2. Create your account
3. Verify your email

---

## Step 2: Create New Repository

1. Go to https://github.com/new
2. Fill in:
   - **Repository name:** `whiteboard`
   - **Description:** "Collaborative whiteboard app"
   - **Public** (must be public for free GitHub Pages)
   - ✅ Check "Add a README file"
3. Click **Create repository**

---

## Step 3: Upload Frontend Files

1. In your new repo, click **Add file** → **Upload files**

2. Drag and drop these files from your `frontend` folder:
   - `index.html`
   - `canvas.js`
   - `README.md`

3. Scroll down and click **Commit changes**

---

## Step 4: Enable GitHub Pages

1. Click **Settings** tab (top of repo)
2. Click **Pages** in left sidebar
3. Under "Source":
   - Branch: **main**
   - Folder: **/ (root)**
4. Click **Save**

5. Wait 1-2 minutes for deployment

6. Refresh the page - you'll see:
   ```
   Your site is live at https://YOUR-USERNAME.github.io/whiteboard/
   ```

---

## Step 5: Start Backend ngrok

Open terminal:
```bash
ngrok http 8000
```

Copy the URL (e.g., `abc123-xyz.ngrok-free.app`)

---

## Step 6: Update canvas.js on GitHub

1. In your GitHub repo, click **canvas.js**
2. Click the **pencil icon** (Edit this file)
3. Find line 20:
   ```javascript
   const BACKEND_URL = "localhost:8000"
   ```
4. Change to your ngrok URL:
   ```javascript
   const BACKEND_URL = "abc123-xyz.ngrok-free.app"
   ```
5. Scroll down and click **Commit changes**
6. Wait 30 seconds for GitHub Pages to update

---

## Step 7: Test!

1. Open your GitHub Pages URL:
   ```
   https://YOUR-USERNAME.github.io/whiteboard/
   ```

2. Press F12 to open console
3. Should see: "✅ Connected to room: room1"
4. Try drawing!

---

## Step 8: Share with Friends

Send them your GitHub Pages URL:
```
https://YOUR-USERNAME.github.io/whiteboard/
```

They can:
- Draw together in real-time
- Create different rooms with `?room=name`
- Use on desktop or mobile

---

## When ngrok URL Changes

Every time you restart ngrok, you get a new URL. To update:

1. Get new ngrok URL
2. Go to GitHub repo
3. Edit `canvas.js`
4. Update line 20 with new URL
5. Commit changes
6. Wait 30 seconds

That's it! Your frontend URL stays the same forever.

---

## Alternative: Use Git Command Line

If you prefer command line:

```bash
cd frontend
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/whiteboard.git
git push -u origin main
```

Then enable Pages in Settings.

---

## Troubleshooting

**"404 - There isn't a GitHub Pages site here"**
- Wait 2-3 minutes after enabling Pages
- Check Settings → Pages shows "Your site is live"
- Make sure repo is Public

**"Can't connect to backend"**
- Check ngrok is running: `ngrok http 8000`
- Verify BACKEND_URL in canvas.js matches ngrok URL
- No `https://` prefix in BACKEND_URL

**"Changes not showing"**
- Wait 30-60 seconds after commit
- Hard refresh: Ctrl+Shift+R (or Cmd+Shift+R on Mac)
- Check commit went through on GitHub

---

## Current Status

✅ Backend running: `docker-compose up`
✅ Backend ngrok ready: `ngrok http 8000`
⏳ Frontend: Deploy to GitHub Pages (follow steps above)

Once deployed, you'll have:
- Permanent frontend URL (never changes)
- Only need 1 ngrok tunnel (for backend)
- No ngrok warning page for users
- Free forever!
