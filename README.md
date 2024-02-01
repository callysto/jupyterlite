# Callysto JupyterLite

Access our notebooks in JupyterLite:

* [retro](https://callysto.github.io/jupyterlite/retro)
* [lab](https://callysto.github.io/jupyterlite)

To create a "bookmarklet" that allows you to open notebooks from GitHub in this JupyterLite instance, drag this [Open in JupyterLite](javascript:(()=>{var site=location.href.split("github.com/")[1].replace(/\/blob\//,'/');newUrl="https://callysto.github.io/jupyterlite/lab/index.html?fromURL=https://raw.githubusercontent.com/"+site;window.prompt("Open in JupyterLite Link",newUrl);})();) to your bookmarks bar.

JupyterLite documentation:

* How-to Guides: https://jupyterlite.readthedocs.io/en/latest/howto/index.html
* Reference: https://jupyterlite.readthedocs.io/en/latest/reference/index.html
