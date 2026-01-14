from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/linguagens")
def linguagens():
    return render_template("linguagens.html")

@app.route("/python")
def python():
    return render_template("python.html")

@app.route("/javascript")
def javascript():
    return render_template("javascript.html")

@app.route("/flutter")
def flutter():
    return render_template("flutter.html")

@app.route("/bots")
def bots():
    return render_template("bots.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
