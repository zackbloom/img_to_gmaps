GitHub Example
=======

Note that the for size reasons, only a couple of zoom levels are included in the GitHub examples, and they are *very* low res.
Generate your own images to get a real idea of what it looks like.

slice.py
=======
Splits image file given as command line argument into a set of tiles in 
the static/cart_imgs folder.

Min/max zoom levels and tile width/height are configurable as constants.

The full output path is:

    static/cart_imgs/[zoom]/[x]/[y].png

*Depends on Python Image Magick (tested on Python 2.6+)*

Server
=========
The server.py file is a simple tornado server configured to serve the files
in /static on port 8888.  The example page can be reached at /static/page.html.

*Depends on tornado*

Getting Started
===========

- Get an map image file, run slice (optionally configuring the consts):
    python slice.py [image file]
- Run the dev server, or any other web server rooted at the static/ folder.
- Navigate to the page.html page:
  - With the dev server: localhost:8888/static/page.html
- Cackle with glee.
