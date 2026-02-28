// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 DOM loaded, initializing whiteboard...');
    
    const canvas = document.getElementById("board");
    const ctx = canvas.getContext("2d");
    
    if (!canvas || !ctx) {
        console.error('❌ Canvas or context not found!');
        return;
    }
    
    canvas.width = 1200;
    canvas.height = 800;
    
    let currentPage = 1;
    let totalPages = 1;
    let zoom = 1;
    let panX = 0;
    let panY = 0;
    let drawing = false;
    let strokes = {};
    let currentColor = "#000000";
    let currentThickness = 2;
    
    // WebSocket setup
    const BACKEND_URL = "whiteboard-fs5m.onrender.com";
    let currentRoom = new URLSearchParams(window.location.search).get('room') || 'room1';
    const protocol = "wss";
    let wsUrl = `${protocol}://${BACKEND_URL}/ws/${currentRoom}`;
    let ws = null;
    
    // Drawing variables
    let currentStrokeId = null;
    let localStrokeBuffer = [];
    let sendInterval = null;
    
    function connectWebSocket() {
        console.log(`🔗 Connecting to: ${wsUrl}`);
        ws = new WebSocket(wsUrl);
        
        ws.onopen = () => {
            console.log('✅ WebSocket connected');
            const statusEl = document.getElementById('connectionStatus');
            if (statusEl) {
                statusEl.textContent = `🟢 ${currentRoom}`;
                statusEl.style.color = '#27ae60';
            }
        };
        
        ws.onerror = (error) => {
            console.error('❌ WebSocket error:', error);
        };
        
        ws.onclose = () => {
            console.log('🟡 WebSocket disconnected');
        };
        
        ws.onmessage = (e) => {
            console.log('📨 Received:', e.data);
            try {
                const msg = JSON.parse(e.data);
                handleMessage(msg);
            } catch (err) {
                console.error('❌ Error parsing message:', err);
            }
        };
    }
    
    function handleMessage(msg) {
        if (msg.type === 'draw') {
            const page = msg.page;
            if (!strokes[page]) strokes[page] = [];
            
            let stroke = strokes[page].find(s => s.id === msg.stroke_id);
            if (!stroke) {
                stroke = { 
                    id: msg.stroke_id, 
                    color: msg.color, 
                    thickness: msg.thickness, 
                    points: [] 
                };
                strokes[page].push(stroke);
            }
            stroke.points.push({ x: msg.x, y: msg.y });
            
            if (page === currentPage) {
                render();
            }
        }
    }
    
    function render() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        const pageStrokes = strokes[currentPage] || [];
        pageStrokes.forEach(stroke => {
            if (!stroke.points || stroke.points.length < 2) return;
            
            ctx.strokeStyle = stroke.color;
            ctx.lineWidth = stroke.thickness;
            ctx.lineCap = "round";
            ctx.lineJoin = "round";
            ctx.beginPath();
            ctx.moveTo(stroke.points[0].x, stroke.points[0].y);
            
            for (let i = 1; i < stroke.points.length; i++) {
                ctx.lineTo(stroke.points[i].x, stroke.points[i].y);
            }
            ctx.stroke();
        });
    }
    
    function getCanvasCoords(e) {
        const rect = canvas.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        return { x, y };
    }
    
    function startDrawing(e) {
        console.log('🖱️ Start drawing');
        
        if (!ws || ws.readyState !== WebSocket.OPEN) {
            console.error('❌ WebSocket not ready');
            return;
        }
        
        drawing = true;
        currentStrokeId = Date.now().toString() + Math.random();
        const { x, y } = getCanvasCoords(e);
        
        console.log(`📍 Drawing at: (${x}, ${y})`);
        
        // Send to server
        const message = {
            type: 'draw',
            page: currentPage,
            stroke_id: currentStrokeId,
            x, y,
            color: currentColor,
            thickness: currentThickness
        };
        
        console.log('📤 Sending:', message);
        ws.send(JSON.stringify(message));
    }
    
    function continueDrawing(e) {
        if (!drawing) return;
        
        const { x, y } = getCanvasCoords(e);
        
        if (ws && ws.readyState === WebSocket.OPEN) {
            ws.send(JSON.stringify({
                type: 'draw',
                page: currentPage,
                stroke_id: currentStrokeId,
                x, y,
                color: currentColor,
                thickness: currentThickness
            }));
        }
    }
    
    function stopDrawing() {
        if (drawing) {
            console.log('🖱️ Stop drawing');
            drawing = false;
        }
    }
    
    // Event listeners
    canvas.addEventListener('mousedown', startDrawing);
    canvas.addEventListener('mousemove', continueDrawing);
    canvas.addEventListener('mouseup', stopDrawing);
    canvas.addEventListener('mouseleave', stopDrawing);
    
    // Touch events
    canvas.addEventListener('touchstart', (e) => {
        e.preventDefault();
        const touch = e.touches[0];
        const mouseEvent = new MouseEvent('mousedown', {
            clientX: touch.clientX,
            clientY: touch.clientY
        });
        canvas.dispatchEvent(mouseEvent);
    });
    
    canvas.addEventListener('touchmove', (e) => {
        e.preventDefault();
        const touch = e.touches[0];
        const mouseEvent = new MouseEvent('mousemove', {
            clientX: touch.clientX,
            clientY: touch.clientY
        });
        canvas.dispatchEvent(mouseEvent);
    });
    
    canvas.addEventListener('touchend', (e) => {
        e.preventDefault();
        const mouseEvent = new MouseEvent('mouseup', {});
        canvas.dispatchEvent(mouseEvent);
    });
    
    // UI event listeners
    const colorPicker = document.getElementById('colorPicker');
    if (colorPicker) {
        colorPicker.addEventListener('change', (e) => {
            currentColor = e.target.value;
            console.log('🎨 Color changed to:', currentColor);
        });
    }
    
    const thickness = document.getElementById('thickness');
    if (thickness) {
        thickness.addEventListener('change', (e) => {
            currentThickness = parseInt(e.target.value);
            console.log('📏 Thickness changed to:', currentThickness);
        });
    }
    
    // Connect WebSocket
    connectWebSocket();
    
    console.log('✅ Whiteboard initialized successfully');
});