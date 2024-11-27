from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from modules.domain.use_cases import TaskUseCase
from modules.application.serializer import TaskSerializer
from modules.application.repositories import DjangoTaskRepository
from rest_framework.exceptions import NotFound
from tasks.models import TaskModel

class TaskAPIView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        repository = DjangoTaskRepository()
        self.use_case = TaskUseCase(repository)

    def get(self, request, task_id=None):
        if task_id is not None:
            try:
                task = self.use_case.get_task_by_id(task_id)
                serializer = TaskSerializer(task)
                return Response(serializer.data)
            except TaskModel.DoesNotExist:
                raise NotFound("Task not found.")
        else:
            tasks = self.use_case.get_all_tasks()
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data) 
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = self.use_case.create_task(serializer.validated_data['title'], serializer.validated_data['description'])
            return Response(TaskSerializer(task).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, task_id=None):
        task_deleted = self.use_case.delete_task(task_id)

        if task_deleted:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({ 'detail': 'Task not found' }, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, task_id=None):
        if task_id is None:
            return Response({ "error": "Task ID is required for updates" }, status=status.HTTP_400_BAD_REQUEST)
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            try:
                task = self.use_case.update_task(
                    task_id, 
                    serializer.validated_data['title'], 
                    serializer.validated_data['description'],
                    serializer.validated_data['completed']
                )
                return Response(TaskSerializer(task).data)
            except TaskModel.DoesNotExist:
                raise NotFound("Task not found")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, task_id=None):
        if task_id is None:
            return Response({ "error": "Task ID is required for partial updates." }, status=status.HTTP_400_BAD_REQUEST)
        try:
            task = self.use_case.get_task_by_id(task_id)
        except:
            raise NotFound("Task not found.")
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            updated_task = self.use_case.update_task(
                task_id,
                serializer.validated_data.get('title', task.title),
                serializer.validated_data.get('description', task.description),
                serializer.validated_data.get('completed', task.completed)
            )
            return Response(TaskSerializer(updated_task).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    