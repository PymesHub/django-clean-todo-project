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