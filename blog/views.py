from django.shortcuts import render
from django.views.generic import ListView, DetailView

from.models import Post, Category

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

#    template_name = 'blog/post_list.html'
# post_list.html

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)
    return render(request, 'blog/post_list.html',
                  {
                      'post_list' : post_list,
                      'categories' : Category.objects.all(),
                      'no_category_post_count' : Post.objects.filter(category=None).count(),
                      'category' : category,
                  }
                  )

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
