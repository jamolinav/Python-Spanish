from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'codingdojo'

@app.route('/')
def index():
    if 'sessionContador' in session:
        session['sessionContador'] += 1
    else:
        session['sessionContador'] = 1
    return render_template('index.html', times=session['sessionContador'], custom_times=0)

@app.route('/two_visits')
def two_visits():
    if 'sessionContador' in session:
        session['sessionContador'] += 2
    else:
        session['sessionContador'] = 2
    return render_template('index.html', times=session['sessionContador'], custom_times=0)

@app.route('/n_visits', methods=['POST'])
def n_visits():
    print(request.form)
    n = int(request.form['custom_times'])
    if 'sessionContador' in session:
        session['sessionContador'] += n
    else:
        session['sessionContador'] = n
    return render_template('index.html', times=session['sessionContador'], custom_times=n)

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

