from django.urls import path, include
from django.conf.urls import url
from . import views as viewStore # import views so we can use them in urls.
from register import views as v

urlpatterns = [
    url(r'^$', viewStore.index), # "/store" will call the method "index" in "views.py"
    url(r'^register/', v.register),
    #path('register/', v.register, name="register"),
    #path('', include("main.urls")),
]
	