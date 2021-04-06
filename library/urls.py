from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from book.views import BookViewSet
from author.views import AuthorViewSet
from genre.views import GenreViewSet
from user.views import UserViewSet

router = DefaultRouter()
# router.register(r'books', BookViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    path('books/<int:pk>/', BookViewSet.as_view({'get': 'retrieve', 'update': 'update_book'})),
    path('books/', BookViewSet.as_view({'get': 'list',
                                        'post': 'add_book',
                                        'delete': 'remove_book'})),
]
