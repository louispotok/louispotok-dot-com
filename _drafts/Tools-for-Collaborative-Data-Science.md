---
id: 517
title: Tools for Collaborative Data Science
date: 2017-04-19T09:46:40-07:00
author: Louis Potok
layout: post
guid: http://louispotok.com/?p=517
permalink: /?p=517
categories:
  - Data Science
---
Quick, what&#8217;s the hardest part of data science?

> Staying up to date on the latest machine learning research?

WRONG.

> Getting a PhD in statistics?

WRONG.

The hardest part of data science is _collaboration._ It boils down to four key characteristics:

  * Scoping
  * Execution
  * Reproducibility
  * Sharing Results

In my volunteer work for [DataKind](http://datakind.org) I build and lead teams of volunteer data scientists to work on social impact projects. These projects are especially difficult from a collaboration perspective, which has forged my thinking in an especially hot crucible. But these lessons apply in all data science projects.

**Scoping**

Deciding what to do is hard. How can data science actually help achieve your business goals or your social mission? This is a question that no data scientist can answer alone. You need to talk with people who have deep contextual understanding. We&#8217;re still figuring out the best way to do this!

Right now in academia, this looks like statisticians consulting on medical study design. In business, it looks like data scientists embedded with business units, or having a Data Science Product Manager gather requirements from other teams (remind me some day to write a post about the need for a DSPM). In the social sector it looks like DataKind or the Code for San Francisco [Data Science Brigade](http://datascience.codeforsanfrancisco.org/): experienced data scientists working closely with domain experts over a period of weeks to understand the domain and how data can be applied.

Project scoping has two streams of work that inform each other. The first is understanding the problems that would be useful to solve, and the second is understanding what data is available. The problems you can solve are constrained by the data that is available, but you can often develop data sets or find open data to match the problems you identify. In the long run this can also lead you to change your data collection so that in the future you will have the data you need to face your most pressing problems.

**Execution**

There&#8217;s a lot to this.

For one, you need to keep working with the domain experts. Data science projects involve hundreds or thousands of tiny choices, some of which are technical and some of which call on the problem domain, and many of which involve both.

For me the prototypical example is handling missing data. Handling missing data is difficult and requires different kinds of expertise:

  * First you must understand why data is missing &#8212; this requires knowledge of how the data was collected, which a data scientist may not know going in. In a business context it&#8217;s often the engineering team who can answer this one; in the social sector it may be the folks on the ground doing data collection or filling out surveys.
  * Then list your available options and understand the tradeoffs &#8212; data science expertise is needed here. You can ignore observations where _any_ data is missing or where _all_ data is missing. Or you can fill in the missing values. The tradeoffs and methods here are the subject of a very deep literature in statistics and social science so I&#8217;ll avoid going too deep.

Suffice to say that making a decision requires you to consider the tradeoffs in your particular context, and a data scientist who tries to go cowboy is going to ignore important information.

But second, any nontrivial data science project will involve collaboration with other data scientists. This could be multiple people working on something at the same time, or one person doing work that another person will expand on or need to maintain in the future.

https://engineers.sg/video/datalearn-docker-for-reproducible-research-datakind-sg&#8211;1468

https://github.com/datakind-sg/contain-yourself

https://github.com/DataKind-SG/test-driven-data-cleaning

https://github.com/drivendata/cookiecutter-data-science

Features / division of labor

**Reproducibility**

**Sharing Results**