from flask import Flask, jsonify
import os
import time

app = Flask(__name__)
START_TIME = time.time()

@app.get("/")
def home():
    return "Hello 👋 L'appli tourne.", 200

@app.get("/health")
def health():
    # Exemple d'état simple + uptime
    uptime_seconds = int(time.time() - START_TIME)
    return jsonify(
        status="ok",
        uptime_seconds=uptime_seconds,
        service="my-flask-app"
    ), 200

if __name__ == "__main__":
    # 0.0.0.0 pour être accessible depuis le réseau (docker/VM)
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "5000"))
    app.run(host=host, port=port, debug=True)
