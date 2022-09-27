from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    cars = ['bmw', 'audi', 'bugatti', 'lamborghini']
    return render_template('index.html', cars=cars) #cars=cars это передача списка в сам шаблон по ключевому слову cars


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/css')
def css():
    return render_template('css.html')


if __name__ == '__main__':
    app.run(debug=True)
