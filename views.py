import requests
from django.http import HttpResponse
from django.shortcuts import render
import datetime
import glob
import os
import copy
import markdown

def index(request):
    options=gen_preview_pages("blog","index")
    return render(request, 'preview_base.html', options)

def projects(request):
    options=gen_preview_pages("projects","projects")
    return render(request, 'preview_base.html', options)

def contact(request):
    options=gen_content_post('contact','content','contact')
    return render(request, 'content_base.html', options)

def post(request,title,root):
    options=gen_content_post(title,request.resolver_match.url_name,root)
    return render(request, 'content_base.html', options)

def gen_content_post(title,page_dir,root):
    """
    gen_content_posts() - Generates html content posts from markdown files in
    provided directory.
    """
    md = markdown.Markdown(extensions=["markdown.extensions.meta"])
    content = md.convert(get_page(os.path.join(page_dir,title + '.md')))
    options = {'title':'Joseph\s Blog',
           'index':'',
           'projects':'',
           'contact':'',
           'year':datetime.datetime.now().year,
           'content_title':md.Meta["content_title"][0],
           'publication_date':md.Meta["publication_date"][0],
           'img_link':md.Meta["img_link"][0],
           'image_subtext':md.Meta["image_subtext"][0],
           'content_text':content,
           }
    options[root] = 'active'
    return options

def gen_preview_pages(page_dir,out_dir):
    """
    gen_preview_pages(page_dir,out_dir)

    Generates template input for preview pages.
    """
    md = markdown.Markdown(extensions=["markdown.extensions.meta"])
    # content_template = jinja_env.get_template(preview_base)
    content_pages = get_page_names(page_dir,ext='.md')
    options = {'title':'Joseph\s Blog',
               'index':'',
               'projects':'',
               'contact':'',
               'year':datetime.datetime.now().year,
               'posts':[]
               }
    options[out_dir] = 'active'
    post_list = []
    for page in content_pages:
        content = md.convert(get_page(os.path.join(page_dir,page)))
        post_details = {'content_title':md.Meta["content_title"][0],
                       'publication_date':md.Meta["publication_date"][0],
                       'img_link':md.Meta["img_link"][0],
                       'image_subtext':md.Meta["image_subtext"][0],
                       'output_link':'{}/{}'.format(page_dir,os.path.splitext(page)[0]),
                       'content_text':content,}
        post_list.append(copy.deepcopy(post_details))
    options['posts'] = sorted(post_list, key=lambda k: k['publication_date'],reverse=True)
    return options

def get_page_names(root,ext):
    """
    get_page_names(root,ext)

    Returns list of files that have extention ext in directory root
    """
    path_to_posts = os.path.join(root,'*'+ ext)
    pages = glob.glob(path_to_posts)
    return [os.path.basename(page) for page in pages]

def get_page(path):
    """
    get_page(path)

    Returns string containing data in file specified by input path.
    """
    return open(path).read()
