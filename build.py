#!/usr/bin/env python3

def main():
    content = genContent()
    template='templates/base.html'
    base = getBase(template)
    for page in content:
        formatting = page['formatting']
        formatting['content'] = open(page['filename']).read()
        open(page['output'],'w').write(base.format(**formatting))

def genContent():
    return [{'filename':'content/index.html',
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

def getBase(template):
    return open(template).read()





if __name__ == '__main__':
    main()
