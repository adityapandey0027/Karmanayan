from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Vision page
@app.route('/vision')
def vision():
    return render_template('vision.html')

# Team page
@app.route('/team')
def team():
    return render_template('team.html')

# Contact page with form support
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"New message from {name} ({email}): {message}")
        return redirect(url_for('contact'))
    return render_template('contact.html')

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(f"Login attempt by {email}")
        return redirect(url_for('home'))
    return render_template('login.html')

# Signup page (optional)
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        print(f"New signup: {name} ({email})")
        return redirect(url_for('login'))
    return render_template('signup.html')

# Main entry point
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
