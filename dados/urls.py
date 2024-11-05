from django.urls import path

from . import views as v

app_name = "dados"


urlpatterns = [
    path("", v.index, name="index"),
    path(
        "ajax/get_card_experience/<int:card_id>/",
        v.get_card_experience,
        name="get_card_experience",
    ),
]
