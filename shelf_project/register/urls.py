from django.conf.urls import include, url

from . import views as v # import views so we can use them in urls.


urlpatterns = [

    url("register", v.register, name="register"),

]
