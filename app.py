from flask import Flask, jsonify

@app.route("/api/status")
def status():
    return jsonify({
        "status": "online",
        "app": "Inteligência do Cafunfo"
    })

