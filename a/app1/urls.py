from django.urls import path
from app1 import views
urlpatterns=[
    path("silk/<int:id>",views.silk)
]