# pages/urls.py
from django.urls import path

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from django.contrib.auth import views as authViews
from .views import HomePageView, PayPageView, AuthPageView, RegisterPageView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'), 
    path('', views.index, name='home'),  
    path('catalog/', views.catalog, name = 'catalog'),
    path('reviews/', views.reviews_create, name = 'reviews'),
    path('history/', views.reviews, name = 'history'),
    path('pay/', PayPageView.as_view(), name = 'pay'),
    path('news/', views.news, name = 'news'),
    path('auth/', views.login, name = 'auth'),
    path('register/', views.register, name = 'register'),
    path('exit/', authViews.LogoutView.as_view(), name='exit')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)