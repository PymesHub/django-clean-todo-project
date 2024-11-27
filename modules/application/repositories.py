from typing import List
from modules.domain.entities import Task
from modules.domain.interfaces import TaskRepository
from tasks.models import TaskModel

class DjangoTaskRepository(TaskRepository):

    def get_all_tasks(self) -> List[Task]:
        tasks = TaskModel.objects.all()
        return [Task(id=task.id, title=task.title, description=task.description, completed=task.completed ) for task in tasks]
    
    def create_task(self, task: Task) -> Task:
        task_model = TaskModel.objects.create(title=task.title, description=task.description, completed=task.completed)
        return Task(id=task_model.id, title=task_model.title, description=task_model.description, completed=task_model.completed)
    
    def delete_task(self, task_id: int) -> None:
        try:
            task_model = TaskModel.objects.get(id=task_id)
            task_model.delete()
            return True
        except TaskModel.DoesNotExist:
            return False

    def get_task_by_id(self, task_id: int) -> Task:
        task = TaskModel.objects.get(id=task_id)
        return Task(id=task_id, title=task.title, description=task.description, completed=task.completed)
    
    def update_task(self, task: Task) -> Task:
        task_model = TaskModel.objects.get(id=task.id)
        if task.title is not None:
            task_model.title = task.title
        if task.description is not None:
            task_model.description = task.description
        if task.completed is not None:
            task_model.completed = task.completed
        task_model.save()
        return Task(id=task_model.id, title=task_model.title, description=task_model.description, completed=task_model.completed)