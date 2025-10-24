from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import KnowledgeEntry
from .forms import KnowledgeEntryForm

# 🧠 List all knowledge entries for the logged-in user
@login_required
def knowledge_list(request):
    entries = KnowledgeEntry.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'knowledge/list.html', {'entries': entries})

# ➕ Create new entry
@login_required
def add_knowledge(request):
    if request.method == 'POST':
        form = KnowledgeEntryForm(request.POST, request.FILES)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('knowledge_list')
    else:
        form = KnowledgeEntryForm()
    return render(request, 'knowledge/add.html', {'form': form})

# ✏️ Edit entry
@login_required
def edit_knowledge(request, pk):
    entry = get_object_or_404(KnowledgeEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        form = KnowledgeEntryForm(request.POST, request.FILES, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('knowledge_list')
    else:
        form = KnowledgeEntryForm(instance=entry)
    return render(request, 'knowledge/edit.html', {'form': form})

# ❌ Delete entry
@login_required
def delete_knowledge(request, pk):
    entry = get_object_or_404(KnowledgeEntry, pk=pk, user=request.user)
    entry.delete()
    return redirect('knowledge_list')
