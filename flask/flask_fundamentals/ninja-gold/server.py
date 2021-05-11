from flask import Flask, render_template, session, redirect, request
import random
from datetime import datetime
import markupsafe

app = Flask(__name__)
app.secret_key = 'codingdojo'

@app.route('/')
def index():
    if 'golds' not in session:
        session['golds'] = 0
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    print(request.form)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    if request.form['building'] == 'farm':
        earn = random.randint(10, 20)
        session['golds'] += earn
        mensaje = f'<div style="color: green;">Earned {earn} golds from farm! ({dt_string})</div>'
    if request.form['building'] == 'cave':
        earn = random.randint(5, 10)
        session['golds'] += random.randint(5, 10)
        mensaje = f'<div style="color: green;">Earned {earn} golds from cave! ({dt_string})</div>'
    if request.form['building'] == 'house':
        earn = random.randint(2, 5)
        session['golds'] += random.randint(2, 5)
        mensaje = f'<div style="color: green;">Earned {earn} golds from house! ({dt_string})</div>'
    if request.form['building'] == 'casino':
        earn = random.randint(-50, 50)
        while earn == 0:
            earn = random.randint(-50, 50)
        session['golds'] += earn
        if earn > 0:
            mensaje = f'<div style="color: green;">Earned {earn} golds from casino! ({dt_string})</div>'
        else:
            mensaje = f'<div style="color: red;">Entered to casino and lost {(earn*-1)}...Ouch.. ({dt_string})</div>'

    if 'activities' not in session:
        session['activities'] = [markupsafe.Markup(mensaje)]
    else:
        session['activities'].append(markupsafe.Markup(mensaje))

    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)