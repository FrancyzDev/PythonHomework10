from django.shortcuts import render, get_object_or_404
from django.views import View
from branches.models import Branch

def branches_list(request):
    branches_data = Branch.objects.all()
    return render(request, 'branches_list.html', {'title': 'Філії','branches': branches_data})

def branch_detail(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    return render(request, 'branches_detail.html', {
        'branch': branch,
    })
    