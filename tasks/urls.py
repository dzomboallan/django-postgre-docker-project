from rest_framework.routers import DefaultRouter
from .views import TaskAPI

router = DefaultRouter()
router.register("tasks", TaskAPI, basename="tasks")
urlpatterns = router.urls