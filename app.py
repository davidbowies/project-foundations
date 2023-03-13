from flask import Flask, render_template

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


@app.route("/general")
def general():
    return render_template("general.html")


@app.route('/user/<username>')
def user_profile(username):
    return render_template('user.html', username=username)


@app.route('/todo/<slug>')
def to_do(slug):
    to_do_list = {
    '1' : {'task': 'Complete project proposal', 'status': 'in progress'},
    '2' : {'task': 'Attend meeting with team', 'status': 'complete'},
    '3' : {'task': 'Research competitors', 'status': 'not started'},
    '4' : {'task': 'Create wireframe designs', 'status': 'in progress'},
    '5' : {'task': 'Review feedback from stakeholders', 'status': 'not started'},
    '6' : {'task': 'Finalize project plan', 'status': 'complete'}
}
    return render_template('todo.html', to_do=to_do_list)

if __name__ == '__main__':
    app.run()
