from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"New message from {name} ({email}): {message}")
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/vision')
def vision():
    return render_template('vision.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(f"Login attempt by {email}")
        return redirect(url_for('home'))
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Process signup data here
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        print(f"New signup: {name} ({email})")
        return redirect(url_for('login'))
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
