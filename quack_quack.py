from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

# Ensure the static directory exists
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

@app.route('/')
def translator():
    return render_template('quack.html')

if __name__ == '__main__':
    app.run(debug=True)
