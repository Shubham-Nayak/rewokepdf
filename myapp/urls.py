from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('login/',views.login),
    path('signup/',views.signup),
    path('logout/',views.logout),
    path('buysubscription/',views.buysubscription),
    path('checkout/<int:myid>/',views.checkout),
    path('savepdf/',views.savepdf),
    path('history/',views.history),



]