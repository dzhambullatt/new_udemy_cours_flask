from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
    cars = ['bmw', 'audi', 'bugatti', 'lamborghini']
    return render_template('index.html', cars=cars) #cars=cars это передача списка в сам шаблон по ключевому слову cars


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
