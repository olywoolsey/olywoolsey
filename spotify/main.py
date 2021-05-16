from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def Welcome():
    return "Welcome"
@app.route('/hello')
def hello():
    return "Hello, World!"
@app.route('/login')
def login():
    return render_template('LoginPage.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)