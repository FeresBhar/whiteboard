# Testing Sync Between Devices

## What I Fixed

✅ **Removed local prediction** - All drawing now goes through server first
✅ **Fixed undo/clear buttons** - Added WebSocket ready checks
✅ **Added mobile touch support** - Drawing works on phones/tablets
✅ **Fixed sync issues** - Everyone sees the same thing now

---

## How to Test

### 1. Restart Everything

**Terminal 1 - Backend:**
```bash
docker-compose restart
```

**Terminal 2 - Backend ngrok:**
```bash
# Should already be running
ngrok http 8000
```

**Terminal 3 - Frontend:**
```bash
cd frontend
python -m http.server 3000
```

**Terminal 4 - Frontend ngrok (for sharing):**
```bash
ngrok http 3000
```

### 2. Test on Computer

1. Open browser: `http://localhost:3000`
2. Check console (F12): Should see "🟢 Connected"
3. Draw something
4. Click "Undo" - should remove last stroke
5. Click "Clear Page" - should clear everything

### 3. Test on Phone

1. Open the frontend ngrok URL on your phone
2. Click "Visit Site" on ngrok warning
3. Wait for "🟢 Connected" in toolbar
4. Draw something on phone
5. Should appear on computer immediately!

### 4. Test Sync

**Open 2 browser windows side by side:**
- Window 1: `http://localhost:3000`
- Window 2: `http://localhost:3000`

**Test these:**
- ✅ Draw in Window 1 → Appears in Window 2
- ✅ Draw in Window 2 → Appears in Window 1
- ✅ Click Undo in Window 1 → Removes stroke in both
- ✅ Click Clear in Window 2 → Clears both
- ✅ Add Page in Window 1 → New page in both
- ✅ Switch pages → Both stay in sync

---

## Common Issues

### "Drawing doesn't appear on other device"

**Check:**
1. Both devices show "🟢 Connected" in toolbar
2. Both are in the same room (check URL - should be same `?room=` parameter)
3. Browser console shows no errors (F12)

**Fix:**
- Refresh both devices (Ctrl+F5)
- Check that backend ngrok is still running
- Verify BACKEND_URL in canvas.js is correct

### "Buttons don't work"

**Check:**
1. Connection status shows "🟢 Connected"
2. Browser console for errors

**Fix:**
- Refresh page (Ctrl+F5)
- Make sure WebSocket connected before clicking buttons

### "Phone drawing is laggy"

This is normal with ngrok free tier:
- ngrok adds ~100-200ms latency
- Drawing goes: Phone → ngrok → server → ngrok → all devices
- For production, deploy to Railway/Render for better performance

### "Can't draw on phone"

**Check:**
1. Touch the canvas area (white part)
2. Make sure you clicked "Visit Site" on ngrok warning
3. Check connection status in toolbar

**Fix:**
- Refresh page
- Try landscape mode
- Check browser console for errors

---

## Expected Behavior

**Drawing:**
- Slight delay (100-200ms with ngrok) is normal
- Everyone sees strokes appear in real-time
- Strokes should be identical on all devices

**Buttons:**
- Undo removes last complete stroke for everyone
- Clear removes all strokes on current page for everyone
- Add Page creates new page for everyone
- Page switching syncs across all devices

**Mobile:**
- Touch and drag to draw
- Pinch to zoom (browser default)
- All features work same as desktop

---

## Performance Tips

1. **Reduce lag:** Deploy to production (Railway + Netlify)
2. **Better mobile:** Use landscape mode for more space
3. **Smoother drawing:** Close other apps on phone
4. **Faster sync:** Use same WiFi network when possible

---

## Next Steps

If everything works:
1. Share the frontend ngrok URL with friends
2. Tell them to click "Visit Site" on warning page
3. Everyone can draw together!

For permanent hosting:
- Backend → Railway (free tier)
- Frontend → Netlify (free tier)
- No more ngrok warnings or timeouts!
