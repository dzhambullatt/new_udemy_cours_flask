from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)
Bootstrap(app)

# DB configuration
db = yaml.load(open('db.yaml'))

app.config('MYSQL_HOST') = db['mysql_host']
app.config('MYSQL_USER') = db['mysql_user']
app.config('MYSQL_PASSWORD') = db['mysql_password']
app.config('MYSQL_DB') = db['mysql_db']

mysql = MySQL(app)


@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    return render_template('index.html')  # cars=cars это передача списка в сам шаблон по ключевому слову cars


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/css')
def css():
    return render_template('css.html')


if __name__ == '__main__':
    app.run(debug=True)
