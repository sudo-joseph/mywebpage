#!/bin/bash

#build index.html
cat templates/top.html content/index.html templates/bottom.html > index.html
sed '/<li class="nav-item home">/ c\          <li class="nav-item home active">' index.html > temp.html
sed '/<a class="nav-link" href="index.html">Home<\/a>/ c\         <a class="nav-link active" href="index.html">Home</a>' temp.html > index.html

#build projects.html

cat templates/top.html content/projects.html templates/bottom.html > projects.html
sed '/<li class="nav-item projects">/ c\          <li class="nav-item projects active">' projects.html > temp.html
sed '/<a class="nav-link" href="projects.html">Projects<\/a>/ c\         <a class="nav-link active" href="projects.html">Projects</a>' temp.html > projects.html

#build contact.html

cat templates/top.html content/contact.html templates/bottom.html > contact.html
sed '/<li class="nav-item contact">/ c\          <li class="nav-item contact active">' contact.html > temp.html
sed '/<a class="nav-link" href="contact.html">Contact Me<\/a>/ c\         <a class="nav-link active" href="contact.html">Contact Me</a>' temp.html > contact.html

rm temp.html
