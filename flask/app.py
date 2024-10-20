from flask import Flask, render_template

app = Flask(__name__, static_folder='./static/dist/assets', template_folder='./static/dist')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


if __name__ == "__main__":
    app.run(debug=True)
