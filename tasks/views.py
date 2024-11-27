from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from modules.domain.use_cases import TaskUseCase
from modules.application.serializer import TaskSerializer
from modules.application.repositories import DjangoTaskRepository

class TaskAPIView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        repository = DjangoTaskRepository()
        self.use_case = TaskUseCase(repository)

    # Modificación: Asegúrate de que 'request' esté presente como argumento
    def get(self, request):  # Aquí 'request' es necesario
        tasks = self.use_case.get_all_tasks()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = self.use_case.create_task(serializer.validated_data['title'], serializer.validated_data['description'])
            return Response(TaskSerializer(task).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
