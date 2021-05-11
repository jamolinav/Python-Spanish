from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', row=8, col=8, color1='red', color2='black')
@app.route('/<int:row>')
def row(row):
    return render_template('index.html', row=row, col=8, color1='red', color2='black')
@app.route('/<int:row>/<int:col>')
def row_col(row,col):
    return render_template('index.html', row=row, col=col, color1='red', color2='black')
@app.route('/<int:row>/<int:col>/<color1>/<color2>')
def row_col_color(row,col,color1,color2):
    return render_template('index.html', row=row, col=col, color1=color1, color2=color2)

if __name__ == '__main__':
    app.run(debug=True)