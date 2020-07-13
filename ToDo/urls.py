from django.urls import path
from .views import TodoCreateView,TodoListView,TodoDeleteView,TodoDetailView,TodoUpdateView
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('home/new/',TodoCreateView.as_view(), name='home'),
    path('home/<int:pk>/',TodoDetailView.as_view(), name='detail'),
    path('home/<int:pk>/delete/',TodoDeleteView.as_view(), name='delete'),
    path('home/<int:pk>/update/',TodoUpdateView.as_view(), name='update'),
    path('home/',TodoListView.as_view(), name='list_view'),
    path('logout/',LogoutView.as_view(template_name="base.html"), name='logout'),
    path('login/',LoginView.as_view(template_name="login.html"), name='login'),
]
