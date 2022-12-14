from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy

class PostList(ListView):
      model = Post
      ordering = '-time_in_post'
      template_name = 'news.html'
      context_object_name = 'post'
      paginate_by = 10

      # Переопределяем функцию получения списка товаров
      def get_queryset(self):
          # Получаем обычный запрос
          queryset = super().get_queryset()
          # Используем наш класс фильтрации.
          # self.request.GET содержит объект QueryDict, который мы рассматривали
          # в этом юните ранее.
          # Сохраняем нашу фильтрацию в объекте класса,
          # чтобы потом добавить в контекст и использовать в шаблоне.
          self.filterset = PostFilter(self.request.GET, queryset)
          # Возвращаем из функции отфильтрованный список товаров
          return self.filterset.qs

      def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          # Добавляем в контекст объект фильтрации.
          context['filterset'] = self.filterset
          return context



class PostDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'post'


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

class PostDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post_list')

class ArticleCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['title'] = "Добавить"
        return context


class ArticleUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['title'] = "Редактировать"
        return context


class ArticleDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('posts_list')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['title'] = "Удалить"
        context['previous_page_url'] = reverse_lazy('posts_list')
        return context