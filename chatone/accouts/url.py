from django.urls import path
from . import views



urlpatterns = [
    path('login/',views.login, name='login'),
    path('signup/',views.sigup, name='signup'),
    path('account/',views.accout, name='account'),
    path('logot',views.logot, name='logot'),
    path('editaccount/',views.edit_profile, name='edit_profile'),
    path('new_password/',views.reset_pass, name='new_password')
]

