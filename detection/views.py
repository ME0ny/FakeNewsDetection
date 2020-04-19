from django.shortcuts import render,redirect
from .forms import ArticleParseRequestForm
from django.http import HttpResponseRedirect
import json
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    if request.method == 'POST':
        form = ArticleParseRequestForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            intext = req.text
            insource = req.source
            return loading(request,intext,insource)
    else:
        #initial = {'text': "Введите текст статьи", 'source': "Введите источник статьи"}
        form = ArticleParseRequestForm()
    return render(request, 'detection/index.html', {'form':form})

# @csrf_exempt
# def ArticleRequest(request):
#     url = request.POST.get('url')
#     return render(request, 'detection/index.html', {'myurl': url})


def loading(request,text,source):
    message = "Звоним редактору"
    return render(request, 'detection/loading.html', 
    {
        'message': message,
        'text' : text,
        'source': source,
    })

def result(request):
    ctx = {
        'fake': True,
        'title': "Вести",
        'rating': 5,
    }
    return render(request, 'detection/result.html',ctx)

