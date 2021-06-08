---
title: "Colophon"
visible: true
permalink: "/colophon/"
nb_migrate: clean 
summary: How this site was made, and a brief history.
---

<div class="accordion">
<h3>What is a colophon?</h3>

<div>

Per [Wikipedia](https://en.wikipedia.org/wiki/Colophon_(publishing)):
> In publishing, a colophon is a brief statement containing information about the publication of a book such as the place of publication, the publisher, and the date of publication.

For websites, it's usually information about the technology used to create the website.
</div>


<h3> Why have a colophon?</h3>
<div>
1. **For the builders who come after**. Digital technology can seem like impenetrable magic, but everything here is the work of human hands. By default, it should be easy for people to learn from the artifacts around them should they wish to make something similar.
1. **For the builders who came before**. This website relies on the work of countless people around the world. I owe them a debt and wish to acknowledge that, in a limited way. It is impossible to thank everyone [^thanks] but one can try.
1. **For our place in the tradition**. The colophon, on printed materials, has a long history. We, as digital media pioneers [^alan-kay], should think deeply about our place in that tradition. It is appropriate that digital colophons have their own standards and norms.

[^alan-kay]: Per Alan Kay, [the real computer revolution hasn't happened yet](https://www.youtube.com/watch?v=aYT2se94eU0)

[^thanks]: Thank you for transistors! For lithium mined from the earth! For language and fire and cloud computing!
</div>
</div>
<br>

## How it's made

This site is built with Jekyll and hosted on Netlify. It uses the minima theme. The code to show revision history on each page is taken from [this post](https://ryanjduffy.github.io/blog/2016/01/08/including-git-history-in-a-jekyll-post.html) by Ryan Duffy, as explained [here]({{site.baseurl}}{% link _posts/2020-10-11-revision-history.md %}). The domain is managed by Google Domains.

I have also lifted a lot from the excellent [argmin gravitas](https://www.gleech.org/).

The website lives in [this repository](https://github.com/louispotok/louispotok-dot-com). It's private as of this writing (May 2021) but I do intend to make it public soon. If you want to look at the source but it's still closed, please let me know and I'll open it up!


## History and migration

Louispotok.com was originally a Wordpress blog, hosted on cPanel, with domain managed by NameCheap. In 2020 I experimented with a Jekyll static site hosted on Github Pages (louispotok.github.io/notebook). This was originally a ["daily notebook"]({% link _posts/2020-06-15-first.md %}) blog, but I continued posting there for a while and stopped updating louispotok.com.

In May 2021 I decided to combine the two sites into a single unified blog. I used Ben Balter's [Wordpress-to-Jekyll exporter](https://github.com/benbalter/wordpress-to-jekyll-exporter). It mostly worked fine, though some formatting was mangled in the transition, and the tool also, bizarrely, [strips out all youtube links](https://github.com/benbalter/wordpress-to-jekyll-exporter/issues/222).

As of today (5/30/2021) there are still some issues with the site due to the migration:
* Inconsistent urls: the wordpress posts have nice `louispotok.com/post-title` urls, while the notebook posts have `louispotok.com/YYYY/MM/DD/post-title.html` urls.
* There were 11 comments on the wordpress site which are now missing. Apologies to Sam, Gideon, Ohad and Matt. Some day I may add commenting on this site and reinstate those comments.
* I have not yet cleaned up the formatting from all the wordpress posts.
* The history on each page is inaccurate, since there are no commits from before the migration/merge.