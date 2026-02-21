from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


# Utilisation de la vue générique pour la déconnexion
class MyLogoutView(LogoutView):
    # Redirige vers la page de login après déconnexion
    next_page = reverse_lazy('accounts:login')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connexion automatique
            return redirect("accounts:signup_success")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

def signup_success(request):
    return render(request, "registration/signup_success.html")