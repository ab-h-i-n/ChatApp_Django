from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.HomePage,name='home'),
    
    # login-section
	path("login/", LoginView.as_view
		(template_name="LoginPage.html"), name="login-user"),
	path("logout/", LogoutView.as_view(), name="logout-user"),
]