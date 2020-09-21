from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='note'),
    path('delete/<int:id>', views.deletefunc, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('post', views.post_func, name='post')
]