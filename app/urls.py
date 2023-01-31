from django.urls import path
from . import views

urlpatterns = [
    path("app",views.main,name="Home-page"),
    path('app/<id>', views.main_detail, name="id-page"),
    path('collections/<int:pk>',views.collector_path,name="collector-path")
]
