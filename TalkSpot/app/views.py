from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Post, Comment


def index(request):
    posts = Post.objects.all().order_by('-created_at')  # Busca todos os posts, ordenados por data
    return render(request, 'app/app.html', {'posts': posts})


def app_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('app_index')
        messages.error(request, 'Invalid username or password')
    return render(request, 'app/login.html')


def app_logout(request):
    logout(request)
    return redirect('app_login')


def post_list(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'app/post.html', {'post': post})


def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.user
        Post.objects.create(title=title, content=content, author=author)
        return redirect('app_index')
    return render(request, 'app/create_post.html')


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # Verifica se o usuário é o autor do post
    if request.user != post.author:
        return HttpResponseForbidden("Você não tem permissão para editar este post.")
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('post_list', post_id=post.id)
    return render(request, 'app/edit_post.html', {'post': post})


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Verifica se o usuário é o autor do post
    if request.user != post.author:
        return HttpResponseForbidden("Você não tem permissão para excluir este post.")

    # Exclui o post
    post.delete()

    # Redireciona para a página inicial após a exclusão
    return redirect('app_index')


def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        author = request.user
        Comment.objects.create(content=content, author=author, post=post)
    return redirect('post_list', post_id=post.id)


def edit_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    # Verifica se o usuário é o autor do comentário
    if request.user != comment.author:
        return HttpResponseForbidden("Você não tem permissão para editar este comentário.")
    if request.method == 'POST':
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('post_list', post_id=post_id)
    return render(request, 'app/edit_comment.html', {'comment': comment})


def delete_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Verifica se o usuário é o autor do comentário
    if request.user != comment.author:
        return HttpResponseForbidden("Você não tem permissão para excluir este comentário.")

    # Exclui o post
    comment.delete()

    # Redireciona de volta para a página do post
    return redirect('post_list', post_id=post_id)
