from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from .models import Post, Comment, Quote
from django.http import JsonResponse
import random
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import update_session_auth_hash

User = get_user_model()


def cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        bio = request.POST.get('bio')
        profile_picture = request.FILES.get('profile_picture')

        if password1 != password2:
            messages.error(request, 'As senhas não coincidem.')
            return redirect('cadastro')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já existe.')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado.')
            return redirect('cadastro')

        user = User.objects.create_user(
            username=username,
            password=password1,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.bio = bio
        if profile_picture:
            user.profile_picture = profile_picture
        user.save()

        login(request, user)
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('app_index')

    return render(request, 'app/cadastro.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        errors = []

        # Atualiza informações básicas
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.bio = request.POST.get('bio')

        # Atualização de senha
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if current_password and new_password:
            if user.check_password(current_password):
                if new_password == confirm_password:
                    user.set_password(new_password)
                    update_session_auth_hash(request, user)
                    messages.success(request, 'Senha alterada com sucesso!')
                else:
                    errors.append('A nova senha e a confirmação não coincidem.')
            else:
                errors.append('Senha atual incorreta.')

        if not errors:
            user.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('app_index')  # Redireciona para home após sucesso

        for error in errors:
            messages.error(request, error)

    return render(request, 'app/edit_profile.html')



@login_required(login_url='app_login')
def index(request):
    # Busca todos os posts, ordenados por data
    posts = Post.objects.all().order_by('-created_at')

    # Posts trending (últimos 7 dias, ordenados por curtidas)
    trending_posts = get_trending_posts(limit=5)
    paginated_posts = paginate_queryset(request, posts)

    return render(request, 'app/app.html', {'posts': paginated_posts, 'trending_posts': trending_posts})


@login_required(login_url='app_login')
def trending(request):
    # Calcula a data de 7 dias atrás
    seven_days_ago = timezone.now() - timezone.timedelta(days=7)

    # Filtra os posts dos últimos 7 dias e ordena por curtidas
    posts = Post.objects.filter(
        created_at__gte=seven_days_ago  # Filtra posts criados nos últimos 7 dias
    ).annotate(
        total_likes=Count('likes')  # Conta o número de curtidas
    ).order_by(
        '-total_likes'  # Ordena por curtidas em ordem decrescente
    )

    return render(request, 'app/trending.html', {'posts': posts})


@login_required(login_url='app_login')
def relevance(request):
    # Annotate cada post com o número de curtidas e ordena por curtidas em ordem decrescente
    posts = Post.objects.annotate(total_likes=Count('likes')).order_by('-total_likes')

    # Posts trending (últimos 7 dias, ordenados por curtidas)
    trending_posts = get_trending_posts()
    paginated_posts = paginate_queryset(request, posts)

    return render(request, 'app/app_relevance.html', {'posts': paginated_posts, 'trending_posts': trending_posts})


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


@login_required(login_url='app_login')
def post_list(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    trending_posts = get_trending_posts()

    return render(request, 'app/post.html', {'post': post, 'trending_posts': trending_posts})


@login_required(login_url='app_login')
def create_post(request):
    if request.user.is_staff:
        return HttpResponseForbidden("Você não tem permissão para criar post.")
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.user
        Post.objects.create(title=title, content=content, author=author)
        return redirect('app_index')
    return render(request, 'app/create_post.html')


@login_required(login_url='app_login')
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

    trending_posts = get_trending_posts()

    return render(request, 'app/edit_post.html', {'post': post, 'trending_posts': trending_posts})


@login_required(login_url='app_login')
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Verifica se o usuário é o autor do post. Staff faz a moderação e pode deletar qualquer post
    if request.user != post.author and not request.user.is_staff:
        return HttpResponseForbidden("Você não tem permissão para excluir este post.")

    # Exclui o post
    post.delete()

    # Redireciona para a página inicial após a exclusão
    return redirect('app_index')


@login_required(login_url='app_login')
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user.is_staff:
        return HttpResponseForbidden("Você não tem permissão para criar comentários.")
    if request.method == 'POST':
        content = request.POST.get('content')
        author = request.user
        Comment.objects.create(content=content, author=author, post=post)
    return redirect('post_list', post_id=post.id)


@login_required(login_url='app_login')
def edit_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    # Verifica se o usuário é o autor do comentário
    if request.user != comment.author:
        return HttpResponseForbidden("Você não tem permissão para editar este comentário.")
    if request.method == 'POST':
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('post_list', post_id=post_id)

    trending_posts = get_trending_posts()

    return render(request, 'app/edit_comment.html', {'comment': comment, 'trending_posts': trending_posts})


@login_required(login_url='app_login')
def delete_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Verifica se o usuário é o autor do comentário. Staff faz a moderação e pode deletar qualquer comment
    if request.user != comment.author and not request.user.is_staff:
        return HttpResponseForbidden("Você não tem permissão para excluir este comentário.")

    # Exclui o post
    comment.delete()

    # Redireciona de volta para a página do post
    return redirect('post_list', post_id=post_id)


@login_required(login_url='app_login')
def like_post(request, post_id):
    if request.user.is_staff:
        return JsonResponse({"error": "Usuários staff não podem curtir posts."}, status=403)

    post = get_object_or_404(Post, id=post_id)

    # Verifica se o usuário já curtiu o post
    if request.user in post.likes.all():
        post.likes.remove(request.user)  # Descurtir
    else:
        post.likes.add(request.user)  # Curtir

    return JsonResponse({"likes": post.likes.count()})


@login_required(login_url='app_login')
def bookmark_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user in post.bookmarks.all():
        post.bookmarks.remove(request.user)  # Remover dos favoritos
        bookmarked = False
    else:
        post.bookmarks.add(request.user)  # Adicionar aos favoritos
        bookmarked = True

    return JsonResponse({"bookmarked": bookmarked})


@login_required(login_url='app_login')
def bookmarked_posts(request):
    posts = request.user.bookmarked_posts.all()

    trending_posts = get_trending_posts()

    return render(request, 'app/bookmarked_posts.html', {'posts': posts, 'trending_posts': trending_posts})


@login_required(login_url='app_login')
def user_posts(request, username):
    user_profile = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user_profile).order_by('-created_at')

    trending_posts = get_trending_posts()

    return render(request, 'app/user_posts.html',
                  {'user_profile': user_profile, 'posts': posts, 'trending_posts': trending_posts})


def get_trending_posts(limit=5, days=14):
    """Retorna os posts mais curtidos dos últimos 'days' dias, limitados a 'limit' resultados."""
    since_date = timezone.now() - timezone.timedelta(days=days)
    return Post.objects.filter(
        created_at__gte=since_date
    ).annotate(
        total_likes=Count('likes')
    ).order_by(
        '-total_likes'
    )[:limit]


def paginate_queryset(request, queryset, per_page=5):
    """Paginação genérica para qualquer queryset."""
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, per_page)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    return paginated_queryset
