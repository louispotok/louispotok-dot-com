---
title: About
layout: page
permalink: "/about/"
id: 2
guid: http://louispotok.com/?p=2
header: true
---
I'm Louis. This site is mostly a [blog]({{site.baseurl}}{% link pages/blog.md %}). Some basic stats about the blog are available on [the stats page]({% link pages/stats.md %}).

You can reach me on [Twitter](https://twitter.com/louispotok) (DMs open!) or by [email](mailto:{{site.email}}).

<div class="accordion"> 
<h3>Bugs?</h3>
<p>
If you spot typos, broken links, etc, please let me know! In particular, some of the content is [migrated]({% link pages/colophon.md %}#history-and-migration) from an older Wordpress version of this blog, so older posts in particular may have formatting errors, etc.
</p>
</div>

<div class="accordion"> 
  <h3>Disclosure
  </h3>
  <p>Some of the links on my site are through Amazon's Affiliates Program. If you make a purchase on Amazon through a link on this site, I receive a small commission. (The book does not cost you any extra.) I set this up in 2013 because I thought it would be cool, but I've made about $15 lifetime from the program.
  </p>
</div>

<br>

Some other pages on this site:

{% for page in site.pages %}
{% if page.visible == true %}
* [{{page.title}}]({{page.url}})
{% endif %}
{% endfor %}
