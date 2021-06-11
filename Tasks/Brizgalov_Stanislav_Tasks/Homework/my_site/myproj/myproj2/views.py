from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from .models import Post


def index(request):
    p = Post.objects.all()

    return render(request, 'myproj2/index.html', {'post': p, 'title': 'Главная страница'})



def about(request):
    return render(request, 'myproj2/about.html', {'title': 'Про нас'})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'myproj2/index.html', {'title': 'Главная страница'})
            else:
                return render(request, 'myproj2/registration/login.html', {'title': 'Авторизация', 'status': 'Логин или пароль введен неверно', 'form': form})
    else:
        form = LoginForm()
    return render(request, 'myproj2/registration/login.html', {'title': 'Авторизация', 'form': form})


def creat_in(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'myproj2/registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'myproj2/registration/creat_in.html', {'user_form': user_form})




