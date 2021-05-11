from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)
app.secret_key = 'codingdojo'

@app.route('/')
def index():
    if 'jugadores' not in session:
        session['jugadores'] = []
    if 'intentos' not in session:
        session['intentos'] = 0
    if 'nombre' not in session:
        session['nombre'] = ''
    if 'mensaje' not in session:
        session['mensaje'] = 'Intente adivinar'

    if 'num_secreto' not in session:
        session['num_secreto'] = random.randint(1, 100)
    return render_template('index.html', num_secreto=session['num_secreto'], jugadores=session['jugadores'])

@app.route('/adivinar', methods=['POST'])
def adivinar():
    print(request.form)
    print('num_secreto:',session['num_secreto'])
    session['intentos'] = int(session['intentos']) + 1
    session['nombre'] = request.form['nombre']

    if int(session['intentos']) >= 5:
        mensaje = 'Perdedor'
        session['jugadores'].append({'nombre': session['nombre'], '': session['nombre'], 'intentos': session['intentos'], 'resultado': mensaje, 'num_secreto': session['num_secreto']})
        return redirect('/destroy_session_jugador')

    if int(session['num_secreto']) == int(request.form['numero_jugador']):
        mensaje = 'Ganador'
        session['jugadores'].append({'nombre': session['nombre'], '': session['nombre'], 'intentos': session['intentos'], 'resultado': mensaje, 'num_secreto': session['num_secreto']})
        return redirect('/destroy_session_jugador')

    if int(session['num_secreto']) > int(request.form['numero_jugador']):
        mensaje = 'Demasiado bajo'

    if int(session['num_secreto']) < int(request.form['numero_jugador']):
        mensaje = 'Demasiado alto'

    session['mensaje'] = mensaje
    
    return redirect('/')

@app.route('/destroy_session_jugador')
def destroy_session_jugador():
    session.pop('nombre')
    session.pop('intentos')
    session.pop('num_secreto')
    session.pop('mensaje')
    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)