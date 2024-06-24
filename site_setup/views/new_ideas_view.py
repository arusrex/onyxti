from home.models import NewIdeas, NewIdeasItems
from home.forms import NewIdeasForm, NewIdeasItemsForm
from django.shortcuts import render, redirect
from django.contrib import messages

def new_ideas(request):
    obj = NewIdeas.objects.first()
    form = NewIdeasForm(instance=obj)

    if form.is_valid():
        form = NewIdeasForm(request.POST, instance=obj)
        form.save()
        messages.success(request, 'Saved!')
        return redirect('home:new_ideas')
    
    context = {
        'obj':obj,
        'form': form,
        }
    
    return render(request, 'dashboard/pages/new_ideas.html', context)

def new_idea(request, id):
    pass

def edit_new_idea(request, id):
    pass

def delete_new_idea(request, id):
    pass