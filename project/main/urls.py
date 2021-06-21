from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('python/info/', views.school_info, name = 'python'),
    path('register/user', views.register_user, name = 'register_user'),
    path('login/user', views.login_user, name = 'login_user'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
