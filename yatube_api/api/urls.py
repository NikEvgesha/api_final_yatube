from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from api.views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, basename='post')
router_v1.register('groups', GroupViewSet, basename='group')
router_v1.register('follow', FollowViewSet, basename='follow')

comment_router_v1 = routers.NestedDefaultRouter(
    router_v1,
    'posts',
    lookup='post'
)
comment_router_v1.register(
    'comments',
    CommentViewSet,
    basename='post-comments'
)

urlpatterns_v1 = [
    path('', include(router_v1.urls)),
    path('', include(comment_router_v1.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt'))
]

urlpatterns = [
    path('v1/', include(urlpatterns_v1))
]
