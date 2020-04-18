from django.shortcuts import render

def index(request):
    return render(request, 'detection/index.html', {})


def loading(request):
    message = "Звоним редактору"
    return render(request, 'detection/loading.html', 
    {
        'message': message, 
    })

def result(request):
    ctx = {
        'fake': True,
        'title': "Вести",
        'rating': 5,
    }
    return render(request, 'detection/result.html',ctx)

