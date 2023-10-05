from flask import Flask, render_template

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('pages/404.jinja'), 404


@app.route('/')
def index():
    return render_template('pages/index.jinja', name="Anthony Bernardo Kamers")


if __name__ == '__main__':
    app.run()
