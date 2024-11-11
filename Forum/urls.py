from django.urls import path, re_path, include
from .views import RegisterView, CustomTokenObtainPairView, TopicDetailView, TopicListCreateView, PostDetailView, PostListCreateView, CommentListCreateView, CommentDetailView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('topic/', TopicListCreateView.as_view(), name='token_list_created'),
    path('topic/<int:pk>/', TopicDetailView.as_view(), name='topic_detail'),

    path('post/', PostListCreateView.as_view(), name='post_list_created'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

    path('comments/', CommentListCreateView.as_view(), name='commit_;ist_created'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='commit_detail'),

    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
