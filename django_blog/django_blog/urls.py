"""
URL configuration for django_blog project.

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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("about/", views.about_blog),
    path("", views.show_home, name='home'),
    path("set-password/", views.set_password),
    path("set-userdata/", views.set_userdata),
    path("register/", views.create_new_user),
    path("deactivate/", views.deacivate_account),
    path("login/", views.login_page),
    path("logout/", views.logout_user),
    path("topics/", views.view_topics),
    path("<str:name>/comment/", views.article_comment, name='article'),
    path("create/", views.create_article),
    path("<article>/update/", views.article_update),
    path("<article>/delete/", views.article_delete),
    path("<str:name>/", views.view_article, name='article'),
    path("topics/<str:topic>/", views.topic_change),
    path("topics/<str:topic>/subscribe/", views.subscribe_topic),
    path("topics/<str:topic>/unsubscribe/", views.unsubscribe_topic),
    path("profile/<str:username>/", views.user_profile),
]
