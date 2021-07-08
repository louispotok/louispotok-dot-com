---
---
Blogs that I like:

I should move this to `_data`, I think. 
What fields do I want? Tags? Summary? Do I really want to do this on my Thursday morning?

<ul>
{% for blog in site.data.blogroll %}
<li>
<a href="{{blog.url}}">{{blog.name}}</a>
</li>
{% endfor %}
</ul>

--- 
* ben kuhn
* gavin leech
* gwern
* SSC
* dorian taylor
* bret victor
* JP
* geoffrey litt
* linus / the sephist
* Marginal revolution
* hacker news
* andrew gelman
* interconnected / matt webb
* david maciver
* hillel wayne
* robin sloan
* banana
* tom critchlow
* jsomers
* adam elkus
* kyle chayka

