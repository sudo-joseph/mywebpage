#!/usr/bin/env python3

__author__ = 'Joseph Reid'

import datetime
import string
import glob
import os
import copy
# from jinja2 import Template
import markdown
from jinja2 import Environment, FileSystemLoader
from operator import itemgetter

def main():
    """
    main() - Main Loop for Static Site Generator.
    """
    CONTENT_BASE = 'content_base.html'
    SITE_BASE = 'base.html'
    PREVIEW_BASE = 'preview_base.html'
    JINJA_ENV = Environment(loader=FileSystemLoader('templates'))

    #generate blog posts based on content in blog/
    gen_content_posts("blog","index",CONTENT_BASE,SITE_BASE,JINJA_ENV)
    gen_preview_pages("blog","index",PREVIEW_BASE,JINJA_ENV)

    #generate project posts based on content in project/
    gen_content_posts("projects","projects",CONTENT_BASE,SITE_BASE,JINJA_ENV)
    gen_preview_pages("projects","projects",PREVIEW_BASE,JINJA_ENV)
    #Generate site
    gen_site_pages(SITE_BASE,JINJA_ENV)

def gen_site_pages(site_base,jinja_env):
    """
    gen_site_pages(site_base,jinja_env)

    Generates site pages based on html files in content/ with jinja2 template
    from jinja_env.
    """
    site_template = jinja_env.get_template(site_base)
    site_pages = get_page_names(root="content",ext=".html")

    for page in site_pages:
        options = {'title':'',
                   'year':datetime.datetime.now().year,
                   'project_pages':''}
        options['content'] = get_content(page)
        options[os.path.splitext(page)[0]] = 'active'
        #todo move render call to seperate file
        output_file = site_template.render(**options)
        open(os.path.join("docs",page),'w').write(output_file)

def get_page_names(root,ext):
    """
    get_page_names(root)

    Returns list of html files in directory root.
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

def get_content(page):
    """
    get_page(template)

    Returns string with page content specified by input var.
    """
    return get_page(os.path.join("content",page))

def gen_content_posts(page_dir,out_dir,content_base,site_base,jinja_env):
    """
    gen_content_posts() - Generates html content posts from markdown files in
    provided directory.
    """
    md = markdown.Markdown(extensions=["markdown.extensions.meta"])
    content_template = jinja_env.get_template(content_base)
    content_pages = get_page_names(page_dir,ext='.md')

    for page in content_pages:
        content = md.convert(get_page(os.path.join(page_dir,page)))
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
        options[out_dir] = 'active'
        output_file = content_template.render(**options)
        open(os.path.join("docs",os.path.splitext(page)[0] + '.html')
            ,'w').write(output_file)

def gen_preview_pages(page_dir,out_dir,preview_base,jinja_env):
    md = markdown.Markdown(extensions=["markdown.extensions.meta"])
    content_template = jinja_env.get_template(preview_base)
    content_pages = get_page_names(page_dir,ext='.md')
    options = {'title':'Joseph\s Blog',
               'index':'',
               'projects':'',
               'contact':'',
               'year':datetime.datetime.now().year,
               'posts':[]
               }
    options[out_dir] = 'active'

    for page in content_pages:
        content = md.convert(get_page(os.path.join(page_dir,page)))
        post_details = {'content_title':md.Meta["content_title"][0],
                       'publication_date':md.Meta["publication_date"][0],
                       'img_link':md.Meta["img_link"][0],
                       'image_subtext':md.Meta["image_subtext"][0],
                       'output_link':os.path.splitext(page)[0] + '.html',
                       'content_text':content,}
        options['posts'].append(copy.deepcopy(post_details))
    output_file = content_template.render(**options)
    open(os.path.join("docs",out_dir+".html"),'w').write(output_file)

if __name__ == '__main__':
    main()
