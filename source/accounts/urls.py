from django.urls import path
from django.contrib.auth.views import LoginView
from accounts.views import user_signup, custom_logout
app_name: str = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', custom_logout, name='logout'),
    path('signup/', user_signup, name='signup'),
]
