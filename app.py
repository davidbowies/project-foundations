from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/studies')
def about():
    return render_template('studies.html')

@app.route('/private')
def contact():
    return render_template('private.html')

@app.route('/user/<username>')
def user_profile(username):
    return render_template('user.html', username=username)

if __name__ == '__main__':
  app.run()