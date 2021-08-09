---
title: About
layout: page
permalink: "/about/"
id: 2
guid: http://louispotok.com/?p=2
header: true
visible: true
summary: Basic overview of who I am and what this site is all about.
---
I'm Louis. This website is mostly a [blog]({{site.baseurl}}{% link pages/blog.md %}). Some basic stats about the blog are available on [the stats page]({% link pages/stats.md %}).

You can reach me by [email](mailto:{{site.email}}) or follow me on [Twitter](https://twitter.com/louispotok) (DMs open!). I love getting messages from friendly strangers, so don't be shy. Feel free to:
* Tell me if you had a strong reaction, positive or negative, to something I wrote.
* Ask me a favor -- I'll gladly help if I can.
* Tell me what you're working on and why you're passionate about it.
* Ask for advice.
* Send or request reading suggestions.

Sometimes it's nice to chat in real time too. If you like what's here we'd probably enjoy talking, so go ahead and [book some time](https://calendly.com/louispotok/30-minute-meeting) on my calendar -- even (especially!) if we're strangers.

<div class="accordion"> 
<h3>Bugs?</h3>
<p>
If you spot typos, broken links, etc, please let me know! In particular, some of the content is [migrated]({% link pages/colophon.md %}#history-and-migration) from an older Wordpress version of this blog, so older posts may have formatting errors or worse.
</p>
</div>

<div class="accordion"> 
  <h3>Disclosure
  </h3>
  <p>Some of the links on my site are through Amazon's Affiliates Program. If you make a purchase on Amazon through a link on this site, I receive a small commission. (The book does not cost you any extra.) I set this up in 2013 because I thought it would be cool, but I've made about $15 lifetime from the program.
  </p>
</div>

<br>

Some pages on this site:

{% for page in site.pages %}
{% if page.visible == true %}
<h4>[{{page.title}}]({{page.url}})</h4>
<p style="margin-left:20px"><em>{{page.summary}}</em></p>
{% endif %}
{% endfor %}
