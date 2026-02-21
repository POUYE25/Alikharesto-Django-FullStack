from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup, signup_success
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup, signup_success, MyLogoutView

app_name = 'accounts'

urlpatterns = [
    # Login : utilise la vue native de Django
    path("login/", auth_views.LoginView.as_view(
        template_name="registration/login.html"), name="login"),

    # Logout : utilise votre vue personnalisée
    path("logout/", MyLogoutView.as_view(), name="logout"),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path("signup/", signup, name="signup"),
    path("signup/success/", signup_success, name="signup_success"),
]


