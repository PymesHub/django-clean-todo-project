from typing import List
from .entities import Task

class TaskRepository:
    def get_all_tasks(self) -> List[Task]:
        raise NotImplementedError
    
    def get_task_by_id(self, task_id: int) -> Task:
        raise NotImplementedError
    
    def create_task(self, task: Task) -> Task:
        raise NotImplementedError
    
    def update_task(self, task: Task) -> Task:
        raise NotImplementedError
    
    def delete_task(self, task_id: int) -> None:
        raise NotImplementedError