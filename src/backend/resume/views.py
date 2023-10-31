# from django.conf import settings
# from django.core.paginator import Paginator
# from django.shortcuts import get_object_or_404, render, redirect

# from resume.models import Resume
# from user.models import User

# def paginations(page_number, page_list):
#     paginator = Paginator(page_list, settings.NUMBER_OF_POSTS)
#     return paginator.get_page(page_number.GET.get('page'))


# def index(request):

#     return render(request, 'resume/index.html', context)


# def resume(request, username):
#     author = get_object_or_404(User, username=username)
#     author_posts = author.posts.select_related('group')
#     page_obj = paginations(page_number=request, page_list=author_posts)
#     following = (
#         request.user.is_authenticated
#         and author.following.filter(
#             user=request.user
#         )
#     )
#     context = {
#         'author': author,
#         'page_obj': page_obj,
#         'following': following,
#     }
#     return render(request, 'posts/profile.html', context)
