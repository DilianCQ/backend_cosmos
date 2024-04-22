from rest_framework.routers import DefaultRouter
from usuarios.viewsets import UsuarioViewSet

router = DefaultRouter()
router.register("usuarios", UsuarioViewSet, basename="usuarios")
urlpatterns = router.urls