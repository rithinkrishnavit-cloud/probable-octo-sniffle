from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("delete_task/<int:id>/", views.delete_task, name="delete_task"),
    path("complete_task/<int:id>/", views.complete_task, name="complete_task"),
    path("update_task/<int:id>/", views.update_task, name="update_task"),
]
