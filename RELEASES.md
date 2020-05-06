# Instructions for creating a new release

Spinx-Toggle is [hosted on the pypi repository](https://pypi.org/project/sphinx-explorable/).
To create a new release of sphinx-explorable, you need to do these things:

## To create the release

To create a new release, [open an issue](https://github.com/ExecutableBookProject/sphinx-explorable/issues/new) to keep
track of the to-do list for the release. Copy/paste the following markdown into the issue
and check off the boxes as you complete items:


```
- [ ] Ensure that the [sphinx-explorable version number](https://github.com/ExecutableBookProject/sphinx-explorable/blob/master/sphinx_explorable/__init__.py)
   is correct, and remove the `dev0` part of the version number.
   Make a PR with the new number and merge into master.
- [ ] [Create a new release](https://github.com/executablebookproject/sphinx-explorable/releases).
  - The tag should be the current sphinx-explorable version number.
  - Add a description of what has changed since it was last-used. You can use [the `github-activity` tool](https://github.com/choldgraf/github-activity)
    to make this easier if you wish.
- [ ] Creating a new release should [trigger GitHub action to push the release to PyPI](https://github.com/ExecutableBookProject/sphinx-explorable/actions).
      The [action configuration is here](https://github.com/ExecutableBookProject/sphinx-explorable/blob/master/.github/workflows/tests.yml).
- [ ] Confirm that the new version of sphinx-explorable [is posted to pypi](https://pypi.org/project/sphinx-explorable/)
- [ ] Bump the [sphinx-explorable version number](https://github.com/ExecutableBookProject/sphinx-explorable/blob/master/sphinx_explorable/__init__.py) to
   the next minor (or major) release and append `dev0` to the end.
- [ ] Celebrate! You've just released a new version of sphinx-explorable!
```
