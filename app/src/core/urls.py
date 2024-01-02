from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(route="greet/", view=include("greetings.urls")),
    path(route="admin/", view=admin.site.urls),
]
