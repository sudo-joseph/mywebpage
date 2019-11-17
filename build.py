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

def main():
    """
    main() - Main Loop for Static Site Generator.
    """
    CONTENT_BASE = 'content_base.html'
    SITE_BASE = 'base.html'
    JINJA_ENV = Environment(loader=FileSystemLoader('templates'))

    #generate blog posts based on content in blog/
    gen_content_posts("blog",CONTENT_BASE,SITE_BASE,JINJA_ENV)
    # gen_index_page()

    #generate project posts based on content in project/
    gen_content_posts("projects",CONTENT_BASE,SITE_BASE,JINJA_ENV)
    # gen_project_page()

    #Generate site
    gen_site_pages(SITE_BASE,JINJA_ENV)

def gen_site_pages(site_base,jinja_env):
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

def gen_content_posts(page_dir,content_base,site_base,jinja_env):
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
                   'index':'active',
                   'projects':'',
                   'contact':'',
                   'content':'',
                   'year':datetime.datetime.now().year,
                   'content_title':md.Meta["content_title"][0],
                   'publication_date':md.Meta["publication_date"][0],
                   'img_link':md.Meta["img_link"][0],
                   'image_subtext':md.Meta["image_subtext"][0],
                   'content_text':content,
                   }
        #todo move render call to seperate file
        output_file = content_template.render(**options)
        open(os.path.join("docs",os.path.splitext(page)[0] + '.html')
                ,'w').write(output_file)

# def gen_index_page(blog_posts,index_page,index_formatting,site_base,blog_preview_base,index_base):
#     """
#     gen_index_page(blog_posts,index_formatting,blog_base,site_base)
#
#     Generates blog post preview elements on site landing page.
#     """
#
#     index_blog_preview_template = get_page(blog_preview_base)
#     blog_post_previews = ''
#     for post in blog_posts:
#         formatting = post['formatting']
#         blog_content = get_page(post['content_file'])
#         first_par = ''.join(blog_content.split('</p>')[:2]) + '</p>'
#         formatting['blog_text']=first_par #need to truncate blog text better
#         blog_post_previews += index_blog_preview_template.format(**formatting)
#     site_template = get_page(site_base)
#     index_template = get_page(index_base)
#     index_formatting['content'] = index_template.format(blog_posts=blog_post_previews)
#     open(index_page,'w').write(site_template.format(**index_formatting))
#
# def gen_blog_post_list():
#     blog_dict = {'content_file':'',
#                     'ouput_file':'',
#                     'formatting':{'blog_title':'',
#                                   'publication_date':'',
#                                   'img_link':'',
#                                   'image_subtext':'',
#                                   'blog_text':'',
#                                   'output_link':'',
#                                    }}
#     blog_pages = glob.glob("blog/*.html")
#     output = []    #todo better formatting for page details
#
#     print(blog_pages)
#     for page in blog_pages:
#         page_base = os.path.basename(page)
#         blog_dict['content_file'] = os.path.join("blog",page_base)
#         blog_dict['ouput_file'] = os.path.join("docs",page_base)
#         blog_dict['formatting']["blog_title"] = page_base.split('.')[0]
#         output.append(copy.deepcopy(blog_dict))
#     print(output)
#     return output

if __name__ == '__main__':
    main()
