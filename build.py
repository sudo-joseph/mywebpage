#!/usr/bin/env python3

__author__ = 'Joseph Reid'

#Constants

def main():
    """
    main() - Main Loop for Static Site Generator.
    """

    INDEX_FORMTATTING = {'title':'Joseph\'s Blog',
                              'index':'active',
                              'projects':'',
                              'contact':'',
                               }

    BLOG_POSTS = [{ 'content_file':'blog/JosephLanes.html',
                    'ouput_file':'docs/JosephLanes.html',
                    'formatting':{'blog_title':'A plan to fix I-80 in Berkeley (for me)',
                                  'publication_date':'2019-11-09',
                                  'img_link':'./img/I-80_Eastshore_Fwy.jpg',
                                  'image_subtext':'An Unending Nightmare...',
                                  'blog_subtitle':'A proposal',
                                  'blog_text':'',
                                   }},
                                   ]

    OTHER_PAGES = [{'filename':'content/index.html',
                'output':'docs/index.html',
                'formatting':{'title':'Joseph\'s Blog',
                              'index':'active',
                              'projects':'',
                              'contact':'',
                               }},
                   {'filename':'content/projects.html',
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

    genBlogPosts(BLOG_POSTS,INDEX_FORMTATTING)
    # genindexPage()
    # genContentPages()

def genBlogPosts(blog_posts,index_formatting):
    """
    genBlogPosts() - Generates blog posts.
    """
    blog_base ='templates/blog_base.html'
    site_base ='templates/base.html'
    blog_base_template = getPage(blog_base)
    site_base_template = getPage(site_base)

    for post in blog_posts:
        formatting = post['formatting']
        formatting['blog_text']=getPage(post['content_file'])
        index_formatting['content']=blog_base_template.format(**formatting)
        open(post['ouput_file'],'w').write(site_base_template.format(**index_formatting))


def genContentPages():
    """
    genContntPages() - Generates other pages.
    """
    base ='templates/base.html'
    template = getPage(base)
    for page in OTHER_PAGES:
        formatting = page['formatting']
        formatting['content'] = open(page['filename']).read()
        open(page['output'],'w').write(template.format(**formatting))


def genIndexPage(blog_posts,index_formatting):
    return #to-do fix broken code here .
    index_blog_entry = 'templates/index_blog_entry_base.html'
    index_blog_post_template = getPage(index_blog_entry)
    blog_post_summaries = ''
    for post in blog_posts:
        blog_post_summaries += index_blog_post_template.format(**formatting)


def getPage(template):
    return open(template).read()



if __name__ == '__main__':
    main()
