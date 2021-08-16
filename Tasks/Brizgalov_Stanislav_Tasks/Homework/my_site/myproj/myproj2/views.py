from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from .models import Post1, Post2, Post3, Post4, Post5, Post6, Post7, Post8


def index(request):
    return render(request, 'myproj2/index.html', {'title': 'Главная страница'})


def about(request):
    return render(request, 'myproj2/about.html', {'title': 'Про нас'})


def chainsaw(request):
    p = Post1.objects.all()
    return render(request, 'myproj2/tool/chainsaw.html', {'post': p, 'title': 'chainsaw'})


def gas_drills(request):
    p = Post2.objects.all()
    return render(request, 'myproj2/tool/gas_drills.html', {'post': p, 'title': 'chainsaw'})


def gas_cutters(request):
    p = Post3.objects.all()
    return render(request, 'myproj2/tool/gas_cutters.html', {'post': p, 'title': 'gas_cutters'})


def concrete_mixers(request):
    p = Post4.objects.all()
    return render(request, 'myproj2/tool/concrete_mixers.html', {'post': p, 'title': 'concrete_mixers'})


def grinders(request):
    p = Post5.objects.all()
    return render(request, 'myproj2/tool/grinders.html', {'post': p, 'title': 'grinders'})


def generators(request):
    p = Post6.objects.all()
    return render(request, 'myproj2/tool/generators.html', {'post': p, 'title': 'generators'})


def stairs(request):
    p = Post7.objects.all()
    return render(request, 'myproj2/tool/stairs.html', {'post': p, 'title': 'stairs'})


def mixers(request):
    p = Post8.objects.all()
    return render(request, 'myproj2/tool/mixers.html', {'post': p, 'title': 'mixers'})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
            else:
                return render(request, 'myproj2/registration/login.html',
                              {'title': 'Авторизация', 'status': 'Логин или пароль введен неверно', 'form': form})
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
