from django.shortcuts import render
from django.http import HttpResponse
# Подключение стандартной формы для регистрации
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import text_home

def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'main/404.html', data)

def index(request):
    main = text_home.objects.order_by('-date')
    return render(request, 'main/index.html',{'main': main})

def about(request):
    return render(request, 'main/about.html')

def school_info(request):
    return render(request, 'main/School_info.html')

def register_user(request):
    # Массив для передачи данных шаблонны
    data = {}
    # Проверка что есть запрос POST
    if request.method == 'POST':
        # Создаём форму
        form = RegistrForm(request.POST)
        # Валидация данных из формы
        if form.is_valid():
            # Сохраняем пользователя
            form.save()
            # Передача формы к рендару
            data['form'] = form
            # Передача надписи, если прошло всё успешно
            data['res'] = "Всё прошло успешно"
            # Рендаринг страницы
            return render(request, 'main/register.html', data)
    else: # Иначе
        # Создаём форму
        form = RegistrForm()
        # Передаём форму для рендеринга
        data['form'] = form
        # Рендаринг страницы
        return render(request, 'main/register.html', data)

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'main/login_user.html', {'form': form})