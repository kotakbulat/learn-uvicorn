# main.py
import os
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv # Optional

# Load environment variables (optional)
load_dotenv()

# --- FastAPI App Setup ---
app = FastAPI(title="Uvicorn Features Demo")

# Mount static files (like CSS) - if you have a static folder
# app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup Jinja2 templates
templates = Jinja2Templates(directory="templates")

# --- Helper for WebSocket Connection Management (Simple Example) ---
# In a real app, you'd want a more robust manager class
active_connections: list[WebSocket] = []

# --- HTTP Routes ---
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Serves the home page."""
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": "Home"}
    )

@app.get("/features", response_class=HTMLResponse)
async def read_features(request: Request):
    """Serves the Uvicorn features explanation page."""
    return templates.TemplateResponse(
        "features.html", {"request": request, "title": "Uvicorn Features"}
    )

@app.get("/websocket_demo", response_class=HTMLResponse)
async def websocket_page(request: Request):
    """Serves the page with the WebSocket client."""
    return templates.TemplateResponse(
        "websocket.html", {"request": request, "title": "WebSocket Demo"}
    )

# --- WebSocket Route ---
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """Handles WebSocket connections, echoes messages back."""
    await websocket.accept()
    active_connections.append(websocket)
    print(f"WebSocket connection established: {websocket.client}")
    try:
        while True:
            # Wait for a message from the client
            data = await websocket.receive_text()
            print(f"Received message from {websocket.client}: {data}")
            # Echo the message back to the client who sent it
            await websocket.send_text(f"You said: {data}")
            # Example: Broadcast to all clients (uncomment if desired)
            # for connection in active_connections:
            #     if connection != websocket: # Don't send back to sender if echoing separately
            #         await connection.send_text(f"Someone said: {data}")
    except WebSocketDisconnect:
        active_connections.remove(websocket)
        print(f"WebSocket connection closed: {websocket.client}")
    except Exception as e:
        print(f"WebSocket error for {websocket.client}: {e}")
        active_connections.remove(websocket)
        # Ensure connection is closed if an error occurs mid-communication
        try:
            await websocket.close(code=1011) # Internal Error
        except RuntimeError: # Ignore if already closed
            pass


# --- Running the App (for direct execution, e.g. python main.py) ---
# It's generally better to run using the `uvicorn` command directly.
if __name__ == "__main__":
    import uvicorn
    # Get host/port from environment variables or use defaults
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "8000"))
    reload = os.getenv("RELOAD", "False").lower() in ("true", "1", "t")

    print(f"Starting Uvicorn server on {host}:{port} (Reload={reload})...")
    print("RECOMMENDED: Run using 'uvicorn main:app --reload' or other flags.")

    uvicorn.run("main:app", host=host, port=port, reload=reload)