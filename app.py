from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "cafunfo"

# Banco simples (memória)
users = {}

# ------------------ HOME ------------------
@app.route('/')
def home():
    return render_template('index.html')

# ------------------ PÁGINAS ------------------
@app.route('/linguagens')
def linguagens():
    return render_template('linguagens.html')

@app.route('/python')
def python_page():
    return render_template('python.html')

@app.route('/javascript')
def javascript():
    return render_template('javascript.html')

@app.route('/flutter')
def flutter():
    return render_template('flutter.html')

@app.route('/bots')
def bots():
    return render_template('bots.html')

# ------------------ LOGIN ------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pw = request.form['password']

        if user in users and users[user] == pw:
            session['user'] = user
            return redirect('/')
        else:
            return "Login inválido"

    return render_template('login.html')

# ------------------ REGISTER ------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = request.form['username']
        pw = request.form['password']

        users[user] = pw
        return redirect('/login')

    return render_template('register.html')

# ------------------ LOGOUT ------------------
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

# ------------------ RODAR ------------------
if __name__ == '__main__':
    app.run(debug=True)
