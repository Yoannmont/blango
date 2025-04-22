from django.urls import path, include
from blog.views import index, post_detail, get_ip

app_name = "blog"

urlpatterns = [path('', index, name="index"),
               path('post/<slug>/', post_detail, name="post-detail"),
               path('get_ip/', get_ip, name="get-ip"),
               path('api/v1/', include('blog.api_urls')),
              ]