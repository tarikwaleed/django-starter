from django.urls import path

from . import views

# urlpatterns = [path(route="<str:name>", view=views.greetings, name="greetings")]
urlpatterns = [
    path(route="<str:captured_values>", view=views.greetings, name="greetings")
]
