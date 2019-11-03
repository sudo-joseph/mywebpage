#!/bin/bash

#build index.html
cat templates/top.html content/index.html templates/bottom.html > index.html

#build projects.html
cat templates/top.html content/projects.html templates/contact.html > projects.html

#build contact.html
cat templates/top.html content/contact.html templates/contact.html > contact.html
