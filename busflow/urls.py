from django.urls import path

from . import views

app_name = "busflow"
urlpatterns = [
    path("", views.PontosListView.as_view(), name="index"),  # adicione esta linha
    path("<int:ponto_id>/", views.detail_ponto, name="detail"),  # adicione esta linha
    path("search/", views.search_pontos, name="search"),  # adicione esta linha
    path('update/<int:ponto_id>/', views.update_ponto, name="update"), #
    path('update_onibus/<int:onibus_id>/', views.update_onibus, name="update_onibus"), #
    path("detail_onibus/<int:onibus_id>/", views.detail_onibus, name="detail_onibus"),  # adicione esta linha
    path('import/', views.import_ponto, name='import'),

]
