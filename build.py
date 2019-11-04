#!/usr/bin/env python3

top = open('templates/top.html').read()
bottom = open('templates/bottom.html').read()

index = open('content/index.html').read()
projects = open('content/projects.html').read()
contact = open('content/contact.html').read()

open('docs/index.html','w').write(top + index + bottom)
open('docs/projects.html','w').write(top + projects + bottom)
open('docs/contact.html','w').write(top + contact + bottom)
