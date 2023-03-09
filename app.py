from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
  return '''<h1>Hello World!</h1>
  <a href="/about">About Page</a>'''

@app.route('/cookies/<slug>')
def cookie(slug):
  return slug

if __name__ == '__main__':
  app.run()