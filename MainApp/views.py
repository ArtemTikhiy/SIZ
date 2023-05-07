from typing import Union

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# from MainApp.models import Snippet, Comment
# from MainApp.forms import SnippetForm, UserRegistrationForm, CommentForm

from django.shortcuts import render

# Create your views here.


def index_page(request):
    context = {'pagename': 'Главная страница'}
    return render(request, 'pages/index.html', context)