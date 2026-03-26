from rest_framework import viewsets, permissions, filters
from rest_framework.generics import get_object_or_404
from posts.models import Post, Group
from api.serializers import PostSerializer, \
    GroupSerializer, CommentSerializer, FollowSerializer
from api.permissions import IsAuthorOrReadOnly
from rest_framework import serializers
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def list(self, request, *args, **kwargs):
        limit = request.query_params.get('limit')
        offset = request.query_params.get('offset')

        queryset = self.filter_queryset(self.get_queryset())

        if limit is not None or offset is not None:
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

        # Иначе возвращаем просто список без пагинации
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = None


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = None

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        return post.comments.all()

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
    pagination_class = None

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        following = serializer.validated_data['following']
        if following == self.request.user:
            raise serializers.ValidationError(
                "Нельзя подписаться на самого себя!"
            )
        serializer.save(user=self.request.user)
