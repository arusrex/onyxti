from django.shortcuts import render, redirect
from home.models import Team
from home.forms.team import TeamForm
from django.contrib import messages

def team(request):
    obj = Team.objects.first()
    form = TeamForm(instance=obj)

    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved!')
            return redirect('home:team')
        

    context = {
        'obj': obj,
        'form': form,
    }

    return render(request, 'dashboard/pages/team.html', context)