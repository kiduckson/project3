from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView

from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render
from django.urls import reverse

# Create your views here.


def register(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']

        print(f"{username} {email} {password} {re_password}")

        id_duplicate = User.objects.filter(username=username).exists()
        email_duplicate = User.objects.filter(email=email).exists()

        if password != re_password:
            return render(request, "users/register.html", {'message': "Passwords don't match"})
        elif email_duplicate == True:
            return render(request, "users/register.html", {'message': "Given email is already in use"})
        elif id_duplicate == True:
            return render(request, "users/register.html", {'message': "Given username is already in use"})
        else:
            user = User.objects.create_user(username, email, password)
            user_login = authenticate(
                request, username=username, password=password)
            login(request, user_login)
            return HttpResponseRedirect(reverse("index"))
    elif request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "users/register.html", {"message": None})


class login_view(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class logout_view(LogoutView):
    template_name = 'users/logout.html'
