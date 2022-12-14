from django_filters import FilterSet
from .models import Post

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
    date_time__gt = django_filters.DateFilter(
        field_name="time_in_post", label="Поиск по дате", lookup_expr='gt',
        widget=django.forms.DateInput(
            attrs={'type': 'date', 'class': "form-control"}))

   class Meta:

       model = Post

       fields = {
           'title': ['icontains'],
           'post_text': ['icontains'],
           'time_in_post': ['gte',],
       }