from rest_framework_nested import routers
from core.views import UserViewSet
from . import views


router = routers.DefaultRouter()
router.register('items', views.ToDoItemViewSet, basename='todo')


urlpatterns = router.urls
