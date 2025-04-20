from django.urls import path
from blog.views import index, post_detail

app_name = "blog"

urlpatterns = [path('', index, name="index"),
               path('post/<slug>/', post_detail, name="post-detail"),
              ]