---
title: "Colophon"
visible: true
permalink: "/colophon/"
nb_migrate: clean 
summary: How this site was made, and a brief history.
---

## What is a colophon?

Per [Wikipedia](https://en.wikipedia.org/wiki/Colophon_(publishing)):
> In publishing, a colophon is a brief statement containing information about the publication of a book such as the place of publication, the publisher, and the date of publication.

For websites, it's usually information about the technology used to create the website.

## Why have a colophon?
1. **For the builders who come after**. Digital technology can seem like impenetrable magic, but everything here is the work of human hands. By default, it should be easy for people to learn from the artifacts around them should they wish to make something similar. It is hard to overstate the importance of "view source."
1. **For the builders who came before**. This website relies on the work of countless people around the world. I owe them a debt and wish to acknowledge that, in a limited way. It is impossible to thank everyone [^thanks] but one can try.
1. **For our place in the tradition**. The colophon, on printed materials, has a long history. We, as digital media pioneers [^alan-kay], should think deeply about our place in that tradition. It is appropriate that digital colophons have their own standards and norms.

[^alan-kay]: Per Alan Kay, [the real computer revolution hasn't happened yet](https://www.youtube.com/watch?v=aYT2se94eU0)

[^thanks]: Thank you for transistors! For lithium mined from the earth! For language and fire and cloud computing!

## How it's made

* This site is built with Jekyll and hosted on Netlify. It uses the minima theme.
* The domain is managed by Google Domains.
* The code to show revision history on each page is taken from [this post](https://ryanjduffy.github.io/blog/2016/01/08/including-git-history-in-a-jekyll-post.html) by Ryan Duffy, as explained [here]({{site.baseurl}}{% link _posts/2020-10-11-revision-history.md %}).
* Basic analytics are collected on a self-hosted ~Matomo~ Goatcounter instance and are not shared with any third party.
* The website lives in [this repository](https://github.com/louispotok/louispotok-dot-com).
* Many small technical decisions are lifted or inspired from the excellent [argmin gravitas](https://www.gleech.org/).

If you want to talk about any of the decisions I made, or are looking for help doing something similar, I'm happy to help.

## History and migration

Louispotok.com was originally a Wordpress blog, hosted on cPanel, with domain managed by NameCheap. In 2020 I experimented with a Jekyll static site hosted on Github Pages (louispotok.github.io/notebook). This was originally a ["daily notebook"]({% link _posts/2020-06-15-first.md %}) blog, but I continued posting there for a while and stopped updating louispotok.com.

In May 2021 I decided to combine the two sites into a single unified blog. I used Ben Balter's [Wordpress-to-Jekyll exporter](https://github.com/benbalter/wordpress-to-jekyll-exporter). It mostly worked fine, though some formatting was mangled in the transition, and the tool also, bizarrely, [strips out all youtube links](https://github.com/benbalter/wordpress-to-jekyll-exporter/issues/222).

As of today (6/26/2021) there are still some issues with the site due to the migration:
* Inconsistent urls: the wordpress posts have nice `louispotok.com/post-title` urls, while the notebook posts have `louispotok.com/YYYY/MM/DD/post-title.html` urls.
* I have not yet cleaned up the formatting from all the wordpress posts.
* The history on each page is inaccurate, since there are no commits from before the migration/merge.

## Why "Capillary Action"?

I named this blog in 2013 without giving it much thought. In 2021 I thought about it, and realized I liked it.

Capillary action is the process by which a liquid diffuses through a series of small tubes ("capillaries"), moving as though of its own accord and often against gravity.

In your body, it's how blood gets from veins and arteries through the much smaller capillaries into your cells. If you've ever dipped the corner of a paper towel into some coffee, you can see it at work as well.

**Ideas too seem to spread of their own volition through innumerable tiny channels until they suffuse the whole medium.**

There was also [a band with the same name](https://en.wikipedia.org/wiki/Capillary_Action_(band)), but I am not affiliated with them.
