from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    name = request.args.get("name", "World")
    return f'<H1>Hello, {escape(name)}!<H1>'

@app.route('/about')
def about():
    return f'<H1>About page<H1>'

if __name__ == '__main__':
    app.run(debug=True)