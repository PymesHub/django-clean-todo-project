from django.contrib import admin
from django.urls import path
from tasks.views import TaskAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/tasks/", TaskAPIView.as_view(), name='task-list-create'),
    path("api/tasks/<int:task_id>", TaskAPIView.as_view())
]
