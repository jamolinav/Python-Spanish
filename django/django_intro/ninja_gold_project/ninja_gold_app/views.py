from django.shortcuts import render, redirect
from datetime import datetime
import random
from django.utils.safestring import SafeData, SafeString, mark_safe

def index(request):
    if 'golds' not in request.session:
        request.session['golds'] = 0
    if 'activities' in request.session:
        request.session['activities_inv'] = request.session['activities'][::-1]
    return render(request, 'index.html')

def process_money(request, form):
    print(request)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    if form == 'farm':
        earn = random.randint(10, 20)
        request.session['golds'] += earn
        mensaje = f'<div style="color: green;">Earned {earn} golds from farm! ({dt_string})</div>'
    if form == 'cave':
        earn = random.randint(5, 10)
        request.session['golds'] += random.randint(5, 10)
        mensaje = f'<div style="color: green;">Earned {earn} golds from cave! ({dt_string})</div>'
    if form == 'house':
        earn = random.randint(2, 5)
        request.session['golds'] += random.randint(2, 5)
        mensaje = f'<div style="color: green;">Earned {earn} golds from house! ({dt_string})</div>'
    if form == 'casino':
        earn = random.randint(-50, 50)
        while earn == 0:
            earn = random.randint(-50, 50)
        request.session['golds'] += earn
        if earn > 0:
            mensaje = f'<div style="color: green;">Earned {earn} golds from casino! ({dt_string})</div>'
        else:
            mensaje = f'<div style="color: red;">Entered to casino and lost {(earn*-1)}...Ouch.. ({dt_string})</div>'

    if 'activities' not in request.session:
        request.session['activities'] = [mark_safe(mensaje)]
    else:
        request.session['activities'].append(mark_safe(mensaje))

    request.session.save()
    return redirect('/ninja_gold')

def destroy_session(request):
    request.session.clear()
    return redirect('/ninja_gold')
