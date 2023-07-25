from django.forms import ModelForm

from TodoList.models import Todo
class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title' , 'status' , 'priority']