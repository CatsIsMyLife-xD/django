# pages/views.py
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Task, Organization, Catalog, News
from .forms import TaskForm, UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})

def login(request):
    if request.method == 'POST':
        user_form = AuthenticationForm(data = request.POST)
        if user_form.is_valid():
            return redirect ('home')
    else:
        user_form = AuthenticationForm()
    return render(request, 'auth.html', {'user_form': user_form})



class HomePageView(TemplateView):
    template_name = 'home.html'

class PayPageView(TemplateView):
    template_name: str = 'pay.html'

class AuthPageView(TemplateView):
    template_name: str = 'auth.html'

class RegisterPageView(TemplateView):
    template_name: str = 'register.html'

def index(request):
    code_m = Catalog.objects.last()
    product_name_m  = Catalog.objects.last()
    image_m = Catalog.objects.last()
    price_m = Catalog.objects.last()
    description_m = Catalog.objects.last()
    return render (request, 'pages/home.html', {'title' : 'Каталог', 'code': code_m, 'product_name': product_name_m, 'image' : image_m, 'price': price_m, 'description' : description_m})

def info(request):
    tasks_m = Task.objects.last()
    return render(request, 'pages/history.html', {'title': 'Отзывы', 'tasks':tasks_m})

def reviews_create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('history')
        else:
            error = 'Неверная форма'
    form = TaskForm()
    context = {
        'form' : form,
        'error': error
    }

    return render(request, 'pages/reviews.html', context)

def reviews(request):
    tasks = Task.objects.all()
    return render(request, 'pages/history.html', {'title': 'Отзывы', 'tasks':tasks})

def about(request):
    adress = Organization.objects.all()
    phone = Organization.objects.all()
    name = Organization.objects.all()
    return render (request, 'pages/about.html', {'title' : 'Информация об организации','name': name, 'adress': adress, 'phone': phone} )
    
def catalog(request):
    code = Catalog.objects.all()
    product_name  =  Catalog.objects.all()
    image = Catalog.objects.all()
    price = Catalog.objects.all()
    description = Catalog.objects.all()
    return render (request, 'pages/catalog.html', {'title' : 'Каталог', 'code': code, 'product_name': product_name, 'image' : image, 'price': price, 'description' : description})

def news(request):
    news_name = News.objects.order_by('id')
    news_image = News.objects.order_by('id')
    news_description = News.objects.order_by('id')
    return render (request, 'pages/news.html', {'title' : 'Новости и праздники', 'news_name' : news_name, 'news_image' : news_image, 'news_description' : news_description})
