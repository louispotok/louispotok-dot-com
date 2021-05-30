---
title: "Colophon"
visible: true
permalink: "/colophon/"
nb_migrate: dirty
---

## How it's made

This site is built with Jekyll and hosted on Netlify. It uses the minima theme. The code to show revision history on each page is taken from [this post](https://ryanjduffy.github.io/blog/2016/01/08/including-git-history-in-a-jekyll-post.html) by Ryan Duffy, as explained [here]({{site.baseurl}}{% link _posts/2020-10-11-revision-history.md %}). The domain is managed by Google Domains.

I have also lifted a lot from the excellent [argmin gravitas](https://www.gleech.org/).

The website lives in [this repository](https://github.com/louispotok/louispotok-dot-com).

## History and migration

Louispotok.com was originally a Wordpress blog, hosted on cPanel, with domain managed by NameCheap. In 2020 I experimented with a Jekyll static site hosted on Github Pages (louispotok.github.io/notebook). This was originally a ["daily notebook"]({% link _posts/2020-06-15-first.md %}) blog, but I continued posting there for a while and stopped updating louispotok.com.

In May 2021 I decided to combine the two sites into a single unified blog. I used Ben Balter's [Wordpress-to-Jekyll exporter](https://github.com/benbalter/wordpress-to-jekyll-exporter). It mostly worked fine, though some formatting was mangled in the transition, and the tool also, bizarrely, [strips out all youtube links](https://github.com/benbalter/wordpress-to-jekyll-exporter/issues/222).

As of today (5/30/2021) there are still some issues with the site due to the migration:
* Inconsistent urls: the wordpress posts have nice `louispotok.com/post-title` urls, while the notebook posts have `louispotok.com/YYYY/MM/DD/post-title.html` urls.
* There were 11 comments on the wordpress site which are now missing. Apologies to Sam, Gideon, Ohad and Matt. Some day I may add commenting on this site and reinstate those comments.
* I have not yet cleaned up the formatting from all the wordpress posts.

