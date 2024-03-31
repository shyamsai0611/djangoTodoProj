from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Todo
from .form import craeteTodoForm

def create_todo(request):
    if request.method == 'POST':
        form = craeteTodoForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            var.save()
            messages.success(request,'Todo item added')
            return redirect('all-todos')
        else:
            messages.warning(request,'Something went wrong')
            return redirect('create-todo')
    else:
        form = craeteTodoForm()
        context = {'form':form}
        return render(request,'todo/create_todo.html',context)
    
@login_required
def all_todos(request):
    obj = Todo.objects.filter(user=request.user).order_by('-date_created')
    context = {'obj':obj}
    return render(request,'todo/all_todos.html',context)

# def mark_as_completed(request, pk):
#     obj = Todo.objects.get(pk=pk)
#     obj.is_completed = True
#     obj.save()
#     messages.success(request,'Todo marked as completed')
#     return redirect('all-todos')

def mark_as_completed(request, pk):
    obj = get_object_or_404(Todo, pk=pk)
    obj.is_completed = True
    obj.save()
    messages.success(request, 'Todo marked as completed')
    print(f'Todo ID {pk} marked as completed. is_completed: {obj.is_completed}')
    return redirect('all-todos')




