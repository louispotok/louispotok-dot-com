---
id: 386
title: What is an order of magnitude?
date: 2015-08-18 11:17:32.000000000 -07:00
layout: post
guid: http://louispotok.com/?p=386
permalink: "/what-is-an-order-of-magnitude/"
categories:
- Uncategorized
wp_migrate: dirty
mathjax: true
---
I've always wondered exactly how to define an order of magnitude. At [ideas42](http://www.ideas42.org) I had a particular colleague with a PhD in Econ; one time I mentioned that I think use it in a "fuzzy" way, and he responded that he always uses it in an exact way.

So what is the exact way? I think there are actually two ways to use the phrase. 

1. As a **unary operation**, a property of a single number. 
* Every number $$x$$ has an order of magnitude $$m_x$$, an integer, such that when $$x$$ is expressed in scientific notation, $$x = x_0 * 10^{m_x}$$. For $$m_x$$ to be unique we have to restrict $$1<={x_0}<10$$.  
* So, for example, $$m_{101} = 2$$ because $$101 = 1.01 * 10^2$$. But $$m_{99} = 1$$ because $$99 = 9.9 * 10^1$$. So $$99$$ and $$101$$ are an order of magnitude apart.
* In fact this defines an equivalence relation on the reals where two numbers are equivalent if they have the same order of magnitude.
1. But you can also define it only as a **binary operation** between two numbers.
* Suppose $$x<=y$$. Then you can say that $$x$$ and $$y$$ differ by $$M_{x,y}$$ orders of magnitude where $$M_{x,y}$$ such that $$(x * 10^{M_{x,y}}) <= y < ( x * 10^{M_{x,y}+1} )$$.
* This defines a relation as well, where $$xRy \iff M_{x,y} = 0$$. But this is not transitive and therefore not an equivalence relation. To see this, note that under this definition $$1 \sim 9$$ and $$9 \sim 14$$ but 1 and 14 differ by 1 order of magnitude.

Notice that these two definitions can differ. Example: is 153 an order of magnitude more than 53? Definition (1) would say yes, but Definition (2) would say no.

The [Wikipedia page](https://en.wikipedia.org/w/index.php?title=Order_of_magnitude&oldid=657710213) actually uses both definitions without trying to explain the contradiction. First, it gives our definition (1): 

> **Orders of magnitude** are written in [powers of 10](https://en.wikipedia.org/wiki/Powers_of_10). For example, the order of magnitude of 1500 is 3, since 1500 may be written as 1.5 × 10^3.

Then it quotes John Baez using our definition (2):
> > We say two numbers have the same order of magnitude of a number if the big one divided by the little one is less than 10. For example, 23 and 82 have the same order of magnitude, but 23 and 820 do not."[\[2\]](https://en.wikipedia.org/w/index.php?title=Order_of_magnitude&oldid=657710213#cite_note-2) — [John C. Baez](https://en.wikipedia.org/wiki/John_C._Baez "John C. Baez")

Source: [Order of magnitude - Wikipedia](https://en.wikipedia.org/wiki/Order_of_magnitude)

The general principle is that objective-sounding, mathematical terms get used for rhetoric even when they are loosely defined; dig deep and precision is often in short supply. 

How do you use the phrase?
