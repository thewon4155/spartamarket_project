from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views as project_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('accounts/', include('accounts.urls')),
    path('bookmark/', include('bookmark.urls')),
    path('register/', project_views.register, name='register'),
    path('profile/', project_views.profile, name='profile'),
    path('login/', project_views.login, name='login'),
]
