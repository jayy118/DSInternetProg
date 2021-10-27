from django.shortcuts import render
from django.views.generic import ListView, DetailView

from.models import Post

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk'
#    template_name = 'blog/post_list.html'
# post_list.html

class PostDetail(DetailView):
    model = Post
# post_detail.html

#def index(request) :
#    posts = Post.objects.all().order_by('-pk')
#
#    return render(request, 'blog/post_list.html',
#                  {
#                      'posts': posts,
#                  }
#                  )
#
#def single_post_page(request, pk) :
#    post = Post.objects.get(pk=pk) -> 괄호속 조건을 만족하는 레코드를 가져와리/ 매개변수 pk= post pk인 경우
#
#    return render(request, 'blog/post_detail.html',
#                 {
#                      'post': post,
#                  }
#                  )
