#!/usr/bin/env python3

#Open all tempalte files.
top = open('templates/top.html').read()
bottom = open('templates/bottom.html').read()

#Open all content files.
index = open('content/index.html').read()
projects = open('content/projects.html').read()
contact = open('content/contact.html').read()

## export compiled files with page specific string formatting.

open('docs/index.html','w').write(top.format(
        title='Joseph\'s Blog',
        index='active',
        projects='',
        contact='')
         + index + bottom)
open('docs/projects.html','w').write(top.format(
        title='Joseph\'s Projects',
        index='',
        projects='active',
        contact='')
         + projects + bottom)
open('docs/contact.html','w').write(top.format(
        title='Contact Me',
        index='',
        projects='',
        contact='active')
         + contact + bottom)
