from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,DetailView,UpdateView
from .models import Todo
from .forms import TodoForm

# Create your views here.
#def home(request):
  #  todo = Todo.objects.all()
  #  return render(request,'list.html',{'todos':todo})

class TodoCreateView(CreateView):
    model = Todo
    fields = ("title","start_date",'start_time')
    template_name = "todo.html"
    success_url ='/home'
    
class TodoListView(ListView):
    model = Todo
    template_name = "list.html"
    ordering = ['start_time']
    context_object_name = 'todos'

class TodoDeleteView(DeleteView):
     model = Todo
     template_name = "delete.html"
     success_url = '/home'
class TodoDetailView(DetailView):
    model = Todo
    template_name = "detail.html"

class TodoUpdateView(UpdateView):
    model = Todo
    template_name = "todo.html"
    fields = ("title","start_date",'start_time')
