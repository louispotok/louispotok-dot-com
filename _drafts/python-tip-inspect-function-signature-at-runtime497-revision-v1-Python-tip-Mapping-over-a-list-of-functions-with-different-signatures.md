---
id: 501
title: 'Python tip: Mapping over a list of functions with different signatures'
date: 2017-03-21T12:08:47-07:00
author: Louis Potok
layout: revision
guid: http://louispotok.com/497-revision-v1/
permalink: /?p=501
---
\# Problem:

I have a list of functions with different signatures. They all share the first parameter. I want to call them all with the same first argument, and for the ones with other signatures, pass the &#8220;appropriate&#8221; argument (I know this is a little hand-wavy).

Here&#8217;s a trivial example:

<pre class="brush: python; title: ; notranslate" title="">def half(a):
    return a / 2

def twice(a):
    return 2 * a

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

functions = [half, twice, addition, subtraction]
a = get_a()
b = get_b()

</pre>

Desired outcome:

<pre class="brush: python; title: ; notranslate" title="">[half(a), twice(a), addition(a,b), subtraction(a, b)]
</pre>

\# Solution 1:  
One option is to \`get\_b()\` within the functions that need them. This is not ideal, suppose \`get\_b\` is not a pure function (e.g. a network call), we would want to pass \`b\` into scope instead of getting it from elsewhere every time it&#8217;s needed.

\# Solution 2:  
We could change the signature to accept arbitrary kwargs and then pass a dict of args, for example:

<pre class="brush: python; title: ; notranslate" title="">def half(a, **kwargs):
    return a / 2

def twice(a, **kwargs):
    return 2 * a

def addition(a, **kwargs):
    return a + kwargs['b']

def subtraction(a, **kwargs):
    return a - kwargs['b']

functions = [half, twice, addition, subtraction]
a = get_a()
payload = {'b': get_b()}
results = [f(a, **payload) for f in functions]
</pre>

This isn&#8217;t great, since we need to modify the function definitions.

\# Solution 3  
Allow each function to have a different signature, inspect the signature at runtime and pass what is needed.  
(Adapted from http://stackoverflow.com/a/2677263/3393459)

<pre class="brush: python; title: ; notranslate" title="">import inspect

def half(a):
    return a / 2

def twice(a):
    return 2 * a

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

# Wrapper which looks at the signature of the function and passes the correct args
def call_func_with_correct_args(f, possible_args):
    func_args = inspect.getargspec(f).args
    args_to_pass = {k: possible_args[k] for k in func_args}
    return f(**args_to_pass)

functions = [half, twice, addition, subtraction]
a = get_a()
b = get_b()
full_payload = {'a': a, 'b': b}

results = [call_func_with_correct_args(f, full_payload) for f in functions]

</pre>