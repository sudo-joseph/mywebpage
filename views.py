import requests
from django.http import HttpResponse
from django.shortcuts import render
import datetime
import glob
import os
import copy
import markdown
import utils

def index(request):
    options=utils.gen_preview_pages("blog","index")
    return render(request, 'preview_base.html', options)

def projects(request):
    context = utils.github_api(request)
    return render(request, 'git_repo_base.html', context)

def contact(request):
    options=utils.gen_content_post('contact','content','contact')
    return render(request, 'content_base.html', options)

def post(request,title,root):
    options=utils.gen_content_post(title,request.resolver_match.url_name,root)
    return render(request, 'content_base.html', options)
