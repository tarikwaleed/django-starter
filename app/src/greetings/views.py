from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# def greetings(request: HttpRequest, **captured_values):
def greetings(request: HttpRequest, captured_values):
    # return HttpResponse(f"Hello, {captured_values.get('name')}")
    return HttpResponse(f"Hello, {captured_values}")
