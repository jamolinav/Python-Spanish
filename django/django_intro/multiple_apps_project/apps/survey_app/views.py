from django.shortcuts import render

def root(request):
    return redirect(request, 'survey')

def index(request):
    print(request)
    return render(request, 'survey_app/index.html')

def create_user(request):
    print("Got Post Info")
    print(request)
    name        = request.POST['name']
    location    = request.POST['location']
    language    = request.POST['language']
    comment     = request.POST['comment']
    context = {
        'name' : name,
        'location' : location,
        'language' : language,
        'comment' : comment
    }
    return render(request, 'survey_app/result.html', context)
