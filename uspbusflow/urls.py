from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('staticpages.urls')), # modifique esta linha
    path('busflow/', include('busflow.urls')), # adicionar esta linha
    path('admin/', admin.site.urls),
]
