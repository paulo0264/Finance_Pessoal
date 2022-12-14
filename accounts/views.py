from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
from accounts.models import Usuario
from accounts.forms import RegisterUserForm


def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        user_aux = Usuario.objects.get(username=request.POST['username'])
        password = request.POST["password"]
        user = authenticate(
            request, username=user_aux.username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')

    return render(request, "accounts/dashboard.html")


def cadastrar(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        user_form = RegisterUserForm(data=request.POST)
        try:
            user_aux = Usuario.objects.get(email=request.POST['email'])
            form = RegisterUserForm()
            item = {
                'form': form,
                'msg': 'Erro! Já existe um usuário com o mesmo e-mail',
            }

            if user_aux:
                return render(request, 'cadastrar.html', item)

        except Usuario.DoesNotExist:
            user = user_form.save(commit=False)
            user.password = make_password(user_form.cleaned_data['password'])
            user.save()

    form = RegisterUserForm()
    item = {
        'form': form
    }

    return render(request, 'cadastrar.html', item, )
