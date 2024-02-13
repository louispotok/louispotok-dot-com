---
title: NAEB
layout: page
permalink: /naeb/
visible: true
summary: Unauthorized mirror of the Native American Ethnobotany Database.
---

**tldr**: I host an [unauthorized mirror](https://naeb.louispotok.com) of the Native American Ethnobotany Database, which contains 45000 different uses of 4000 plants by 300 Native American tribes.

## Ethnobotany is cool

Plants are a fundamental building block of all human societies. Almost everything we eat either is a plant, or eats plants [^fungi]. Plants also synthesize an incredibly broad range of chemicals and can be used in an enormous number of ways: medicine, materials of all kinds, and for broader cultural purposes.

[^fungi]: I see you, fungi fans.

However, these uses are not always obvious. It can take experimentation and learning on timelines beyond a single human life to uncover the secrets of a particular plant, particularly when a complicated set of processing steps is required:

> In the Americas, where manioc was first domesticated, societies who have relied on bitter varieties for thousands of years show no evidence of chronic cyanide poisoning. In the Colombian Amazon, for example, indigenous Tukanoans use a multistep, multiday processing technique that involves scraping, grating, and finally washing the roots in order to separate the fiber, starch, and liquid. Once separated, the liquid is boiled into a beverage, but the fiber and starch must then sit for two more days, when they can then be baked and eaten.

-- Joseph Henrich, The Secret of Our Success, as [quoted by Scott Alexander](https://slatestarcodex.com/2019/06/04/book-review-the-secret-of-our-success/).

Native American peoples uncovered thousands of such uses, and once lost these are not trivial for Western science to rediscover. It is a tragedy that these cultures were destroyed and so much of their knowledge lost, but some of it was recorded by anthropologists. 

## The Native American Ethnobotany Project

Starting in the 1970's, Daniel Moerman and collaborators began compiling these records, and ended up creating a database with information from 206 distinct sources. The project was funded by the National Endowment for the Humanities, the National Science Foundation, and the University of Michigan-Dearborn. This database is **magnificent**.

Professor Moerman publishes a web version of the database [here](http://naeb.brit.org/), a great start for others to build on. However, it does not provide full download or unlimited query access.

So I scraped the NAEB database and [published it](https://naeb.louispotok.com/) using the wonderful [Datasette](https://datasette.io/) tool.

## Why I did this

This data should be open. It was publicly funded years ago, it belongs to the people, and it represents too much human labor to risk its disappearance.

My first full-time job out of college was at the Center for Population Economics, led by Economics Nobel Laureate Bob Fogel. Fogel was at the time in his 90's, and the CPE had been around for decades, performing distinctive research in economic history. [^heros] The dataset they gathered was unique and highly valuable: longitudinal health and economic records for every soldier who fought in the Union Army, the earliest such dataset in existence. Union Army veterans were eligible for pensions, but were required to appear before a board of doctors every few years in order to assess their physical condition and set the appropriate amount of their pension. We tracked these men across their life cycle, as they changed jobs, moved across the country, married and had children, got sick, and eventually died. We were able to link those records to census data, to block-level disease reporting in American cities, to the introduction of sewers and roads. 

[^heros]: Example: [Heros and Cowards](https://www.nber.org/books-and-chapters/heroes-and-cowards-social-face-war) by Costa and Kahn.

I left in 2012 and Fogel died in June 2013. The Wayback Machine's [last snapshot](https://web.archive.org/web/20140116023258/http://www.cpe.uchicago.edu/) of the CPE homepage is dated January 16, 2014. Where did the data go? Was it gone forever? Buried on a few hard drives, as a few researchers finished their papers and then forgot about it? Several times throughout the intervening years I went looking for any trace of this data, to no avail. The NBER [hosts it now](https://www.nber.org/programs-projects/projects-and-centers/Early%20Indicators%20of%20Later%20Work%20Levels,%20Disease%20and%20Death) in some form, although it looks like this page only went up in early 2022. [^caveat]

[^caveat]: As measured by [the first Wayback Machine capture](https://web.archive.org/web/20220000000000*/https://www.nber.org/programs-projects/projects-and-centers/Early%20Indicators%20of%20Later%20Work%20Levels%2C%20Disease%20and%20Death), admittedly imperfect.

It was inconcievable to me that all this work was gone, that the data needed to check and build on dozens of papers and books was no longer available to the wider world. Fogel won a Nobel for this work! And the underlying observations were allowed to disappear?

## Email me!

I hope you find [the database](https://naeb.louispotok.com) interesting and useful. I would love to hear from you about how you're using it, anything cool you find, or any questions or suggestions. You can reach me [by email](mailto:{{site.email}}).
