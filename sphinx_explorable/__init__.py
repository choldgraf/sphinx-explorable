"""A small sphinx extension to add "toggle" buttons to items."""
import os
from docutils.parsers.rst import Directive, directives
from docutils import nodes

__version__ = "0.1.1dev0"


def st_static_path(app):
    static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "_static"))
    app.config.html_static_path.append(static_path)


# We connect this function to the step after the builder is initialized
def setup(app):
    # Add our static path

    options = {"async": "async"}
    app.add_js_file("https://unpkg.com/@iooxa/components", **options)
