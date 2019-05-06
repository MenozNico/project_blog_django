from django.urls import path
from . import views
from blog.views import BlogDetail, BlogListIndex


urlpatterns = [
    path("", BlogListIndex.as_view(), name="blog_index"),
    # path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("<int:pk>/", BlogDetail.as_view(), name="blog_detail"),
    path("<category>/", views.blog_category, name="blog_category")
]
