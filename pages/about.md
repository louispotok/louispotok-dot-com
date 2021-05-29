---
title: About
layout: page
permalink: "/about/"
id: 2
guid: http://louispotok.com/?p=2
header: true
---
I'm Louis. This site is mostly a [blog]({{site.baseurl}}{% link pages/blog.md %}).

You can reach me on [Twitter](twitter.com/louispotok) (DMs open!) or by [email](mailto:{{site.email}}).

<div class="accordion"> 
<h3>Disclosure</h3>
<p>Some of the links on my site are through Amazon's Affiliates Program. If you make a purchase on Amazon through a link on this site, I receive a small commission. (The book does not cost you any extra.) I set this up in 2013 because I thought it would be cool, but I've made about $12 lifetime from the program.
</p>
</div>
<br>
<div>
<p>Some other pages on this site:
<ul>
{% for page in site.pages %}
  {%- if page.visible == true -%}
   <li><a href="{{site.baseurl}}{{ page.url }}">{{ page.title }}</a></li>
 {%- endif -%}
{% endfor %}
</ul>
</p>
</div>
