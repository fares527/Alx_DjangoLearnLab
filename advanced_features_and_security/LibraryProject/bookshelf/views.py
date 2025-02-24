from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Article
from django.contrib.auth.models import Group
from django.http import HttpResponseForbidden

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'app_name/article_list.html', {'articles': articles})

@permission_required('app_name.can_create', raise_exception=True)
def article_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Article.objects.create(title=title, content=content)
        return redirect('article_list')
    return render(request, 'app_name/article_create.html')

@permission_required('app_name.can_edit', raise_exception=True)
def article_edit(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.save()
        return redirect('article_list')
    return render(request, 'app_name/article_edit.html', {'article': article})

@permission_required('app_name.can_delete', raise_exception=True)
def article_delete(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.delete()
    return redirect('article_list')

def article_view(request, article_id):
    if request.user.has_perm('app_name.can_view'):
        article = get_object_or_404(Article, pk=article_id)
        return render(request, 'app_name/article_view.html', {'article': article})
    else:
        return HttpResponseForbidden("You do not have permission to view this article.")
