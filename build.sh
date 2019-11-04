#!/bin/bash

#build index.html
cat templates/top.html content/index.html templates/bottom.html > docs/index.html
sed -i "s/{title}/Joseph's Blog/g;s/{index}/active/g" docs/index.html


#build projects.html
cat templates/top.html content/projects.html templates/bottom.html > docs/projects.html
sed -i "s/{title}/Joseph's Projects/g;s/{projects}/active/g" docs/projects.html

# #build contact.html
cat templates/top.html content/contact.html templates/bottom.html > docs/contact.html
sed -i "s/{title}/Contact Me/g;s/{contact}/active/g" docs/contact.html
