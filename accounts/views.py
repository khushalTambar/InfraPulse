from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm


def login_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    form = LoginForm(request, data=request.POST or None)

    if request.method == "POST":

        if form.is_valid():

            login(request, form.get_user())

            return redirect("dashboard")

        messages.error(request, "Invalid username or password.")

    return render(
        request,
        "accounts/login.html",
        {"form": form},
    )


def register_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    form = RegisterForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Account created successfully."
            )

            return redirect("login")

    return render(
        request,
        "accounts/register.html",
        {"form": form},
    )


@login_required
def logout_view(request):

    logout(request)

    return redirect("home")