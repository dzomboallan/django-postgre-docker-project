from rest_framework.viewsets import ModelViewSet
from .models import Task
from .serializers import TaskSerializer

# Create your views here.
class TaskAPI(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
