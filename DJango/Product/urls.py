from django.http import HttpResponse
from django.urls import path
from . import views


def index(request):
    return HttpResponse("this is Product page")


urlpatterns = [
    path('test', index),
    path('django_web', views.index),
    path('addProducts', views.post_product_data),
    path('personForm', views.ger_form)
]