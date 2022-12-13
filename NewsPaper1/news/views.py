from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
      model = Post
      # ordering = 'categories'
      template_name = 'news.html'
      context_object_name = 'post'



class PostDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'new.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'post'