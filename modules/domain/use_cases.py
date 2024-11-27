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
            return self.repository.create_task(new_task)
    
    def delete_task(self, task_id: int) -> None:
          return self.repository.delete_task(task_id)
    
    def get_task_by_id(self, task_id: int) -> Task:
          return self.repository.get_task_by_id(task_id)
    
    def update_task(self, task_id: int, title: str, description: str, completed: bool) -> Task:
          task = self.repository.get_task_by_id(task_id)
          task.title = title
          task.description = description
          task.completed = completed
          return self.repository.update_task(task)