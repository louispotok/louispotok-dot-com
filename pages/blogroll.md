---
---
Blogs that I like:

I should move this to `_data`, I think. 
What fields do I want? Tags? Summary? Do I really want to do this on my Thursday morning?

Also, something like:
If you like what I'm up to you should check out my friends. These are people with an active and ongoing presence.

<ul>
{% for blog in site.data.blogroll %}
<li>
<a href="{{blog.url}}">{{blog.name}}</a>
</li>
{% endfor %}
</ul>

