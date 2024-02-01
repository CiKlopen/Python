from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Home Page!'

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/greet')
def greet():
    # 获取名字参数，默认为 "World"
    name = request.args.get('name', 'World')
    return f'Hello, {name}!'

@app.route('/add')
def add():
    # 获取两个参数 a 和 b，将它们转换为整数并相加
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    result = a + b
    return f'The sum of {a} and {b} is {result}.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
