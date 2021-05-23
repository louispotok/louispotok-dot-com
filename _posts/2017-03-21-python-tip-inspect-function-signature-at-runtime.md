---
id: 497
title: 'Python tip: Inspect function signature at runtime'
date: 2017-03-21 13:08:07.000000000 -07:00
author: Louis Potok
layout: post
guid: http://louispotok.com/?p=497
permalink: "/python-tip-inspect-function-signature-at-runtime/"
categories:
- Python
- Uncategorized
wp_migrate: dirty
---
## Problem:

I have a list of functions with different signatures. There is some set of possible parameters, and I want to call all these functions with the &#8220;appropriate&#8221; argument for each parameter.

This is a little hand-wavy, let&#8217;s look at an example:

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

And we want to do this without making our function definitions too ugly.

## Solution 1:

One option is to \`get\_b()\` within the functions that need them. This is not ideal, suppose \`get\_b\` is not a pure function (e.g. a network call), we would want to pass \`b\` into scope instead of getting it from elsewhere every time it&#8217;s needed.

## Solution 2:

We could change the signature to accept arbitrary kwargs and then pass a dict of args, for example:

<pre class="brush: python; title: ; notranslate" title="">def half(**kwargs):
    return kwargs['a'] / 2

def twice(**kwargs):
    return 2 * kwargs['a']

def addition(**kwargs):
    return kwargs['a'] + kwargs['b']

def subtraction(**kwargs):
    return kwargs['a'] - kwargs['b']

functions = [half, twice, addition, subtraction]
payload = {'a': get_a(), 'b': get_b()}
results = [f(**payload) for f in functions]
</pre>

This works, but makes each of our function definitions uglier.

## Solution 3:

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

# Wrapper which:
# * accepts a dict of all possible kwargs and their names
# * inspects the signature of the function
# * calls that function with the correct args
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

So this is nice and clever, but we need to be careful that our function parameters are named correctly and consistently. Essentially we are passing the burden to the function definitions.

## Conclusion

I don&#8217;t know what a great solution to this might look like. Is there a better way to do this? If all the parameters are different types, Python3&#8217;s type hinting might provide another option. What does this look like in other languages?