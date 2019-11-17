#!/usr/bin/env python3

__author__ = 'Joseph Reid'

import utils
from jinja2 import Environment, FileSystemLoader

def main():
    """
    main() - Main Loop for Static Site Generator.
    """
    CONTENT_BASE = 'content_base.html'
    SITE_BASE = 'base.html'
    PREVIEW_BASE = 'preview_base.html'
    JINJA_ENV = Environment(loader=FileSystemLoader('templates'))

    #generate blog posts based on content in blog/
    utils.gen_content_posts("blog","index",CONTENT_BASE,SITE_BASE,JINJA_ENV)
    utils.gen_preview_pages("blog","index",PREVIEW_BASE,JINJA_ENV)

    #generate project posts based on content in project/
    utils.gen_content_posts("projects","projects",CONTENT_BASE,SITE_BASE,JINJA_ENV)
    utils.gen_preview_pages("projects","projects",PREVIEW_BASE,JINJA_ENV)
    #Generate site
    utils.gen_site_pages(SITE_BASE,JINJA_ENV)

if __name__ == '__main__':
    main()
