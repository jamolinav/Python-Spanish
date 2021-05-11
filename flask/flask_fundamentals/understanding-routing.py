from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '¡Hola Mundo!'
@app.route('/dojo')
def dojo():
    return 'Dojo!'
@app.route('/say/<name>')
def say(name):
    return f'¡Hola {name}!'
@app.route('/repeat/<int:num>/<saludo>')
def repeat(num, saludo):
    return f'{saludo}<br>' * num

if __name__ == '__main__':
    app.run(debug=True)
    
    