from django.contrib import admin
from django.urls import path, include
from backend_cosmos.swagger import urlpatternsSwagger

urlpatterns = urlpatternsSwagger + [
    path("admin/", admin.site.urls),
    path("api/", include("usuarios.routes")),
]