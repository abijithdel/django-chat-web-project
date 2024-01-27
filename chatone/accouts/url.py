from django.urls import path
from . import views



urlpatterns = [
    path('login/',views.login, name='login'),
    path('signup/',views.sigup, name='signup'),
    path('account/',views.accout, name='account'),
    path('logot',views.logot, name='logot'),
    path('editaccount/',views.edit_delete, name='adite_and_delete')
]

