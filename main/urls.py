from django.urls import path
from .views import Post_list,Post_Detail,Category

urlpatterns = [
    path('', Post_list.as_view()),
    path('blog/<slug:slug>/', Post_Detail.as_view(), name='post_detail'),
    path('category/<slug:slug>/', Category.as_view(), name='post_category'),
]
