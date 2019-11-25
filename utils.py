#!/usr/bin/env python3
__author__ = 'Joseph Reid'

import datetime
import glob
import os
import copy
import markdown
from jinja2 import Environment, FileSystemLoader
import string
import sys
import requests

## main() & helper() for creating new site pages.

def main():
    """
    main() - Main Loop for utils.py.
    """
    if sys.argv[1] == "new":
        if len(sys.argv) == 3:
            if sys.argv[2] == 'blog':
                print("Generating new blog post")
                gen_new_post("blog")
                print("Page Generated")
            elif sys.argv[2] == 'project':
                print("Generating new project post")
                gen_new_post("projects")
                print("Page Generated")
            else:
                print("Unknown Page Type")
                helper()
        else:
            print("Generating new blog post")
            gen_new_post("blog")
            print("Page Generated")
    else:
        print("Please specify ’’new’ to generate new page")

def helper():
    """
    helper()

    Prints help message explaining correct utils.py usage.
    """
    help_msg = """
        Usage:
            Rebuild site: python3 manage.py build

            Create new page: python3 utils.py new {type}
                {type} - optional argument for page type (blog or projects),
                defaults to blog.

        """
    print(help_msg)

##Functions below used for generate template content in manage.py

def gen_content_post(title,page_dir,root):
    """
    gen_content_posts() - Generates template content from markdown files in
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

    Generates template input for preview pages by looping over all md files in input dir.
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

def gen_new_post(page_dir="blog",template='page_markup_base.md'):
    """
    gen_new_post - create new page from template

    Creates a new page in directory specified based on template with jinja.
    """
    jinja_env = Environment(loader=FileSystemLoader("templates"))
    new_page_template = jinja_env.get_template(template)
    title = input("Enter page title: ")
    options = {'title': title,
               'publication_date':datetime.datetime.now().strftime('%Y-%m-%d'),
               }

    output_file = new_page_template.render(**options)
    path_name = os.path.join(page_dir,clean_title(title)+'.md')
    open(path_name,'w').write(output_file)

def clean_title(title):
    """
    clean_title(title)

    Returns inputed title in lower_snake_case with no punctuation.
    """
    title = title.lower()
    title = title.split()
    title = [''.join(filter(str.isalnum, word)) for word in title]
    title = '_'.join(title)
    return(title)

def github_api(request):
    response = requests.get('https://api.github.com/users/sudo-joseph/repos')
    repos = response.json()
    import pprint
    pprint.pprint(repos[1])
    options = {'title':'Joseph\s Blog',
               'index':'',
               'projects':'active',
               'contact':'',
               'year':datetime.datetime.now().year,
               'repos':[]
               }
    repo_list = []

    for repo in repos:
        if repo['fork']==False:
            post_details = {'content_title':repo['name'],
                           'last_updated':repo['updated_at'],
                           'output_link':repo['svn_url'],
                           'content_text':repo['description'],
                           'language':repo['language'],
                           }
            if repo['license']:
                post_details['licence'] = repo['licence']['name']
            repo_list.append(copy.deepcopy(post_details))
    options['repos'] = sorted(repo_list, key=lambda k: k['last_updated'],reverse=True)
    return options

if __name__ == "__main__" and len(sys.argv)>1:
    main()
