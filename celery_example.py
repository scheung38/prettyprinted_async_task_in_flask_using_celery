from flask import Flask
from flask_celery import make_celery

app = Flask(__name__)

app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(app)


@app.route('/process/<name>')
def process(name):
    reverse.delay(name)
    return 'I sent an async request!'


@app.route('/add/<a>,<b>')
def add(a, b):
    add_together.delay(a, b)
    return "adding two numbers together"


@celery.task()
def add_together(a, b):
    res = int(a) + int(b)
    return res


@celery.task(name='celery_example.reverse')
def reverse(string):
    return string[::-1]


if __name__ == '__main__':
    app.run(debug=True)
