from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "cafunfo"

users = {}

@app.route('/')
def home():
    return render_template('index.html')


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


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = request.form['username']
        pw = request.form['password']

        users[user] = pw
        return redirect('/login')

    return render_template('register.html')
