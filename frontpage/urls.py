from django.urls import path

from . import views


app_name = "frontpage"
urlpatterns = [
    path("", views.index, name="frontpage"),
    path('whitepaper/', views.whitepaper, name="whitepaper"),
]
