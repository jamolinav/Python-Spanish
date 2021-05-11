from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
        return render_template('index.html',nivel=1,num=3,color='blue')
@app.route('/play/<int:num>')
def play_num(num):
        return render_template('index.html',nivel=2,num=num,color='blue')
@app.route('/play/<int:num>/<color>')
def play_num_color(num,color):
        return render_template('index.html',nivel=3,num=num,color=color)


if __name__ == '__main__':
    app.run(debug=True)