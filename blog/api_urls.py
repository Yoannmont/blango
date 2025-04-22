from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog.api.views import UserDetail, TagViewSet, PostViewSet
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
import os
from rest_framework.routers import DefaultRouter

schema_view = get_schema_view(
    openapi.Info(
        title="Blango API",
        default_version="v1",
        description="API for Blango Blog",
    ),
    url=f"https://{os.environ.get('CODIO_HOSTNAME')}-8000.codio.io/api/v1/",
    public=True,
)


tag_router = DefaultRouter()
tag_router.register("tags", TagViewSet)

post_router = DefaultRouter()
post_router.register("posts", PostViewSet)

urlpatterns = [
    path("users/<str:email>/", UserDetail.as_view(), name="api_user_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
  re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path('', include(tag_router.urls)),
    path('', include(post_router.urls)),
]