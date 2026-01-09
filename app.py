from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)

# Rota do frontend
@app.route("/")
def index():
    return send_from_directory(".", "index.html")

# API de teste
@app.route("/api/ping")
def ping():
    return jsonify({
        "status": "ok",
        "message": "🔥 Backend Python ativo – Inteligência do Cafunfo online!"
    })

# Porta obrigatória do Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
