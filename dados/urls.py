from django.urls import path

from . import views as v

app_name = "dados"


urlpatterns = [
    path("", v.index, name="index"),
]
