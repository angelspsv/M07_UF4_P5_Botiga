from rest_framework.routers import DefaultRouter
from .views import UsuariosViewSet

router = DefaultRouter()
router.register(r'', UsuariosViewSet)

urlpatterns = router.urls
