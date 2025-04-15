How to Run and Interact:
Open VS Code Terminal: Open your uvicorn_portfolio folder in VS Code and open a new terminal (Terminal -> New Terminal).
Create Virtual Environment (Recommended):
python -m venv venv
.\venv\Scripts\activate  # On Windows Powershell/CMD
# source venv/bin/activate # On Linux/macOS/Git Bash
Use code with caution.
Bash
Install Dependencies:
pip install -r requirements.txt
Use code with caution.
Bash
Run with Uvicorn (Basic):
uvicorn main:app --host 127.0.0.1 --port 8000
Use code with caution.
Bash
Open your browser to http://127.0.0.1:8000.
Navigate to /features and /websocket_demo.
Observe the logs in your VS Code terminal (Logging feature).
Run with Hot Reload:
Stop the server (Ctrl+C in the terminal).
Run:
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
Use code with caution.
Bash
Now, open main.py, change the title in the @app.get("/") route, and save the file.
Watch the terminal - Uvicorn should detect the change and restart.
Refresh http://127.0.0.1:8000 in your browser to see the updated title. (Hot Reload feature).
Test WebSocket:
Go to http://127.0.0.1:8000/websocket_demo.
Type a message in the input box and click "Send".
The server should echo it back. (WebSocket feature). Check terminal logs too.
Test HTTPS/HTTP2 (Optional):
Make sure openssl is available (often comes with Git for Windows).
Generate self-signed certificates in the terminal (in your project folder):
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365 -nodes -subj "/CN=localhost"
Use code with caution.
Bash
(This creates key.pem and cert.pem).
Stop Uvicorn (Ctrl+C).
Run with SSL:
uvicorn main:app --host 127.0.0.1 --port 8000 --ssl-keyfile key.pem --ssl-certfile cert.pem
Use code with caution.
Bash
Open https://127.0.0.1:8000 (note https). Your browser will warn you about the self-signed certificate. Proceed if you trust it (you just created it). (HTTPS feature).
Stop Uvicorn.
Run with SSL and HTTP/2 (requires h2 installed):
uvicorn main:app --host 127.0.0.1 --port 8000 --ssl-keyfile key.pem --ssl-certfile cert.pem --http h2
Use code with caution.
Bash
Open https://127.0.0.1:8000. Use browser dev tools (Network tab) to verify the protocol is h2 or HTTP/2. (HTTP/2 feature).