from django.conf import settings
from django.urls import path
from .views import BlogListView, BlogListDetail

from django.conf.urls.static import static

urlpatterns = [
    path('', BlogListView.as_view(), name='List, Create Blog'),
    path('<int:pk>/', BlogListDetail.as_view(), name='Retrieve, Update, Delete a Blog'),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)