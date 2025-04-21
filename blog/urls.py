from django.urls import path
from blog.views import index, post_detail, get_ip

app_name = "blog"

urlpatterns = [path('', index, name="index"),
               path('post/<slug>/', post_detail, name="post-detail"),
               path('get_ip', get_ip, name="get-ip")
              ]