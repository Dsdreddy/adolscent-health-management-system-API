from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Mock user database
users_db = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Save user with hashed password
        users_db[username] = generate_password_hash(password)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Verify user credentials
        if username in users_db and check_password_hash(users_db[username], password):
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials, please try again."
    return render_template('login.html')

@app.route('/guardian_login', methods=['GET', 'POST'])
def guardian_login():
    if request.method == 'POST':
        username = request.form['username']
        Guardian_password = request.form['Guardian_password']
        # Verify guardian credentials
        if username in users_db and check_password_hash(users_db[username], parent_password):
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials, please try again."
    return render_template('guardian_login.html')


@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    # Mock user data for dashboard
    user_info = {
        "name": "John Doe",
        "age": 28,
        "email": "johndoe@example.com",
        "phone": "123-456-7890"
    }
    return render_template('dashboard.html', user_info=user_info)

@app.route('/health_metrics_log')
def health_metrics_log():
    return render_template('health_metrics_log.html')

@app.route('/symptoms_checker')
def symptoms_checker():
    return render_template('symptoms_checker.html')

@app.route('/book_appointment')
def book_appointment():
    return render_template('book_appointment.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
