from django.urls import path,re_path
from . import views

app_name = "articles"
urlpatterns = [
    path('', views.articles_list,name="list"),
    path('create',views.create_article, name='create'),
    #path('<slug>',views.article_detail,name="detail"),
    re_path(r'detail/(?P<slug>[-\w]+)/', views.article_detail, name='detail'),
]
