# sphinx-explorable

[Ink components](https://iooxa.dev/) are a way of defining interactive document
elements using Web components. This package is an attempt at exposing them to
users of Sphinx via roles and directives.

The roles/directives functionality isn't quite there yet, but first it will be
a space to play around with the user interface and syntax for this behavior.

Here's some raw HTML to generate components:

```
<r-var name="cookies" value="3" format=".4"></r-var>
<p>
    When you eat <r-dynamic bind="cookies" min="2" max="100"> cookies</r-dynamic>,
    you consume <r-display bind="cookies * 50" format=".0f">150</r-display> calories.
</p>
```

It generates this output:

```{raw} html
<r-var name="cookies" value="3" format=".4"></r-var>
<p>
    When you eat <r-dynamic bind="cookies" min="2" max="100"></r-dynamic> cookies,
    you consume <r-display bind="cookies * 50" format=".0f"></r-display> calories.
</p>
```

How could this be accomplished with roles and directives? Here's one way to do it...

````
We can declare an ink dynamic variable like so:

```{ink} cookies
:value: 2
:format: .4
```

When you eat {ink:dynamic}`cookies:2-100:cookies`,
you consume {ink:display}`cookies * 50:.0f` calories.
````

In this case, the `display` and `dynamic` roles parse their values differently
and use this to configure what the output should look like (e.g. `display` allows
one to pass a formatting string).
