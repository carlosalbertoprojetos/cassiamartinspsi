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
    path(
        "ajax/get_sub_topicos/<int:subtop_id>/",
        v.get_sub_topicos,
        name="get_sub_topicos",
    ),
]
