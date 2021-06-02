from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/index')
def Index():
    return render_template("index.html")


@app.route('/')
def Login():
    return render_template("login.html")


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/tables')
def tables():
    return render_template("tables.html")


@app.route('/forms')
def forms():
    return render_template("forms.html")


@app.route('/charts')
def charts():
    return render_template("charts.html")


if __name__ == '__main__':
    app.run()
