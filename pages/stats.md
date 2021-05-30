---
layout: page
permalink: "/stats/"
title: Stats
visible: true
summary: Basic website stats. Right now, just a count of posts by year.
---

The amount I write has varied a lot over the years! Post count:
{% assign counter = 0 -%}
{% for post in site.posts -%}
  {% assign thisyear = post.date | date: "%Y" -%}
  {% assign prevyear = post.previous.date | date: "%Y" -%}
  {% assign counter = counter | plus: 1 -%}
  {% if thisyear != prevyear -%}
[{{thisyear}} ({{counter}})](/{{thisyear}}) : {% for i in (1..counter) %}\*{%- endfor -%}
    {%- assign counter = 0 -%}
  {% endif %}
{% endfor %}
