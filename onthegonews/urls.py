from django.contrib import admin
from django.urls import path
from news.views import my_article

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', my_article, name='news'),
]
