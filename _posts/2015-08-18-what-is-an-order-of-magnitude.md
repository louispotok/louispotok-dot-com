---
id: 386
title: What is an order of magnitude?
date: 2015-08-18T11:17:32-07:00
author: Louis Potok
layout: post
guid: http://louispotok.com/?p=386
permalink: /what-is-an-order-of-magnitude/
categories:
  - Uncategorized
---
I&#8217;ve always wondered exactly how to define an order of magnitude. At [ideas42](http://www.ideas42.org) I had a particular colleague with a PhD in Econ; one time I mentioned that I think use it in a &#8220;fuzzy&#8221; way, and he responded that he always uses it in an exact way.

So what is the exact way? I think there are actually two ways to use the phrase. Is it a property or is it only a relation?

  1. Property: _every number has an order of magnitude that is equivalent to its power of ten_ (so the OOM of 153 is 2 because 153 = 1.53 * 10^2). This implies a relation: two numbers have the same order of magnitude if each of them has the same order of magnitude, and you calculate the difference in their OOMs by subtracting one from the other.
  2. Relation: two numbers x and y, with x < y, differ by N orders of magnitude if  
    > (x \* 10^N) < y < ( x\* 10^(N-1) )

Notice that these two definitions have different &#8220;predictions&#8221;! Example: is 153 an order of magnitude more than 53? Definition (1) would say yes, but Definition (2) would say no.

The [Wikipedia page](https://en.wikipedia.org/w/index.php?title=Order_of_magnitude&oldid=657710213) actually uses both definitions without trying to explain the contradiction &#8212; the first sentence is a statement of definition (1) but the John Baez quote is definition (2).

The general principle is that objective-sounding, mathematical terms get used for rhetoric even when they are loosely defined; dig deep and nothing is as precise as it seems.

How do you use the phrase?