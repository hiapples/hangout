from flask import Flask, send_from_directory, render_template

app = Flask(__name__, static_folder='./static/dist/assets', template_folder='./static/dist')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/assets/<path:path>')
def send_asset(path):
    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    app.run(debug=True)
