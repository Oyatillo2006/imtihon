
from django.contrib import admin
from django.urls import path
from home.views import home, delete, edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home),
    path("delete/<int:id>/", delete),
    path("edit/<int:id>/", edit),
]
