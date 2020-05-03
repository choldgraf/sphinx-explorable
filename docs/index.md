# sphinx-ink

```{raw} html
<ink-var name="cookies" value="3" format=".4"></ink-var>
<p>
    When you eat <ink-dynamic name="cookies" min="2" max="100"> cookies</ink-dynamic>,
    you consume <ink-display :value="cookies * 50" format=".0f">150</ink-display> calories.
</p>
```