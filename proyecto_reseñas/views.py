from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


def inicio(request):
    contexto = {}
    http_response= render(
        request=request,
        template_name='blog/inicio.html',
        context=contexto,
    )
    return http_response