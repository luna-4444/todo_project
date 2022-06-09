from django.urls import path
from . import views

from rest_framework.routers import SimpleRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token

router = SimpleRouter()
router.register(r'tasks', views.TodoTasksViewSet)

urlpatterns = router.urls


urlpatterns += [
    path("todo_tasks", views.TodoTasksAPI.as_view(), name="todo_tasks"),
    path("auth_token", obtain_auth_token, name="auth_token"),
    path("jwt_token", obtain_jwt_token, name="jwt_token"),
]
