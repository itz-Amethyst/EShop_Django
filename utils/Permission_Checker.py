# ! another way to pass data
from django.http import HttpRequest
from django.urls import reverse


# def permission_checker_decorator_factory(data):
#     def permission_checker_decorator(func):
#
#
#         if .....
#
#
#     return permission_checker_decorator()
def permission_checker_decorator(func):
    def wrapper(request: HttpRequest, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return func(request, *args, **kwargs)
        else:
            return reverse('login_page')

    return wrapper()

