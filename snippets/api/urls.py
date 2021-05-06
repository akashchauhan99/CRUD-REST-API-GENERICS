from .views import BlogList, CreateApiViewApi, CreateBlogApiView
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('createBlog', CreateBlogApiView.as_view(), name="create blog"),
    path('create_blog', CreateApiViewApi.as_view(), name="create_blog"),
    path('blog_list', BlogList.as_view(), name="blog_list"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
