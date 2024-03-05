"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

# settings.configure()
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include( 'auth_api.urls', namespace="auth_api")),
    path('api/users/', include( 'users_api.urls', namespace="users_api")),
    path('api/forums/', include( 'forums_api.urls', namespace="forums_api")),
    path('api/messages/', include( 'messages_api.urls', namespace="messages_api")),

    path('api/faculties/', include( 'faculties_api.urls', namespace="faculties_api")),
    path('api/departments/', include( 'departments_api.urls', namespace="departments_api")),
    path('api/courses/', include( 'courses_api.urls', namespace="courses_api")),
    path('api/inbox/', include( 'inbox_api.urls', namespace="inbox_api")),

    path('api/posts/',include('posts_api.urls',namespace="post_api")),
    path('api/comments/',include('comments_api.urls',namespace="comments_api")),
    path('api/recommendations/',include('recommendations_api.urls',namespace="recommendations_api")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


