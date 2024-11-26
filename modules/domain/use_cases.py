from typing import List
from .interfaces import TaskRepository
from .entities import Task

class TaskUseCase:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def get_all_tasks(self) -> List[Task]:
            return self.repository.get_all_tasks()
        
    def create_task(self, title: str, description: str) -> Task:
            new_task = Task(id=None, title=title, description=description)
            return self.repository_create_task(new_task)