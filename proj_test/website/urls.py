from django.urls import path
from .views import hello_blog, post_detail
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', hello_blog, name='home'),
    path('post/<int:id>/', post_detail, name='post_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
