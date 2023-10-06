from django.http import HttpRequest, HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect


def my_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse('homepage')


def dynamic_view(request: HttpRequest, name: str) -> HttpResponse:
    return HttpResponse(f"name is {name}")


def addition(request: HttpRequest, num_1: int, num_2: int) -> HttpResponse:
    return HttpResponse(f"{num_1} + {num_2} = {num_1 + num_2}")


def path_view(request: HttpRequest, file_path: str) -> HttpResponse:
    return HttpResponse(f"{file_path = }")


def about_blog(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"This is blog")


def show_home(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"This is home page")


def view_article(request: HttpRequest, name: str) -> HttpResponse:
    return HttpResponse(f"This is page of article {name}")


def article_comment(request: HttpRequest, name: str,) -> HttpResponse:
    return HttpResponse(f"This is comment of article {name}")


def create_article(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"This is the article creation form page")


def article_update(request: HttpRequest, article: str) -> HttpResponse:
    return HttpResponse(f"This is page for update  {article} ")


def article_delete(request: HttpRequest, article: str) -> HttpResponse:
    return HttpResponse(f"This is page for delete  {article} ")


def view_topics(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"This is all topics on blog")


def topic_change(request: HttpRequest, topic: str) -> HttpResponse:
    return HttpResponse(f"Topic_change")


def subscribe_topic(request: HttpRequest, topic: str) -> HttpResponse:
    return HttpResponse(f"Subscribe topic")


def unsubscribe_topic(request: HttpRequest, topic: str) -> HttpResponse:
    return HttpResponse(f"Unsubscribe topic")


def user_profile(request: HttpRequest, username: str) -> HttpResponse:
    return HttpResponse(f"Username is {username}")


def set_password(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"Please, set your new password")


def set_userdata(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"Please, update user info")


def deacivate_account(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"On this page you can deactivate your account")


def create_new_user(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"Create new profile!")


def login_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"Hello! log in, please!")


def logout_user(request: HttpRequest) -> redirect:
    logout(request)
    return redirect("home")
