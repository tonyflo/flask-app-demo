from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    mountains = ['Everest', 'K2', 'Kilimanjaro']
    return render_template('index.html', mountain=mountains)

app.run(host='0.0.0.0', port=80)
