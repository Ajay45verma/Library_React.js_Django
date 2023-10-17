from django.urls import path
from . import views
urlpatterns = [
    path('test',views.Demo_test ,name="Demo_test"),
    path('user',views.UserVi ,name="UserVi"),
   
]