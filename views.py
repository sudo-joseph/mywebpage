"""
View functions for my django site.

This script can be used to generate a new blog page based on template, and
provides some helper functions for generating content for site pages.
"""

# from django.http import HttpResponse
from django.shortcuts import render
import utils


def index(request):
    """Render index page."""
    options = utils.gen_preview_pages("blog", "index")
    return render(request, 'preview_base.html', options)


def projects(request):
    """Render projects page."""
    context = utils.github_repos(request)
    return render(request, 'git_repo_base.html', context)


def contact(request):
    """Render contact page."""
    options = utils.gen_content_post('contact', 'content', 'contact')
    return render(request, 'content_base.html', options)


def post(request, title, root):
    """Render blog post pages."""
    options = utils.gen_content_post(title,
                                     request.resolver_match.url_name,
                                     root)
    return render(request, 'content_base.html', options)
