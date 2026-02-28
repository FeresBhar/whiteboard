const canvas = document.getElementById("board")
const ctx = canvas.getContext("2d")

canvas.width = 1200
canvas.height = 800

let currentPage = 1
let totalPages = 1
let zoom = 1
let panX = 0
let panY = 0
let drawing = false
let strokes = {}
let currentColor = "#000000"
let currentThickness = 2

let animationFrameId = null
let needsRender = true
let lastRenderTime = 0
const RENDER_THROTTLE = 16 // ~60fps

// Configure your backend URL here
// For Railway: "your-app-name.railway.app"
// For Render: "your-app-name.onrender.com"
// For local testing: "localhost:8000"
const BACKEND_URL = "fd38-196-176-254-74.ngrok-free.app"  // Updated automatically

let currentRoom = new URLSearchParams(window.location.search).get('room') || 'room1'

// Auto-detect protocol based on URL
const isSecure = BACKEND_URL.includes('.railway.app') || 
                BACKEND_URL.includes('.onrender.com') || 
                BACKEND_URL.includes('.fly.dev') ||
                BACKEND_URL.includes('ngrok') ||
                window.location.protocol === 'https:'

const protocol = isSecure ? "wss" : "ws"
let wsUrl = `${protocol}://${BACKEND_URL}/ws/${currentRoom}`

let ws = null
let reconnectAttempts = 0
const maxReconnectAttempts = 5

function connectWebSocket() {
  wsUrl = `${protocol}://${BACKEND_URL}/ws/${currentRoom}`
  ws = new WebSocket(wsUrl)
  
  ws.onopen = () => {
    console.log('✅ Connected to room:', currentRoom)
    console.log('WebSocket URL:', wsUrl)
    reconnectAttempts = 0
    document.getElementById('connectionStatus').textContent = `🟢 ${currentRoom}`
    document.getElementById('connectionStatus').style.color = '#27ae60'
    
    // Update room selector
    document.getElementById('roomSelect').value = currentRoom
    
    // Clear local strokes when switching rooms
    strokes = {}
    currentPage = 1
    totalPages = 1
    requestRender()
  }
  
  ws.onerror = (error) => {
    console.error('❌ WebSocket error:', error)
    document.getElementById('connectionStatus').textContent = '🔴 Connection Error'
    document.getElementById('connectionStatus').style.color = '#e74c3c'
  }
  
  ws.onclose = () => {
    console.log('WebSocket closed')
    document.getElementById('connectionStatus').textContent = '🟡 Disconnected'
    document.getElementById('connectionStatus').style.color = '#f39c12'
    
    // Try to reconnect
    if (reconnectAttempts < maxReconnectAttempts) {
      reconnectAttempts++
      console.log(`Reconnecting... (${reconnectAttempts}/${maxReconnectAttempts})`)
      setTimeout(connectWebSocket, 2000)
    }
  }
  
  ws.onmessage = handleMessage
}

connectWebSocket()

// Optimized rendering with throttling
function requestRender() {
  if (!needsRender) {
    needsRender = true
    if (animationFrameId) {
      cancelAnimationFrame(animationFrameId)
    }
    animationFrameId = requestAnimationFrame(renderThrottled)
  }
}

function renderThrottled(timestamp) {
  if (timestamp - lastRenderTime >= RENDER_THROTTLE) {
    render()
    lastRenderTime = timestamp
    needsRender = false
  } else {
    animationFrameId = requestAnimationFrame(renderThrottled)
  }
}

function render() {
  ctx.clearRect(0, 0, canvas.width, canvas.height)
  ctx.save()
  ctx.translate(panX, panY)
  ctx.scale(zoom, zoom)
  
  // Draw all strokes for current page
  const pageStrokes = strokes[currentPage] || []
  pageStrokes.forEach(stroke => {
    if (!stroke.points || stroke.points.length < 2) return
    ctx.strokeStyle = stroke.color
    ctx.lineWidth = stroke.thickness
    ctx.lineCap = "round"
    ctx.lineJoin = "round"
    ctx.beginPath()
    ctx.moveTo(stroke.points[0].x, stroke.points[0].y)
    for (let i = 1; i < stroke.points.length; i++) {
      ctx.lineTo(stroke.points[i].x, stroke.points[i].y)
    }
    ctx.stroke()
  })
  
  ctx.restore()
  
  // Update UI
  document.getElementById('pageNum').textContent = currentPage
  document.getElementById('zoomLevel').textContent = Math.round(zoom * 100)
  updatePageList()
}

function switchRoom(newRoom) {
  if (newRoom === currentRoom) return
  
  console.log(`Switching from ${currentRoom} to ${newRoom}`)
  
  // Close current connection
  if (ws) {
    ws.close()
  }
  
  // Update room and reconnect
  currentRoom = newRoom
  
  // Update URL without page reload
  const url = new URL(window.location)
  url.searchParams.set('room', newRoom)
  window.history.pushState({}, '', url)
  
  // Reconnect to new room
  connectWebSocket()
}

function renderPagePreview(pageNum) {
  const previewCanvas = document.createElement('canvas')
  previewCanvas.width = 160
  previewCanvas.height = 100
  const previewCtx = previewCanvas.getContext('2d')
  
  previewCtx.fillStyle = 'white'
  previewCtx.fillRect(0, 0, 160, 100)
  
  const pageStrokes = strokes[pageNum] || []
  const scaleX = 160 / 1200
  const scaleY = 100 / 800
  
  // Optimize preview rendering - limit strokes for performance
  const maxStrokes = 50 // Limit preview strokes for performance
  const strokesToRender = pageStrokes.slice(-maxStrokes)
  
  strokesToRender.forEach(stroke => {
    if (!stroke.points || stroke.points.length < 2) return
    previewCtx.strokeStyle = stroke.color
    previewCtx.lineWidth = Math.max(1, stroke.thickness * scaleX)
    previewCtx.lineCap = "round"
    previewCtx.lineJoin = "round"
    previewCtx.beginPath()
    previewCtx.moveTo(stroke.points[0].x * scaleX, stroke.points[0].y * scaleY)
    for (let i = 1; i < stroke.points.length; i++) {
      previewCtx.lineTo(stroke.points[i].x * scaleX, stroke.points[i].y * scaleY)
    }
    previewCtx.stroke()
  })
  
  return previewCanvas
}

function updatePageList() {
  const pageList = document.getElementById('pageList')
  pageList.innerHTML = ''
  
  for (let i = 1; i <= totalPages; i++) {
    const pageItem = document.createElement('div')
    pageItem.className = 'page-item' + (i === currentPage ? ' active' : '')
    
    const preview = renderPagePreview(i)
    preview.className = 'page-preview'
    
    const pageNumber = document.createElement('div')
    pageNumber.className = 'page-number'
    pageNumber.textContent = `Page ${i}`
    
    const deleteBtn = document.createElement('button')
    deleteBtn.className = 'page-delete'
    deleteBtn.textContent = '×'
    deleteBtn.onclick = (e) => {
      e.stopPropagation()
      if (totalPages > 1 && confirm(`Delete page ${i}?`)) {
        deletePage(i)
      }
    }
    
    pageItem.appendChild(preview)
    pageItem.appendChild(pageNumber)
    if (totalPages > 1) pageItem.appendChild(deleteBtn)
    
    pageItem.onclick = () => {
      currentPage = i
      ws.send(JSON.stringify({ type: 'page_change', page: i }))
      requestRender()
    }
    
    pageList.appendChild(pageItem)
  }
}

function deletePage(pageNum) {
  if (totalPages <= 1) return
  
  // Remove page from strokes
  delete strokes[pageNum]
  
  // Shift pages down
  for (let i = pageNum + 1; i <= totalPages; i++) {
    strokes[i - 1] = strokes[i]
  }
  delete strokes[totalPages]
  
  totalPages--
  
  if (currentPage > totalPages) {
    currentPage = totalPages
  }
  
  ws.send(JSON.stringify({ type: 'delete_page', page: pageNum }))
  requestRender()
}

function handleMessage(e) {
  const msg = JSON.parse(e.data)
  
  if (msg.type === 'draw') {
    const page = msg.page
    if (!strokes[page]) strokes[page] = []
    
    let stroke = strokes[page].find(s => s.id === msg.stroke_id)
    if (!stroke) {
      stroke = { id: msg.stroke_id, color: msg.color, thickness: msg.thickness, points: [] }
      strokes[page].push(stroke)
    }
    stroke.points.push({ x: msg.x, y: msg.y })
    
    if (page > totalPages) totalPages = page
    
    if (page === currentPage) {
      requestRender()
    } else {
      // Only update page list if not on current page (less frequent)
      setTimeout(updatePageList, 100)
    }
  } else if (msg.type === 'undo') {
    if (strokes[msg.page] && strokes[msg.page].length > 0) {
      strokes[msg.page].pop()
      if (msg.page === currentPage) {
        requestRender()
      } else {
        setTimeout(updatePageList, 100)
      }
    }
  } else if (msg.type === 'page_change') {
    currentPage = msg.page
    if (msg.page > totalPages) totalPages = msg.page
    requestRender()
  } else if (msg.type === 'clear') {
    strokes[msg.page] = []
    if (msg.page === currentPage) {
      requestRender()
    } else {
      setTimeout(updatePageList, 100)
    }
  } else if (msg.type === 'delete_page') {
    deletePage(msg.page)
  }
}

let currentStrokeId = null
let localStrokeBuffer = []
let sendInterval = null

function startDrawing(e) {
  if (!ws || ws.readyState !== WebSocket.OPEN) {
    console.error('WebSocket not connected')
    return
  }
  
  drawing = true
  currentStrokeId = Date.now().toString() + Math.random()
  localStrokeBuffer = []
  const { x, y } = getCanvasCoords(e)
  
  // Send to server immediately
  ws.send(JSON.stringify({
    type: 'draw',
    page: currentPage,
    stroke_id: currentStrokeId,
    x, y,
    color: currentColor,
    thickness: currentThickness
  }))
  
  // Start batching for smoother performance - reduced frequency for less lag
  sendInterval = setInterval(() => {
    if (localStrokeBuffer.length > 0 && ws && ws.readyState === WebSocket.OPEN) {
      // Send in smaller batches to reduce lag
      const batchSize = Math.min(3, localStrokeBuffer.length)
      const batch = localStrokeBuffer.splice(0, batchSize)
      
      batch.forEach(point => {
        ws.send(JSON.stringify({
          type: 'draw',
          page: currentPage,
          stroke_id: currentStrokeId,
          x: point.x,
          y: point.y,
          color: currentColor,
          thickness: currentThickness
        }))
      })
    }
  }, 80) // Reduced frequency from 50ms to 80ms for less network traffic
}

function continueDrawing(e) {
  if (!drawing) return
  const { x, y } = getCanvasCoords(e)
  
  // Buffer for sending - limit buffer size to prevent lag
  if (localStrokeBuffer.length < 10) {
    localStrokeBuffer.push({ x, y })
  }
}

function stopDrawing() {
  if (!drawing) return
  drawing = false
  
  if (sendInterval) {
    clearInterval(sendInterval)
    sendInterval = null
  }
  
  // Send any remaining buffered points
  if (localStrokeBuffer.length > 0 && currentStrokeId && ws && ws.readyState === WebSocket.OPEN) {
    localStrokeBuffer.forEach(point => {
      ws.send(JSON.stringify({
        type: 'draw',
        page: currentPage,
        stroke_id: currentStrokeId,
        x: point.x,
        y: point.y,
        color: currentColor,
        thickness: currentThickness
      }))
    })
    localStrokeBuffer = []
  }
  
  currentStrokeId = null
}

function getCanvasCoords(e) {
  const rect = canvas.getBoundingClientRect()
  const x = (e.clientX - rect.left - panX) / zoom
  const y = (e.clientY - rect.top - panY) / zoom
  return { x, y }
}

canvas.addEventListener('mousedown', startDrawing)
canvas.addEventListener('mousemove', continueDrawing)
canvas.addEventListener('mouseup', stopDrawing)
canvas.addEventListener('mouseleave', stopDrawing)

// Touch support for mobile
canvas.addEventListener('touchstart', e => {
  e.preventDefault()
  const touch = e.touches[0]
  const mouseEvent = new MouseEvent('mousedown', {
    clientX: touch.clientX,
    clientY: touch.clientY
  })
  canvas.dispatchEvent(mouseEvent)
})

canvas.addEventListener('touchmove', e => {
  e.preventDefault()
  const touch = e.touches[0]
  const mouseEvent = new MouseEvent('mousemove', {
    clientX: touch.clientX,
    clientY: touch.clientY
  })
  canvas.dispatchEvent(mouseEvent)
})

canvas.addEventListener('touchend', e => {
  e.preventDefault()
  const mouseEvent = new MouseEvent('mouseup', {})
  canvas.dispatchEvent(mouseEvent)
})

canvas.addEventListener('wheel', e => {
  e.preventDefault()
  const delta = e.deltaY > 0 ? 0.9 : 1.1
  zoom = Math.max(0.1, Math.min(5, zoom * delta))
  requestRender()
})

function setupEventListeners() {
  document.getElementById('zoomIn').addEventListener('click', () => {
    zoom = Math.min(5, zoom * 1.2)
    requestRender()
  })

  document.getElementById('zoomOut').addEventListener('click', () => {
    zoom = Math.max(0.1, zoom / 1.2)
    requestRender()
  })

  document.getElementById('undo').addEventListener('click', () => {
    if (ws && ws.readyState === WebSocket.OPEN) {
      ws.send(JSON.stringify({ type: 'undo', page: currentPage }))
    }
  })

  document.getElementById('clear').addEventListener('click', () => {
    if (confirm('Clear this page?')) {
      if (ws && ws.readyState === WebSocket.OPEN) {
        ws.send(JSON.stringify({ type: 'clear', page: currentPage }))
      }
    }
  })

  document.getElementById('addPage').addEventListener('click', () => {
    totalPages++
    currentPage = totalPages
    if (ws && ws.readyState === WebSocket.OPEN) {
      ws.send(JSON.stringify({ type: 'page_change', page: currentPage }))
    }
    requestRender()
  })

  document.getElementById('colorPicker').addEventListener('change', e => {
    currentColor = e.target.value
  })

  document.getElementById('thickness').addEventListener('change', e => {
    currentThickness = parseInt(e.target.value)
  })

  // Room selector functionality
  document.getElementById('joinRoom').addEventListener('click', () => {
    const selectedRoom = document.getElementById('roomSelect').value
    switchRoom(selectedRoom)
  })

  document.getElementById('roomSelect').addEventListener('change', (e) => {
    const selectedRoom = e.target.value
    switchRoom(selectedRoom)
  })
}

// Setup event listeners when DOM is ready
setupEventListeners()

// Initial render
requestRender()