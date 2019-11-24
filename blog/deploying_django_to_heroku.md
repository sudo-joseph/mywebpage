content_title: Deploying Django to Heroku
publication_date: 2019-11-24
img_link: img/django.png
image_subtext:Learning a new web framework can be challenging.

This week I have been rebuilding my website to utilize django to dynamically render my site and then have deployed to Heroku. This has been quite the learning experience as I have had to learn both how to build a site with django while also getting it to be compatible with Heroku.

My largest challenge with this project has been learning how to manage static assets in django correctly. It turns out that we need to specify different assets for dev and production. Trying to serve these from a single location did not work when deploying my site to heroku resulting a jumbled mess of a website without any styling or images. To fix this, I had to specify a STATICFILES_DIRS directory in my settings configuration that was different than my STATIC_ROOT directory. Once I made this change, everything was working correctly.

The next challenge was figuring out how to deploy my django branch to heroku instead of master, as my master branch still contains my static site generator from previous homework. To do this, I had to specify to git which branch to merge into upstream master with the following command: <em>git push heroku django:master</em>. With this approach, I could keep my master branch intact until ready to merge the django branch while still deploying my django site to Heroku.

All in all, this has been an interesting project. While clearly there is a ton of depth here that we have not touched on, it is amazing to me how these tools allow me quickly spin up a dynamic webserver for any project.
