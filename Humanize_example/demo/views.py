from django.shortcuts import render

def index(request):
    context = {
        'first' : 6,
        'second' : 2465143874321454,
        'third' : 3542,
        'fourth' : 4512,
        'fifth': 12
    }
    return render(request, 'demo/demo.html', context)