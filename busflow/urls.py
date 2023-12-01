from django.urls import path

from . import views

app_name = 'busflow'
urlpatterns = [
      path('<int:ponto_id>/', views.detail_ponto, name='detail'), # adicione esta linha
]
