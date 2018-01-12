from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: blankurl like the homepage or http://127.0.0.1:8000/
    url(r'^$', views.welcome, name='welcome')
]
