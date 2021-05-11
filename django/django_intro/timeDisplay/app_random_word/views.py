from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string

def random_word(request):
    if 'attempt' not in request.session:
        request.session['attempt'] = 0
    request.session['attempt'] += 1
    random_word = get_random_string(length=14)
    context = {
        "random_word": random_word,
        "attempt": request.session['attempt']
    }
    return render(request, "index.html", context)

def reset(request):
    request.session.pop('attempt')
    request.session['attempt'] = 0
    return redirect('/random_word')