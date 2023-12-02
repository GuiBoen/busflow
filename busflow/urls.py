from django.urls import path

from . import views

app_name = "busflow"
urlpatterns = [
    path("", views.list_pontos, name="index"),  # adicione esta linha
    path("<int:ponto_id>/", views.detail_ponto, name="detail"),  # adicione esta linha
    path("search/", views.search_pontos, name="search"),  # adicione esta linha
    path('update/<int:ponto_id>/', views.update_ponto, name="update"), #
]
