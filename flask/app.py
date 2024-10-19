from flask import Flask, send_from_directory, jsonify

app = Flask(__name__, static_folder='static/dist')

@app.route('/')
def home():
    # 返回編譯後的 index.html
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
