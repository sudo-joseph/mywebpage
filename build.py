#!/usr/bin/env python3

__author__ = 'Joseph Reid'

import datetime
import string

def main():
    """
    main() - Main Loop for Static Site Generator.
    """
    BLOG_POSTS = [{ 'content_file':'blog/thanksgiving.html',
                    'ouput_file':'docs/thanksgiving.html',
                    'formatting':{'blog_title':'Thanksgiving Can\'t Come Soon Enough',
                                  'publication_date':'2019-11-09',
                                  'img_link':'./img/thanksgiving.jpg',
                                  'image_subtext':'The longest two weeks of the year...',
                                  'blog_text':'',
                                  'output_link':'./thanksgiving.html',
                                   }},
                   { 'content_file':'blog/JosephLanes.html',
                    'ouput_file':'docs/JosephLanes.html',
                    'formatting':{'blog_title':'A plan to fix I-80 in Berkeley (for me)',
                                  'publication_date':'2019-11-01',
                                  'img_link':'./img/I-80_Eastshore_Fwy.jpg',
                                  'image_subtext':'An Unending Nightmare...',
                                  'blog_text':'',
                                  'output_link':'./JosephLanes.html',
                                   }},
                   {   'content_file':'blog/caExplore.html',
                       'ouput_file':'docs/caExplore.html',
                       'formatting':{'blog_title':'Exploring the California Coast',
                                 'publication_date':'2019-10-27',
                                 'img_link':'./img/chimneyrock.jpg',
                                 'image_subtext':'This might be my favorite place in the bay.',
                                 'blog_text':'',
                                 'output_link':'./caExplore.html',
                                  }},
                   { 'content_file':'blog/startingKickstart.html',
                     'ouput_file':'docs/startingKickstart.html',
                     'formatting':{'blog_title':'Starting a Coding Bootcamp',
                                 'publication_date':'2019-10-01',
                                 'img_link':'https://i.giphy.com/media/o0vwzuFwCGAFO/giphy.webp',
                                 'image_subtext':'An Unending Nightmare...',
                                 'blog_subtitle':'A proposal',
                                 'blog_text':'',
                                 'output_link':'./startingKickstart.html',
                                  }},
                                   ]

    OTHER_PAGES = [{'filename':'content/projects.html',
                   'output':'docs/projects.html',
                   'formatting':{'title':'Joseph\'s Projects',
                                 'index':'',
                                 'projects':'active',
                                 'contact':'',
                                  }},
                  {'filename':'content/contact.html',
                  'output':'docs/contact.html',
                  'formatting':{'title':'Contact Me',
                                'index':'',
                                'projects':'',
                                'contact':'active',
                             }}]

    INDEX_PAGE = 'docs/index.html'
    INDEX_FORMATTING = {'title':'Joseph\'s Blog',
                              'index':'active',
                              'projects':'',
                              'contact':'',
                               }

    BLOG_BASE ='templates/blog_base.html'
    SITE_BASE ='templates/base.html'
    BLOG_PREVIEW_BASE='templates/index_blog_preview_base.html'
    INDEX_BASE = 'templates/index_base.html'

    genBlogPosts(BLOG_POSTS,INDEX_FORMATTING,BLOG_BASE,SITE_BASE)
    genIndexPage(BLOG_POSTS,INDEX_PAGE,INDEX_FORMATTING,SITE_BASE,BLOG_PREVIEW_BASE,INDEX_BASE)
    genContentPages(SITE_BASE,OTHER_PAGES)
    # addCopyRight()

def genBlogPosts(blog_posts,index_formatting,blog_base,site_base):
    """
    genBlogPosts() - Generates blog posts based on template and content files in blog/
    """
    blog_base_template = getPage(blog_base)
    site_base_template = getPage(site_base)
    for post in blog_posts:
        formatting = post['formatting']
        formatting['blog_text']=getPage(post['content_file'])
        index_formatting['content']=blog_base_template.format(**formatting)
        open(post['ouput_file'],'w').write(site_base_template.format(**index_formatting))

def genIndexPage(blog_posts,index_page,index_formatting,site_base,blog_preview_base,index_base):
    """
    genIndexPage(blog_posts,index_formatting,blog_base,site_base)

    Generates blog post preview elements on site landing page.
    """

    index_blog_preview_template = getPage(blog_preview_base)
    blog_post_previews = ''
    for post in blog_posts:
        formatting = post['formatting']
        blog_content = getPage(post['content_file'])
        first_par = ''.join(blog_content.split('</p>')[:2]) + '</p>'
        formatting['blog_text']=first_par #need to truncate blog text better
        blog_post_previews += index_blog_preview_template.format(**formatting)
    site_template = getPage(site_base)
    index_template = getPage(index_base)
    index_formatting['content'] = index_template.format(blog_posts=blog_post_previews)
    open(index_page,'w').write(site_template.format(**index_formatting))

def genContentPages(site_base,other_pages):
    """
    genContntPages() - Generates other pages.
    """
    template = getPage(site_base)
    for page in other_pages:
        formatting = page['formatting']
        formatting['content'] = open(page['filename']).read()
        open(page['output'],'w').write(template.format(**formatting))


def getPage(template):
    return open(template).read()

# def addCopyRight(index_page,blog_posts,other_pages):
#     year = datetime.datetime.now().year
#     blogpages = [page['ouput_file'] for page in blog_posts]
#
#     other_pages =
#
#     pages = index_page +


if __name__ == '__main__':
    main()
