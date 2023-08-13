from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reklama
from .forms import AdvForm
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse


#какой-то код, вместо django_shell
def debug_method(request):
    #
    #код
    #
    return HttpResponse("debug")


def index(request):
    reklama_db = Reklama.objects.all()
    context = {"reklamus": reklama_db}
    return render(request, "index.html", context)


def adv_post(request: WSGIRequest):
    if request.method == 'POST':
        form = AdvForm(request.POST, request.FILES)# передаю все данные в форму для проверки
        if form.is_valid(): #проверяю на правильность True/False
            adv = Reklama(**form.cleaned_data) # передаю данные в модель
            adv.user = request.user #добавил в запись юзера, который делал запрос
            adv.save() #сохраняю запись в бд
            return redirect( #перехожу по этой ссылке
                reverse('main-page') #получаю полную ссылку
            )
        else:
            print("Ошибка")

    else: # get
        form = AdvForm()

    context = {"form": form}
    return render(request, "advertisement-post.html", context)



def top_sellers(request):
    return render(request,"top-sellers.html")

def adver(request):
    return render(request, "advertisement.html")

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def profile(request):
    return render(request, "profile.html")

