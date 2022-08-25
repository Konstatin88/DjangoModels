from django.urls import path
from .views import all_news,one_new
urlpatterns = [
    path('', all_news),
    path('<int:id>/', one_new, name='news_detail')
]